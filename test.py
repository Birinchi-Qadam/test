
def royhat():

    ism_sharif = input("Ism Familyangizni kiriting:\n>>>  ")
    natija = dict(x.split() for x in ism_sharif.splitlines())

    print()
    
    for ism, familya in natija.items():
        print(f"Ism: {ism.title()} \nFamilya: {familya.title()}")

royhat()