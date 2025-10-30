from Address import Address
from Mailing import Mailing

to_address = Address (187110, "Кириши", "Восточная", "9", "24")
from_address = Address (187112, "Кириши", "Ленина", "36", "84")
track = "Отправление" 
cost = 200

sending = Mailing (to_address = to_address, from_address = from_address, cost = 200, track = 25)


print(sending)