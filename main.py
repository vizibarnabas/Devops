from auto import Auto

autok = [
    Auto("Toyota", "Corolla", 2020, "Benzin", 180),
    Auto("Ford", "Focus", 2018, "Dízel", 190),
    Auto("BMW", "X5", 2022, "Elektromos", 220),
    Auto("Audi", "A4", 2019, "Benzin", 210)
]

for auto in autok:
    print(auto.adatok())

autok[-1].set_sebesseg(200)
print(f"\nAz utolsó autó új sebessége: {autok[-1].get_sebesseg()} km/h")
