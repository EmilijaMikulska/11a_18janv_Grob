fails = 'janvaris.txt' 

# tresas rindas saturs
with open(fails, 'r') as file:
    saturs = file.readlines()
    if len(saturs) >= 3:
        print(f"Trešā rinda: {saturs[2]}")
    else:
        print("Failā ir mazāk par 3 rindām.")