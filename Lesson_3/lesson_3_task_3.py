from mailing import Mailing
from address import Address

to_address = Address("333555", "Казань", "Гагарина", "1", "11")
from_address = Address("666999", "Набережные Челны", "Строителей", "2", "22")
mailing = Mailing(to_address, from_address, 9100, "0123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
