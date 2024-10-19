import logging
import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict
from dataclasses import dataclass
from .courts import Tribunal
from typing import ClassVar
import time
import inspect

logger = logging.getLogger(__name__)


class Case:
    DETAIL__BASE_URL = "https://services.justice.gov.tn/consultation/"

    def search(self):  # todo add return type
        logger.debug(
            f"Starting court case search: Tribunal={self.tribunal}, Année={self.annee}, Numéro={self.numero_dossier}"
        )

        params = self._get_params()

        retries = 5
        while retries > 0:
            try:
                logger.debug(f"Requesting search results page, retries left: {retries}")
                response = requests.get(self._BASE_URL, params=params, timeout=20)
                logger.debug(f"requesting: {response.url}")
                response.raise_for_status()
                logger.info("Successfully fetched the search results page")

                soup = BeautifulSoup(response.text, "html.parser")
                table = soup.find("table", id=self._TABLE_ID)

                if not table:
                    logger.warning("No results table found on the page")
                    return []

                result_data = []
                rows = table.find_all("tr")
                logger.info(f"Found {len(rows)} rows in the table")

                for row in rows[1:]:  # Skip header row
                    cells = row.find_all("td")
                    logger.debug(f"Found {len(cells)} cells in the row")
                    if len(cells) >= self._field_count:
                        case_details = []
                        data_url_div = row.select_one("[data-url]")
                        if data_url_div:
                            data_url = data_url_div["data-url"]
                            detail_url = f"{self.DETAIL__BASE_URL}{data_url}"
                            logger.debug(f"Requesting data-url: {detail_url}")
                            detail_response = requests.get(detail_url)
                            if detail_response.status_code == 200:
                                case_details = self._format_detail_html(
                                    detail_response.text
                                )
                            else:
                                logger.error(
                                    f"Failed to fetch details for case {cells[2].text.strip()}"
                                )

                        court_case = self._get_case(cells, case_details)

                        result_data.append(court_case)
                        logger.info(
                            f"Added data for case {court_case.numero_dossier} to results"
                        )

                logger.info(
                    f"Completed processing all rows. Total cases found: {len(result_data)}"
                )
                return result_data
            except requests.Timeout:
                logger.warning("Request timed out, retrying...")
                time.sleep(0.5)
                retries -= 1
            except requests.ConnectionError as e:
                if "[Errno -3] Temporary failure in name resolution" in str(e.args):
                    logger.debug("Failed name resolution, trying again...")
                    time.sleep(0.5)
                    retries -= 1
            except requests.RequestException as e:
                logger.error(f"An error occurred during the request: {str(e)}")
                return None


###################### Mahdhar
@dataclass
class MahdharCaseDetail:

    action_number: str
    action: str
    date: str
    text: str


class MahdharCase(Case):
    _BASE_URL = "https://services.justice.gov.tn/consultation/tdocumentlist.php"
    _TABLE_ID: ClassVar[str] = "tbl_tdocumentlist"
    _field_count: ClassVar[int] = 6

    def __init__(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.document_type: str = None
        self.date_entree: str = None
        self.details: List[MahdharCaseDetail] = None

    def _create(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
        document_type: str,
        date_entree: str,
        details: List[MahdharCaseDetail],
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.document_type: str = document_type
        self.date_entree: str = date_entree
        self.details: List[MahdharCaseDetail] = details
        return self

    def _get_params(self) -> Dict[str, str]:
        return {
            "x_TRIBUNAL": self.tribunal.get_id(),
            "z_TRIBUNAL": "=",
            "x_MASTERDOS": self.numero_dossier,
            "z_MASTERDOS": "=",
            "x_ANNEEMASTERDOS": self.annee,
            "z_ANNEEMASTERDOS": "=",
            "cmd": "search",
        }

    @staticmethod
    def _format_detail_html(html: str) -> List[MahdharCaseDetail]:
        soup = BeautifulSoup(html, "html.parser")
        details = []

        table_body = soup.find("tbody")
        if table_body:
            rows = table_body.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 4:
                    details.append(
                        MahdharCaseDetail(
                            action_number=cols[0].get_text(strip=True),
                            action=cols[1].get_text(strip=True),
                            date=cols[2].get_text(strip=True),
                            text=cols[3].get_text(strip=True),
                        )
                    )

        return details

    def _get_case(self, cells, case_details: MahdharCaseDetail):
        return self._create(
            document_type=cells[0].text.strip(),
            tribunal=cells[1].text.strip(),
            numero_dossier=cells[2].text.strip(),
            annee=cells[3].text.strip(),
            date_entree=cells[4].text.strip(),
            details=case_details,
        )


#####################" Madani
@dataclass
class MadaniCaseDetail:
    phase: str
    action_number: str
    action: str
    date: str
    text: str

    def __str__(self):
        return f"Phase: {self.phase}, Action Number: {self.action_number}, Action: {self.action}, Date: {self.date}, Text: {self.text}"


class MadaniCase(Case):
    _BASE_URL = "https://services.justice.gov.tn/consultation/tdossierpalier2list.php"
    _TABLE_ID: ClassVar[str] = "tbl_tdossierpalier2list"
    _field_count: ClassVar[int] = 7

    def __init__(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.type_de_case: str = None
        self.sujet: str = None
        self.type_affaire: str = None
        self.details: List[MadaniCaseDetail] = None

    def _create(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
        type_de_case=None,
        sujet=None,
        type_affaire=None,
        details=None,
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.type_de_case = type_de_case
        self.sujet = sujet
        self.type_affaire = type_affaire
        self.details = details
        return self

    def _get_params(self) -> Dict[str, str]:
        return {
            "x_TRIBUNAL": self.tribunal.get_id(),
            "z_TRIBUNAL": "=",
            "x_DOSSIER": self.numero_dossier,
            "z_DOSSIER": "=",
            "x_ANNEE": self.annee,
            "z_ANNEE": "=",
            "cmd": "search",
        }

    @staticmethod
    def _format_detail_html(html: str) -> List[MadaniCaseDetail]:
        soup = BeautifulSoup(html, "html.parser")
        details = []

        table_body = soup.find("tbody")
        if table_body:
            rows = table_body.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    details.append(
                        MadaniCaseDetail(
                            phase=cols[0].get_text(strip=True),
                            action_number=cols[1].get_text(strip=True),
                            action=cols[2].get_text(strip=True),
                            date=cols[3].get_text(strip=True),
                            text=cols[4].get_text(strip=True),
                        )
                    )

        return details

    def _get_case(self, cells, case_details: MadaniCaseDetail):
        return self._create(
            tribunal=cells[0].text.strip(),
            type_de_case=cells[1].text.strip(),
            numero_dossier=cells[2].text.strip(),
            annee=cells[4].text.strip(),
            sujet=cells[5].text.strip(),
            type_affaire=cells[6].text.strip(),
            details=case_details,
        )


#####################" Jazaii
@dataclass
class JazaiiCaseDetail:
    action_number: str
    action: str
    date: str
    text: str


class JazaiiCase(Case):
    _BASE_URL = "https://services.justice.gov.tn/consultation/tdossierpalierlist.php"
    _TABLE_ID: ClassVar[str] = "tbl_tdossierpalierlist"
    _field_count: ClassVar[int] = 10

    def __init__(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.palier: str = None
        self.type_affaire: str = None
        self.numero_affaire: str = None
        self.annee_affaire: str = None
        self.sujet: str = None
        self.remarques: str = None
        self.decision: str = None
        self.details: List[JazaiiCaseDetail] = None

    def _create(
        self,
        tribunal: Tribunal,
        numero_dossier: str,
        annee: str,
        palier: str,
        type_affaire: str,
        numero_affaire: str,
        annee_affaire: str,
        sujet: str,
        remarques: str,
        decision: str,
        details: List[JazaiiCaseDetail],
    ):
        self.tribunal = tribunal
        self.numero_dossier = numero_dossier
        self.annee = annee
        self.palier = palier
        self.type_affaire = type_affaire
        self.numero_affaire = numero_affaire
        self.annee_affaire = annee_affaire
        self.sujet = sujet
        self.remarques = remarques
        self.decision = decision
        self.details = details
        return self

    def _get_params(self) -> Dict[str, str]:
        return {
            "x_TRIBUNAL": self.tribunal.get_id(),
            "z_TRIBUNAL": "=",
            "x_DOSSIER": self.numero_dossier,
            "z_DOSSIER": "=",
            "x_ANNEE": self.annee,
            "z_ANNEE": "=",
            "cmd": "search",
        }

    @staticmethod
    def _format_detail_html(html: str) -> List[JazaiiCaseDetail]:
        soup = BeautifulSoup(html, "html.parser")
        details = []

        table_body = soup.find("tbody")
        if table_body:
            rows = table_body.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 4:
                    details.append(
                        JazaiiCaseDetail(
                            action_number=cols[0].get_text(strip=True),
                            action=cols[1].get_text(strip=True),
                            date=cols[2].get_text(strip=True),
                            text=cols[3].get_text(strip=True),
                        )
                    )

        return details

    def _get_case(self, cells, case_details: JazaiiCaseDetail):
        return self._create(
            tribunal=cells[0].text.strip(),
            palier=cells[1].text.strip(),
            type_affaire=cells[2].text.strip(),
            numero_dossier=cells[3].text.strip(),
            annee=cells[4].text.strip(),
            numero_affaire=cells[5].text.strip(),
            annee_affaire=cells[6].text.strip(),
            sujet=cells[7].text.strip(),
            remarques=cells[8].text.strip(),
            decision=cells[9].text.strip(),
            details=case_details,
        )
