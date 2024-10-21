from auto import Auto

autok = [
    Auto("Toyota", "Corolla", 2020, "Benzin", 180),
    Auto("Ford", "Focus", 2018, "Dízel", 190),
    Auto("BMW", "iX5", 2022, "Elektromos", 220),
    Auto("Audi", "A4", 2019, "Benzin", 210)
]

for auto in autok:
    print(auto.adatok())

autok[-1].set_sebesseg(200)
print(f"\nAz utolsó autó új sebessége: {autok[-1].get_sebesseg()} km/h")

autok[2].set_sebesseg(170)
print(f"Az {autok[2].get_uzemanyag()} {autok[2].get_modell()}-nek csak {autok[2].get_sebesseg()} a végsebessége.")