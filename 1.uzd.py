#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā)

with open('janvaris.txt', 'r', encoding='utf-8') as ii:
    teksts=ii.read()
    print(teksts)
