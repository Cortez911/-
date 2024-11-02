from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Realme", "8 5G", "+79171111111"))
catalog.append(Smartphone("Samsung", "A22", "+79600000000"))
catalog.append(Smartphone("Alcatel", "911 sos", "+79874444444"))
catalog.append(Smartphone("Redme", "9 a", "+79278888888"))
catalog.append(Smartphone("Mororolla", "razer v 3i", "+79050203789"))

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.phone_number}")
