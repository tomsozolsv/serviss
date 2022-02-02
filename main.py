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
            datums = input("Ievadi datumu(dd/mm/yyyy): ")
            laiks = input("Ievadi vēlamo laiku: ")
            problema = input("Īsi apraksti savu problēmu: ")
            marka = input("Ievadi savu auto marku: ")
            file = open("rezervacijas.txt", "a")
            file.write(f"{num}\t\t\t{vards}\t\t\t{datums}\t\t\t{laiks}\t\t\t{problema}\t\t\t{marka}\n")
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
            import sys
            sys.exit("Paldies Jums!")

        else:
            print("Notikusi ķļūda. Lūdzu mēģiniet vēlreiz.")


while True:
    try:
        file = open("rezervacijas.txt", "r")
    except FileNotFoundError:
        file = open("rezervacijas.txt", "w+")
        file.write("#\t\t\tVards\t\t\t        Datums\t\t\t        Laiks\t\t\t    Problema\t\t\t Marka\n")
    file.close()

    print("Autoservisa pieteikšānās sistēma")
    print("Sistēmas iespējas:")
    print("A. Apskatīt visus pieteikumus\tB. Pierakstīties pakalpojumam")
    print("C. Izdzēst pieteikumu\t\tD. Iziet")
  
    izveles_menu = input('Ievadi savu izvēli: ').upper()
    menu(izveles_menu)