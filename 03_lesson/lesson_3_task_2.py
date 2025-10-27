from smartphone import Smartphone

catalog = [
    Smartphone ("Nokia", "music",  "+79934567656"),
    Smartphone ("Apple",  "13 Pro max",  "+79062844535"),
    Smartphone ("Samsung",  "Ultra 24",  "+79992182394"),
    Smartphone ("Xiaomi",  "X9",  "+79650062645"),
    Smartphone ("Nokia",  "3310",  "+799921824242")
]
    
    


for smartphone in catalog:
    print (f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")