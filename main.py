from datetime import date
import sys
diena = date.today()
sodiena = diena.strftime("%d/%m/%Y")
d = int(diena.strftime("%d"))
m = int(diena.strftime("%m"))
g = int(diena.strftime("%Y"))
class menu:
    def __init__(pasa, izvele):
        pasa.izvele = izvele
        if izvele == "A":
            skaits = 0
            file = open("rezervacijas.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                skaits += 1

            if skaits == 0:
                print("Nav rezervāciju!")
                print()
            else:
                file = open("rezervacijas.txt", "r")
                print(file.read())
                file.close()

        elif izvele == "B":
            with open("rezervacijas.txt", "r") as file:
                for ped_rinda in file:
                    pass

            if ped_rinda[0] == "#":
                num = 1
            else:
                num = int(ped_rinda[0]) + 1

            vards = input("Ievadi savu vārdu: ")
            datums = input("Ievadi datumu(dd/mm/yyyy):") 
            laiks,b = input("Ievadi vēlamo laiku: ").split(':')
            laiks = int(laiks)
            if laiks>17 or laiks<8:
              sys.exit("Serviss šajā laikā nav atvērts!")
              
            problema = input("Īsi apraksti savu problēmu: ")
            marka = input("Ievadi savu auto marku: ")
            telefons = int(input("Ievadi savu telefona numuru:"))
            file = open("rezervacijas.txt", "a")
            file.write(f"{num}\t\t\t\t{vards}\t\t\t\t{datums}\t\t\t\t{laiks}\t\t\t\t{problema}\t\t\t\t{marka}\t\t\t\t{telefons}\n")
            file.close()
            print()


        elif izvele == "C":
            resnum = input("Ievadi pieteikuma numuru: ")
            file1 = open("rezervacijas.txt", "r")
            lines = file1.readlines()
            file1.close()
            file2 = open("rezervacijas.txt", "w")

            for line in lines:
                if not line.startswith(resnum):
                    file2.write(line)
            file2.close()

        elif izvele == "D":
            sys.exit("Paldies Jums!")

        else:
            print("Nezināma izvēle. Lūdzu mēģiniet vēlreiz.")


while True:
    try:
        file = open("rezervacijas.txt", "r")
    except FileNotFoundError:
        file = open("rezervacijas.txt", "w+")
        file.write("#\t\t\tVārds\t\t\t        Datums\t\t\t        Laiks\t\t\t    Problēma\t\t\t Marka    \t\t\tTelefons\n")
    file.close()

    print(f"Autoservisa pieteikšānās sistēma, strādājam no 08:00 - 17:00, šodien ir {sodiena}")
    print("Sistēmas iespējas:")
    print("A. Apskatīt visus pieteikumus\tB. Pierakstīties pakalpojumam")
    print("C. Izdzēst pieteikumu\t\tD. Iziet")
  
    izveles_menu = input('Ievadi savu izvēli: ').upper()
    menu(izveles_menu)