events = {
    "George Gershwin: Porgy and Bess": "18.09.2026",
    "SUPERHEROES": "18.09.2026",
    "Connected - Digitale Kultur im Ruhrgebiet": "19.09.2026",
    "Unter der Lupe": "19.09.2026",
    "Phoenix Hörde": "20.09.2026",
    "Stahlzeit in Dortmund": "20.09.2026"
}

print("\nEvents in Dortmund:")
for event, date in events.items():
    print(event, "-", date)

print("\nEvents during the Night of Museums:")
for event, date in events.items():
    if date == "19.09.2026":
        print(event)