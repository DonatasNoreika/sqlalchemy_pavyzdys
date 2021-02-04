
from modules.projektas import Projektas, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# projektas1 = Projektas("Naujas pr.", 20000)
# projektas2 = Projektas("2 projektas", 55000)
# session.add(projektas1)
# session.add(projektas2)
# session.commit()

# READ

# projektas1 = session.query(Projektas).get(1)
# # print(projektas1)
#
# projektas2 = session.query(Projektas).filter_by(name="2 projektas").first()
# # print(projektas2)
#
# projektai = session.query(Projektas).all()
#
# for projektas in projektai:
#     print(projektas)

# UPDATE

# projektas1 = session.query(Projektas).get(1)
# print(projektas1)
# projektas1.price = 22000
# session.commit()

# DELETE
# projektas1 = session.query(Projektas).get(1)
# session.delete(projektas1)
# session.commit()

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