x=int(input("Zadejte cislo: "))
if x%4==0 and x%7==0:
    print("Cislo je delitelne styri a sedemimi")
elif x%4==0:
    print("Cislo je delitelne styri")
elif x%7==0:
    print("Cislo je delitelne sedemimi")
else:
    print("Cislo nie je delitelne ani styri ,ani sedemimi")