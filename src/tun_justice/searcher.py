import logging
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict
from dataclasses import dataclass
from .courts import Tribunal

logger = logging.getLogger(__name__)


@dataclass
class CaseDetail:
    phase: str
    action_number: str
    action: str
    date: str
    text: str


@dataclass
class CourtCase:
    tribunal: str
    type_de_case: str
    numero_dossier: str
    annee: str
    sujet: str
    type_affaire: str
    details: List[CaseDetail]


class CourtCaseSearcher:
    BASE_URL = "http://services.e-justice.tn/consultation/tdossierpalier2list.php"
    DETAIL_BASE_URL = "http://services.e-justice.tn/consultation/"

    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize the CourtCaseSearcher.

        Args:
            log_level (int): The logging level to use. Defaults to logging.INFO.
        """
        logging.basicConfig(
            level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    @staticmethod
    def _format_detail_html(html: str) -> List[CaseDetail]:
        """
        Extract and format case details from HTML into a list of CaseDetail objects.

        Args:
            html (str): The HTML content of the detail page.

        Returns:
            List[CaseDetail]: A list of CaseDetail objects containing formatted case details.
        """
        soup = BeautifulSoup(html, "html.parser")
        details = []

        table_body = soup.find("tbody")
        if table_body:
            rows = table_body.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    details.append(
                        CaseDetail(
                            phase=cols[0].get_text(strip=True),
                            action_number=cols[1].get_text(strip=True),
                            action=cols[2].get_text(strip=True),
                            date=cols[3].get_text(strip=True),
                            text=cols[4].get_text(strip=True),
                        )
                    )

        return details

    def search(
        self, tribunal: Tribunal, annee: str, numero: str
    ) -> Optional[List[CourtCase]]:
        """
        Search for court cases based on the provided parameters.

        Args:
            tribunal (str): The tribunal code.
            annee (str): The year of the case.
            numero (str): The case number.

        Returns:
            Optional[List[CourtCase]]: A list of CourtCase objects containing case information,
                                       or None if the search fails.
        """
        logger.info(
            f"Starting court case search: Tribunal={tribunal}, Année={annee}, Numéro={numero}"
        )

        params = {
            "x_TRIBUNAL": tribunal.get_id(),
            "z_TRIBUNAL": "=",
            "x_DOSSIER": numero,
            "z_DOSSIER": "=",
            "x_ANNEE": annee,
            "z_ANNEE": "=",
            "cmd": "search",
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            logger.info("Successfully fetched the search results page")

            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", id="tbl_tdossierpalier2list")

            if not table:
                logger.warning("No results table found on the page")
                return []

            result_data = []
            rows = table.find_all("tr")
            logger.info(f"Found {len(rows)} rows in the table")

            for row in rows[1:]:  # Skip header row
                cells = row.find_all("td")
                if len(cells) >= 7:
                    case_details = []
                    data_url_div = row.select_one("[data-url]")
                    if data_url_div:
                        data_url = data_url_div["data-url"]
                        detail_url = f"{self.DETAIL_BASE_URL}{data_url}"
                        detail_response = requests.get(detail_url)
                        if detail_response.status_code == 200:
                            case_details = self._format_detail_html(
                                detail_response.text
                            )
                            logger.info(
                                f"Fetched detailed info for case {cells[2].text.strip()}"
                            )
                        else:
                            logger.error(
                                f"Failed to fetch details for case {cells[2].text.strip()}"
                            )

                    court_case = CourtCase(
                        tribunal=cells[0].text.strip(),
                        type_de_case=cells[1].text.strip(),
                        numero_dossier=cells[2].text.strip(),
                        annee=cells[4].text.strip(),
                        sujet=cells[5].text.strip(),
                        type_affaire=cells[6].text.strip(),
                        details=case_details,
                    )

                    result_data.append(court_case)
                    logger.info(
                        f"Added data for case {court_case.numero_dossier} to results"
                    )

            logger.info(
                f"Completed processing all rows. Total cases found: {len(result_data)}"
            )
            return result_data

        except requests.RequestException as e:
            logger.error(f"An error occurred during the request: {str(e)}")
            return None
