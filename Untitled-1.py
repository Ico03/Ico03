"""inserimento dati"""

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
else:
    km= int(input('inserire chilometraggio annuale:'))
    print("considernado una media di circa: \n", km/365, "km a settimana \t", km/12, "km al mese\t", km, "km all'anno")
    km= [round(km/365, 2), round(km/12, 2), km]         #creazione di un array con km settimanali, mensili e annuali
    
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

print("consumo :", cons, "\tcosto: ", cash, "\tcapienza serbatoio: ", serb) #output per verifia contenuto variabili
consumo_carburante_mensile= round((km[1])/cons[0], 2)
costo_carburante_mensile= round(consumo_carburante_mensile*cash)
print("consumo di carburante mensile: ", consumo_carburante_mensile)    #output per verifia contenuto variabili
print("costi carburante mensili: ", costo_carburante_mensile)   #output per verifia contenuto variabili

