# Court Case Search

A Python library for searching Tunisian court cases.

## Installation

You can install the library using pip:

```
pip install tun_justice
```

## Usage

Here's a basic example of how to use the library:

```python
from tun_justice import MadaniCase, MahdharCase, JazaiiCase, Tribunal

import logging

# Configure the root logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Optionally, set a specific level for the tun_justice logger
logging.getLogger("tun_justice").setLevel(logging.DEBUG)

case = MadaniCase(
    tribunal=Tribunal("محكمة ناحية باردو"), annee="2023", numero_dossier="10737"
)
case1 = MahdharCase(
    tribunal=Tribunal("المحكمة الابتدائية بنابل"), annee="2023", numero_dossier="3"
)
case2 = JazaiiCase(
    tribunal=Tribunal("1100"), annee="2023", numero_dossier="4"
)  # محكمة الاستئناف بتونس

results = [c.search() for c in [case, case1, case2]]

for result in results:
    print("-------------------------------------")
    for case in result:
        print(f"Case Number: {case.numero_dossier}")
        print(f"Type of Case: {case.tribunal}")
        print("Details:")
        print(case.details)

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.