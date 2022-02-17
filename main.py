from datetime import datetime
from datetime import date #importē laikus un datumus
import datetime
import sys #vairāk konsoles iespējas

diena = date.today() #šodienas datums
sodiena = diena.strftime("%d/%m/%Y") #šodienas datums pārveidots
class menu: #tiek definēts izvēļu logs
    def __init__(pasa, izvele): #definētas izvēles
        pasa.izvele = izvele #pārveidots par mainīgo
        if izvele == "A": #apskatīt pieteikumus
            skaits = 0 #rezervāciju skaits
            file = open("rezervacijas.txt") #atver failu ar rezervācijām
            rindas = file.readlines()[1:] #tiek apskatītas visas rindas failā
            file.close()
            for line in rindas:
                skaits += 1 #rezervāciju skaitam tiek pievienots faila rindu skaits

            if skaits == 0:
                print("Nav rezervāciju!") #ja failā nav nekā, sistēma to pasaka
                print()
            else:
                file = open("rezervacijas.txt", "r")
                print(file.read()) #fails tiek atvērs, un tiek parādīti pieteikumi konsolē
                file.close()

        elif izvele == "B": #pieteikt jaunu pieteikumu
            with open("rezervacijas.txt", "r") as file: #tiek atvērts fails lasīšanai
                for ped_rinda in file:
                    pass

            if ped_rinda[0] == "#":
                num = 1 #indeksi pieteikumiem
            else:
                num = int(ped_rinda[0]) + 1

            vards = input("Ievadi savu vārdu un uzvārdu: ") #klienta vārds, uzvārds
          
            datums = input("Ievadi datumu(dd/mm/yyyy): ") #diena, uz kuru piesakās
            pagatne = datetime.datetime.strptime(datums, "%d/%m/%Y") #laiks pirms šodienas
            paslaik = datetime.datetime.now() #pašreizējais laiks
            pagatne.date() < paslaik.date()
            if pagatne.date() < paslaik.date(): #ja klients cenšas pieteikties uz laiku pagātnē, sistēma apstājas
              sys.exit("Šāds laiks nav pieejams!")
          
            laiks = input("Ievadi vēlamo laiku: ") #laika ievade
            sakums="08:00" #serviss atveras
            beigas="16:45" #serviss vairs nepieņem pakalpojumus
            laiks = datetime.datetime.strptime(laiks, '%H:%M').time()
            beigas = datetime.datetime.strptime(beigas, '%H:%M').time() #pārveido visus 3 laikus salīdzināšanai
            sakums = datetime.datetime.strptime(sakums, '%H:%M').time()
            if laiks<sakums or laiks>beigas: #ja ievadītais laiks neatbilst, sistēma apstājas
              sys.exit("Serviss šajā laikā nav atvērts!")
            laicins=[laiks,datums]

            problema = input("Īsi apraksti savu problēmu: ") #klienta problēmas apraksts
            marka = input("Ievadi savu auto marku: ") #klienta auto marka
            telefons = int(input("Ievadi savu telefona numuru:")) #klienta telefona numurs
            
            tabula='rezervacijas.txt' #tabulas saturs tiek ievietots string
            with open(tabula) as f_obj: #atverts fails
              teksts=f_obj.read()  #tiek pārbaudīts, vai klienta vārds jau ir sistēmā
            if vards in teksts: #ja jā, pieteikums atcelts
              sys.exit("Uz Jūsu vārda pastāv pieteikums! Apmeklējiet vai izdzēsiet to.")
              
            pieteikums=''.join(str(laicins)) 
            laiki='laiki.txt'
            with open(laiki) as f_obj:
              laikidiv=f_obj.read() #pārbauda, vai jau ir aizņemts
            if pieteikums in laikidiv:
              sys.exit("Atvainojiet, šis laiks jau ir aizņemts.")
             
            file = open("laiki.txt","a+")
            file.write(f"{pieteikums}\n") #ievadīts pieteikuma laiks citā failā
            file.close()
          
            file = open("rezervacijas.txt","a") #viss ievadītais tiek ievadīts tabulā
            file.write(f"{num}\t\t\t\t{vards}\t\t\t\t{datums}\t\t\t\t{laiks}\t\t\t\t{problema}\t\t\t\t{marka}\t\t\t\t{telefons}\n") #tabula
            file.close() #tabula tiek aizvērta
            print()


        elif izvele == "C": #pieteikuma izdzēšana
            resnum = input("Ievadi pieteikuma numuru: ") #tiek ievadīts pieteikuma indekss
            file1 = open("rezervacijas.txt", "r") #fails atvērts lasīšanai
            rindas = file1.readlines() #apskatītas faila rindiņas
            file1.close() #fails aizvērts
            file2 = open("rezervacijas.txt", "w" ) #fails atvērts rakstīšanai

            for line in rindas:
                if not line.startswith(resnum):
                    file2.write(line) 
            file2.close()

        elif izvele == "D": #ja izvēle d, sistēma apturēta
            sys.exit("Paldies Jums!")

        else: #ja ievada nezināmu burtu, sistēma liek ievadīt izvēli vēlreiz
            print("Nezināma izvēle. Lūdzu mēģiniet vēlreiz.")


while True:
    try: #programma loopā līdz lietotājs iziet
        file = open("rezervacijas.txt", "r")
    except FileNotFoundError: #ja faila nav, tas tiek izveidots
        file = open("rezervacijas.txt", "w+")
        file.write("#\t\t\tVārds\t\t\t       Datums\t\t\t        Laiks\t\t\t     Problēma\t\t\tMarka    \t\t\tTelefons\n")
    file.close()

    print(f"Autoservisa pieteikšānās sistēma, strādājam no 08:00 - 17:00, šodien ir {sodiena}")
    print("Mūsu telefons: +371 29 299 299")
    print("Sistēmas iespējas:")
    print("A. Apskatīt visus pieteikumus\tB. Pierakstīties pakalpojumam")
    print("C. Izdzēst pieteikumu\t\tD. Iziet")
  
    izveles_menu = input('Ievadi savu izvēli: ').upper() #input izvēlei, mazie burti pārveidoti par lieliem
    menu(izveles_menu)