# Court Case Search

A Python library for searching Tunisian court cases.

## Installation

You can install the library using pip:

```
pip install court_case_search
```

## Usage

Here's a basic example of how to use the library:

```python
from tun_justice import CourtCaseSearcher, Tribunal

searcher = CourtCaseSearcher()
results = searcher.search(tribunal=Tribunal("محكمة ناحية باردو"), annee="2023", numero="10737")

if results:
    for case in results:
        print(f"Case Number: {case.numero_dossier}")
        print(f"Subject: {case.sujet}")
        print(f"Type of Case: {case.type_de_case}")
        print(f"Type of Affair: {case.type_affaire}")
        print("Details:")
        for detail in case.details:
            print(f"  - Date: {detail.date}")
            print(f"    Action: {detail.action}")
            print(f"    Phase: {detail.phase}")
            print(f"    Text: {detail.text}")
        print("---")
else:
    print("No results found or an error occurred.")
```

## API Reference

### CourtCaseSearcher

The main class for searching court cases.

#### Methods:

- `__init__(self, log_level: int = logging.INFO)`: Initialize the searcher with an optional log level.
- `search(self, tribunal: str, annee: str, numero: str) -> Optional[List[CourtCase]]`: Search for court cases based on the provided parameters.

### CourtCase

A dataclass representing a court case.

#### Attributes:

- `tribunal: str`: The tribunal code.
- `type_de_case: str`: The type of the case.
- `numero_dossier: str`: The case number.
- `annee: str`: The year of the case.
- `sujet: str`: The subject of the case.
- `type_affaire: str`: The type of affair.
- `details: List[CaseDetail]`: A list of detailed actions related to the case.

### CaseDetail

A dataclass representing detailed information about a specific action in a court case.

#### Attributes:

- `phase: str`: The phase of the action.
- `action_number: str`: The number of the action.
- `action: str`: The description of the action.
- `date: str`: The date of the action.
- `text: str`: Additional text related to the action.

## Error Handling

The `search` method returns `None` if an error occurs during the search process. It's recommended to check if the result is not `None` before processing it.

## Logging

The library uses Python's built-in `logging` module. You can set the log level when initializing the `CourtCaseSearcher`:

```python
import logging
from tun_justice import CourtCaseSearcher

searcher = CourtCaseSearcher(log_level=logging.DEBUG)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.