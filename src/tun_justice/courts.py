from dataclasses import dataclass
from typing import Optional


@dataclass
class CourtOption:
    value: str
    label: str

    def __str__(self):
        return f"{self.label}"


# List of court options
court_options = [
    CourtOption(value="1100", label="محكمة الاستئناف بتونس"),
    CourtOption(value="1102", label="محكمة الاستئناف ببنزرت"),
    CourtOption(value="1101", label="محكمة الاستئناف بنابل"),
    CourtOption(value="1200", label="محكمة الاستئناف بصفاقس"),
    CourtOption(value="1300", label="محكمة الاستئناف بسوسة"),
    CourtOption(value="1400", label="محكمة الاستئناف بالكاف"),
    CourtOption(value="1500", label="محكمة الاستئناف بالمنستير"),
    CourtOption(value="1600", label="محكمة الاستئناف بقفصة"),
    CourtOption(value="1700", label="محكمة الاستئناف بمدنين"),
    CourtOption(value="1800", label="محكمة الاستئناف بقابس"),
    CourtOption(value="2200", label="محكمة الاستئناف بالقصرين"),
    CourtOption(value="2300", label="محكمة الاستئناف بسيدى بوزيد"),
    CourtOption(value="2400", label="محكمة الاستئناف بالقيروان"),
    CourtOption(value="2500", label="محكمة الاستئناف بجندوبة"),
    CourtOption(value="2600", label="محكمة الاستئناف بباجة"),
    CourtOption(value="2700", label="محكمة الاستئناف بسليانة"),
    CourtOption(value="1110", label="المحكمة الابتدائية بتونس"),
    CourtOption(value="1180", label="المحكمة الابتدائية باريانة"),
    CourtOption(value="1170", label="المحكمة الابتدائية ببنعروس"),
    CourtOption(value="1190", label="المحكمة الابتدائية منوبة"),
    CourtOption(value="1130", label="المحكمة الابتدائية بتونس 2"),
    CourtOption(value="1120", label="المحكمة الابتدائية ببنزرت"),
    CourtOption(value="1140", label="المحكمة الابتدائية بباجة"),
    CourtOption(value="1150", label="المحكمة الابتدائية بزغوان"),
    CourtOption(value="1160", label="المحكمة الابتدائية بقرمبالية"),
    CourtOption(value="1220", label="المحكمة الابتدائية بصفاقس 2"),
    CourtOption(value="1910", label="المحكمة الابتدائية بنابل"),
    CourtOption(value="1210", label="المحكمة الابتدائية بصفاقس"),
    CourtOption(value="1310", label="المحكمة الابتدائية بسوسة"),
    CourtOption(value="1320", label="المحكمة الابتدائية بالقيروان"),
    CourtOption(value="1410", label="المحكمة الابتدائية بالكاف"),
    CourtOption(value="1420", label="المحكمة الابتدائية بسليانة"),
    CourtOption(value="1430", label="المحكمة الابتدائية بالقصرين"),
    CourtOption(value="1440", label="المحكمة الابتدائية بجندوبة"),
    CourtOption(value="1510", label="المحكمة الابتدائية بالمنستير"),
    CourtOption(value="1520", label="المحكمة الابتدائية بالمهدية"),
    CourtOption(value="1610", label="المحكمةالابتدائية بقفصة"),
    CourtOption(value="1620", label="المحكمة الابتدائية بسيدي بوزيد"),
    CourtOption(value="1630", label="المحكمة الابتدائية بتوزر"),
    CourtOption(value="1710", label="المحكمة الابتدائية بمدنين"),
    CourtOption(value="1720", label="المحكمة الابتدائية بتطاوين"),
    CourtOption(value="1810", label="المحكمة الابتدائية بقابس"),
    CourtOption(value="1820", label="المحكمة الابتدائية بقبلي"),
    CourtOption(value="1330", label="المحكمة الابتدائية بسوسة 2"),
    CourtOption(value="1111", label="محكمة ناحية تونس"),
    CourtOption(value="1113", label="محكمة ناحية باردو"),
    CourtOption(value="1114", label="محكمة ناحية قرطاج"),
    CourtOption(value="1115", label="محكمة ناحية حي الزهور"),
    CourtOption(value="1116", label="محكمة ناحية الوردية"),
    CourtOption(value="1121", label="محكمة ناحية بنزرت"),
    CourtOption(value="1122", label="محكمة ناحية منزل بورقيبة"),
    CourtOption(value="1123", label="محكمة ناحية ماطر"),
    CourtOption(value="1124", label="محكمة ناحية راس الجبل"),
    CourtOption(value="1141", label="محكمة ناحية باجة"),
    CourtOption(value="1142", label="محكمة ناحية مجاز الباب"),
    CourtOption(value="1143", label="محكمة ناحية تبرسق"),
    CourtOption(value="1151", label="محكمة ناحية زغوان"),
    CourtOption(value="1153", label="محكمة ناحية الفحص"),
    CourtOption(value="1162", label="محكمة ناحية نابل"),
    CourtOption(value="1161", label="محكمة ناحية قرمبالية"),
    CourtOption(value="1163", label="محكمة ناحية منزل تميم"),
    CourtOption(value="1164", label="محكمة ناحية الحمامات"),
    CourtOption(value="1171", label="محكمة ناحية بن عروس"),
    CourtOption(value="1172", label="محكمة ناحية حمام الانف"),
    CourtOption(value="1181", label="محكمة ناحية أريانة"),
    CourtOption(value="1211", label="محكمة ناحية صفاقس"),
    CourtOption(value="1212", label="محكمة ناحية جبنيانة"),
    CourtOption(value="1213", label="محكمة ناحية المحرس"),
    CourtOption(value="1214", label="محكمة ناحية عقارب"),
    CourtOption(value="1311", label="محكمة ناحية سوسة"),
    CourtOption(value="1312", label="محكمة ناحية مساكن"),
    CourtOption(value="1313", label="محكمة ناحية النفيضة"),
    CourtOption(value="1321", label="محكمة ناحية القيروان"),
    CourtOption(value="1322", label="محكمة ناحية حفوز"),
    CourtOption(value="1323", label="محكمة ناحية بوحجلة"),
    CourtOption(value="1324", label="محكمة ناحية الوسلاتية"),
    CourtOption(value="1325", label="محكمة ناحية السبيخة"),
    CourtOption(value="1411", label="محكمة ناحية الكاف"),
    CourtOption(value="1412", label="محكمة ناحية تاجروين"),
    CourtOption(value="1413", label="محكمة ناحية الدهماني"),
    CourtOption(value="1421", label="محكمة ناحية سليانة"),
    CourtOption(value="1422", label="محكمة ناحية مكثر"),
    CourtOption(value="1423", label="محكمة ناحية قعفور"),
    CourtOption(value="1431", label="محكمة ناحية القصرين"),
    CourtOption(value="1432", label="محكمة ناحية تالة"),
    CourtOption(value="1433", label="محكمة ناحية سبيطلة"),
    CourtOption(value="1434", label="محكمة ناحية سبيبة"),
    CourtOption(value="1435", label="محكمة ناحية فريانة"),
    CourtOption(value="1441", label="محكمة ناحية جندوبة"),
    CourtOption(value="1442", label="محكمة ناحية بوسالم"),
    CourtOption(value="1443", label="محكمة ناحية عين دراهم"),
    CourtOption(value="1444", label="محكمة ناحية غار الدماء"),
    CourtOption(value="1512", label="محكمة ناحية جمال"),
    CourtOption(value="1513", label="محكمة ناحية مكنين"),
    CourtOption(value="1521", label="محكمة ناحية المهدية"),
    CourtOption(value="1522", label="محكمة ناحية السواسي"),
    CourtOption(value="1523", label="محكمة ناحية الجم"),
    CourtOption(value="1524", label="محكمة ناحية قصور الساف"),
    CourtOption(value="1525", label="محكمة ناحية الشابة"),
    CourtOption(value="1611", label="محكمة ناحية قفصة"),
    CourtOption(value="1613", label="محكمة ناحية المتلوي"),
    CourtOption(value="1621", label="محكمة ناحية سيدي بوزيد"),
    CourtOption(value="1622", label="محكمة ناحية بنعون"),
    CourtOption(value="1623", label="محكمة ناحية المكناسي"),
    CourtOption(value="1631", label="محكمة ناحية توزر"),
    CourtOption(value="1711", label="محكمة ناحية مدنين"),
    CourtOption(value="1713", label="محكمة ناحية بنقردان"),
    CourtOption(value="1714", label="محكمة ناحية جرجيس"),
    CourtOption(value="1715", label="محكمة ناحية جربة"),
    CourtOption(value="1721", label="محكمة ناحية تطاوين"),
    CourtOption(value="1811", label="محكمة ناحية قابس"),
    CourtOption(value="1812", label="محكمة ناحية الحامة"),
    CourtOption(value="1813", label="محكمة ناحية مارث"),
    CourtOption(value="1814", label="محكمة ناحية مطماطة"),
    CourtOption(value="1821", label="محكمة ناحية قبلي"),
    CourtOption(value="14511", label="محكمة ناحية المنستير"),
    CourtOption(value="1221", label="محكمة ناحية صفاقس 2"),
    CourtOption(value="1215", label="محكمة ناحية ساقية الزيت"),
    CourtOption(value="1722", label="محكمة ناحية غمراسن"),
    CourtOption(value="1436", label="محكمة ناحية فوسانة"),
    CourtOption(value="14514", label="محكمة ناحية طبرقة"),
    CourtOption(value="1625", label="محكمة ناحية جلمة"),
    CourtOption(value="1624", label="محكمة ناحية الرقاب"),
    CourtOption(value="14512", label="محكمة ناحية منزل بوزلفة"),
    CourtOption(value="1192", label="محكمة ناحية طبربة"),
    CourtOption(value="1184", label="محكمة الناحية حي التضامن"),
    CourtOption(value="1191", label="محكمة ناحية منوبة"),
    CourtOption(value="1331", label="محكمة ناحية سوسة 2"),
    CourtOption(value="1216", label="محكمة ناحية بئر علي بن خليفة"),
    CourtOption(value="1822", label="محكمة ناحية نفزة"),
]


def get_court_option_from_name(name: str) -> Optional[CourtOption]:
    for court in court_options:
        if court.label == name:
            return court
    return None


# Function to get the value from the label
def get_court_id_from_name(name: str) -> Optional[str]:
    for court in court_options:
        if court.label == name:
            return court.value
    return None


# Function to get the label from the value
def get_court_name_from_id(id: str) -> Optional[str]:
    for court in court_options:
        if court.value == id:
            return court.label
    return None


class TribunalException(Exception):
    pass


class Tribunal:
    def __init__(self, name: str):
        self.name = name
        self.court_option = get_court_option_from_name(name)
        if self.court_option is None:
            raise TribunalException(f"Court {name} not found")

    def get_id(self) -> str:
        return self.court_option.value


if __name__ == "__main__":
    # Example of getting value from label
    label = "محكمة الاستئناف بتونس"
    value = get_court_id_from_name(label)
    assert value == "1100", "Value should be 1100"

    # Example of getting label from value
    value = "1100"
    label = get_court_name_from_id(value)
    assert label == "محكمة الاستئناف بتونس", "Label should be محكمة الاستئناف بتونس"

    tribubal = Tribunal("محكمة الاستئناف بتونس")
    assert tribubal.get_id() == "1100", "Value should be 1100"
