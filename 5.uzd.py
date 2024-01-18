#Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. 
#Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). 
#Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. 
#Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.

vards=input("Ieraksti savu vārdu: ")
try:
    with open("lietotajs.txt",'w', encoding='utf-8') as aa:
        aa.write(vards)
    print("Vārds ir ierakstīts failā!")
except FileNotFoundError:
    print("Fails nav atrasts")

