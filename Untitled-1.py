"""inserimento dati"""
km= int(1)
cons= int(1)
cash= int(1)
serb= int(1)
#def chilometraggio(km): #funzione per ottenere i km 
    a= int(input('sei in grado di calcolare una media di km: \n1) settimanale \n2) mensile \n3) annuali\n'))
    while a<1 | a>3:
        a= int(input('valore inserito non valido  '))

    if a==1 :
        km= int(input('inserire chilometraggio settimanale:'))
        print("considernado una media di circa: \n", km, "km a settimana \t", km*30, "km al mese\t", km*365, "km all'anno")
        km= [km, km*30, km*365]         #creazione di un array con km settimanali, mensili e annuali
    elif a==2:
        km= int(input('inserire chilometraggio mensile:'))
        print("considernado una media di circa: \n", km/30, "km a settimana \t", km, "km al mese\t", km*12, "km all'anno")
        km= [round(km/30,2), km, round(km*12,2)]          #creazione di un array con km settimanali, mensili e annuali
    else :
        km= int(input('inserire chilometraggio annuale:'))
        print("considernado una media di circa: \n", km/365, "km a settimana \t", km/12, "km al mese\t", km, "km all'anno")
        km= [round(km/365, 2), round(km/12, 2), km]         #creazione di un array con km settimanali, mensili e annuali
    #return(km)

#def carburante(cons, cash, serb):
    a= int(input('consumi auto, preferisci calcolarli in: \n1)km/l \n2)l/100km\n'))
    while a<1 | a>2:
        a= int(input("valore inserito non valido (1 - 2)"))

    if a==1:
        cons= float(input('Iserire il consumo in km/l: '))
        cons= [cons, round(100/cons,2)] #round(var, 2) si ferma alla seconda cifra decimale
    else :
        cons= float(input('Iserire il consumo in l/100km: '))
        cons= [round(100/cons,2), cons] #round(var, 2) si ferma alla seconda cifra decimale

    print(cons)
    cash= float(input('Prezzo del carburante al litro: '))
    cash= round(cash,2) #round(var, 2) si ferma alla seconda cifra decimale

    serb= int(input('Dimensione del serbatoio della propria automobile: '))

    print("consumo :", cons, "\tcosto: ", cash, "\tcapienza serbatoio: ", serb)
    consumo_carburante_mensile=float(km=[1])/cons[0]
    print("consumo di carburante mensile: ", consumo_carburante_mensile)

    #return (cons, cash, serb)




carburante(cons, cash, serb)
chilometraggio(km)
#consumo_carburante_mensile=float(chilometraggio(km[1])/cons[0])