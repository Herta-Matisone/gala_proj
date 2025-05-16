
# lietotāja izvelne lietotājam
user = int(input("Kurš lietotājs (1 vai 2): "))
if user == 1:
    # lietotāja izvelne meršrutam
    rout = int(input("Kurš maršruts (1, 2 vai 3): "))
    if rout == 1:   
        adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/7984/0611,0642"
    elif rout == 2: 
        adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/0611,0642/0079"
    elif rout == 3: 
        adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/0079/2120"
    else:
        print("Nav tāds maršruts")  
elif user == 2:
    # lietotāja izvelne meršrutam
    rout = int(input("Kurš maršruts (1, 2 vai 3): "))
    # tavi linki pie adresse
    if rout == 1:   
        adrese = "bla bla link"
    elif rout == 2: 
        adrese = "bla bla link"
    elif rout == 3: 
        adrese = "bla bla link"
    else:
        print("Nav tāds maršruts")  
else:
    print("Nav tāds lietotājs")




#viss gan jau jāieliek funkcijā un jaizmanto main bet to var vēlāk, jeb es to izdarīšu rīt (gan jau)







# tālakas izvelnes var veidot kad ir pieejami dati jo nezi kā izkatīsies tie
# šie vairāk ir uz kuru printēt unkuru info neprintēt userim

transp = int(input("Kurš transports (1 - viss,  2 - tikai A, 3 - tikai T ): "))
#if tranport == 2 tad print only A, if transport == 3 tad print only T, if == 1 print all  
parsiet = int(input("Vai ar pārsēšanos ar? (1 - Jā, 2 - Nē): "))
# domāju if parsiet == 2 tad, if transport > 1 tad don't print
# ja parsiet == 1 tad neko nedarīt un visu printēt 








# tālāk tu izmanto "adrese" kā savu linka apzīmējumu jeb kurā adījumā un iegūsti vērtības
# es tālāk paturpināšu un uzlabošu gana drīz ar :)


# jāpaskatās būs kā var uztaisīt lai var user mēģināt vēlreiz, bet tas tā
