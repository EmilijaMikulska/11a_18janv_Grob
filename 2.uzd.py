#Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.

import csv

fails = '2.uzd.csv'
with open(fails, 'r') as csv_fails:
    csv_lasitajs = csv.reader(csv_fails) 
        
    for rinda in csv_lasitajs:
        # Pārbauda, vai rindā ir vismaz divas kolonnas
        if len(rinda) >= 2:
            otra_kolonna = rinda[1]
            print(f"Otrās kolonnas: {otra_kolonna}")
        else:
            print("Šijā rindā nav pietiekami kolonnu.")

