from modules.projektas import Projektas, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite: 1 - projekto įvedimas, 2 - ištrinti projektą, 8 - peržiūrėti projektus"))
    if pasirinkimas == 1:
        pavadinimas = input("Įveskite projekto pavadinimą")
        kaina = input("Įveskite projekto kainą")
        projektas = Projektas(pavadinimas, kaina)
        session.add(projektas)
        session.commit()
    if pasirinkimas == 2:
        visi = session.query(Projektas).all()
        for projektas in visi:
            print(projektas)
        numeris = int(input("Pasirinkite norimo ištrinti įrašo ID"))
        trinamas_projektas = session.query(Projektas).get(numeris)
        session.delete(trinamas_projektas)
        session.commit()
    if pasirinkimas == 8:
        visi = session.query(Projektas).all()
        for projektas in visi:
            print(projektas)
