#Izveidot Python programmu, kur  lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), 
#un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.  Nolasītā informācija ir jāizdrukā terminālī.
#Ievērot iespejamās kļūdas!

nosaukums=input("Ievadi faila nosaukumu: ")
paplasinajums=input("Ievadi faila paplašīnājumu: ")

try: 
    with open(nosaukums + '.' + paplasinajums,'r', encoding='utf-8') as ii:
        fails=ii.read()
        print(fails)

except FileNotFoundError:
    print("Fails nav atrasts!")
except StopIteration: 
    print("Fails ir tukšs!")
