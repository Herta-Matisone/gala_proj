from playwright.sync_api import sync_playwright

def iegut_marsrutu(adrese, transp):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Lādējam datus no: {adrese}")
        # laiks = "/12:00"

        page.goto(adrese)


        # adrese = adrese + laiks;
        # print(adrese)

        # Gaidām, kamēr DOM ir ielādēts
        page.wait_for_load_state("networkidle")

        try:
            page.wait_for_selector("#planner_header", timeout=10000)  # gaida līdz 10 sekundēm, lai parādās virsraksts
            virsraksts = page.locator("#planner_header").inner_text()
        except Exception as e:
            print("Virsraksts nav atrasts., viss slikti", str(e))

        # Mēģinām atrast pieturas
        try:
            # Iegūstam pieturas un transportus
            pieturas = page.locator(".ib") 
            #braucamie = None
            count = pieturas.count()
            '''
            pieturas = page.locator(".ib") 
            count = pieturas.count()
            if count == 0:
                print("Pieturas nav atrastas.")
            else:
                for i in range(count):
                    teksts1 = pieturas.nth(i).inner_text()
                    #print(teksts)
                    print(f"{i+1}. {teksts1}")
                    

                    #if "Vieta" in teksts:  # Filtrējam pēc teksta
                     #   print(f"{i+1}. {teksts}")
                     '''  
            # transporta nr un tā tips
            if transp == 1:
                braucamie = page.locator(".num.num1.trol, .num.num2.trol, .num.num1.bus, .num.num2.bus, .num.num1.tram, .num.num2.tram")
            elif transp == 2:
                braucamie = page.locator(".num.num1.bus, .num.num2.bus")
            elif transp == 3:
               braucamie = page.locator( ".num.num1.trol, .num.num2.trol, .num.num1.tram, .num.num2.tram")
            else:
                print("Nepareizs transporta tips.")
                return
            count_braucamie = braucamie.count()
            #pieturas = page.locator(".ib") 
            #count = pieturas.count()
            if count_braucamie == 0:
                print("braucamie nav atrasti.")
                print("Pieturas nav atrastas.")
            else:
                print(f"Atrasti {count_braucamie} braucamie:")
                pietura_indekss = 0
                for i in range(count_braucamie):
                    element = braucamie.nth(i)  
                    teksts = element.inner_text().strip()
                    #for j in range(3):  
                    #    pietura_index = i * 3 + j   
                    #    if pietura_index < count:                  
                    #        teksts1 = pieturas.nth(i).inner_text()

                    try:
                        klases = element.evaluate("e => e.className") 
                    except Exception as e:
                        print(f"Neizdevās nolasīt klasi: {e}")
                        klases = ""

                    # Determine transport type from class
                    if "bus" in klases:
                        tips = "A"   # Autobuss
                    elif "trol" in klases:
                        tips = "TRO"   # Trolejbus
                    elif "tram" in klases:
                        tips = "TRA"  # Tramvajs
                    else:
                        tips = "?"   # Nezināms tips
                    print(f"{i+1}. {tips} {teksts}")

                    #if teksts and teksts1:
                    #    for i in range(i<10):
                    #        print(f"{i+1}. {tips} {teksts}")
                            
                            #for j in range(3):
                            #    x = 0
                            #    for x in range(x<3):
                            #        pietura_index = x+1
                            #        if pietura_index < count:
                            #            print(f"{teksts1}")
                    # Cik pieturas drukāt šim braucienam: pārmaiņus 4 un 3
                    pieturu_skaits = 4 if i in [0] else 3
                    for j in range(pieturu_skaits):
                        pietura_index = i * 3 + j 
                        if pietura_index < count:
                            pietura_teksts = pieturas.nth(pietura_index).inner_text().strip()
                            print(f"   {pietura_teksts}")
                            
                    print()  # tukša rinda starp braucieniem

        except Exception as e:
            print("Pieturas nav atrastas.", str(e))
        
        #if teksts1:
        #    transporta_numeris = braucamie.nth(i).inner_text().strip()
    #for i in range(i<10):
    #    print(f"{tips} - {teksts} - {teksts1}  ")
    #print(f"Pietura {i+1}: {teksts1} | Transporta numurs: {transporta_numeris} ")
# lietotāja izvelne lietotājam
def galvenais():
    user = int(input("Kurš lietotājs (1 vai 2): "))
    adrese = ""
    if user == 1:
        # lietotāja izvelne meršrutam
        print("")
        print("Maršruti")
        print("1 - Elizabetes iela   :   Ķīpsala")
        print("2 - Ķīpsala           :   Centrālā stacija")
        print("3 - Centrālā satcija  :   Medicīnas muzejs")
        print("")
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
        print("")
        print("Maršruti")
        print("1 - Kīpsala   :   Imanta")
        print("2 - Kīpsala   :   Piņķi")
        print("3 - Kīpsala   :   Mārupe")
        print("")
        rout = int(input("Kurš maršruts (1, 2 vai 3): "))
        if rout == 1:   
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/0611,0642/3031,3054 "
        elif rout == 2: 
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/0611,0642/4977,8073"
        elif rout == 3: 
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/0611,0642/1392,1395"
        else:
            print("Nav tāds maršruts")  
    else:
        print("Nav tāds lietotājs")
        return
    laiks = str(input("kādā laikā?(formātā - 13:00): "))
    adrese = adrese + "/" + laiks
    transp = int(input("Kurš transports (1 - viss,  2 - tikai Autobusu, 3 - tikai Tramvaju/Trole): "))

    iegut_marsrutu(adrese, transp)

if __name__ == "__main__":
    galvenais()