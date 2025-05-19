
# 1. variants. Šis man nestrādā, jo dati ir javascript(mēģināšu citu variantu).
# import requests
# from bs4 import BeautifulSoup

# def iegut_marsrutu(adrese):
#     lapa = requests.get(adrese)
#     if lapa.status_code !=200:
#         print(f"Kķūda ielādējot lapu! Statusa kods: {lapa.status_code}")
#         return
    
#     lapas_saturs = BeautifulSoup(lapa.content, "html.parser")

#     virsraksts = lapas_saturs.find("h1")
#     if virsraksts:
#         print("Maršruta virsraksts:", virsraksts.get_text(strip=True))
#     else:
#         print("Virsraksts nav atrasts.")

#     saraksti = lapas_saturs.find_all("div", class_="stop")
#     if not saraksti:
#         print("Neatradām pieturas vai sarakstus šajā lapā.")
#     else:
#         print(f"Atrasts {len(saraksti)} pieturas:")
#         for i, pietura in enumerate(saraksti, 1):
#             print(f"{i}. {pietura.get_text(strip=True)}")

# 2.variants
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
            print("Maršruta virsraksts:", virsraksts)
        except Exception as e:
            print("Virsraksts nav atrasts.", str(e))

        # Mēģinām atrast pieturas
        try:
            pieturas = page.locator(".ib") 
            count = pieturas.count()
            if count == 0:
                print("Pieturas nav atrastas.")
            else:
                for i in range(count):
                    teksts = pieturas.nth(i).inner_text()
                    print(teksts)
                    if "Vieta" in teksts:  # Filtrējam pēc teksta
                        print(f"{i+1}. {teksts}")

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
            if count_braucamie == 0:
                print("braucamie nav atrasti.")
            else:
                print(f"Atrastas {count_braucamie} braucamie:")
                for i in range(count_braucamie):
                    element = braucamie.nth(i)  
                    teksts = element.inner_text().strip()

                    try:
                        klases = element.evaluate("e => e.className") 
                    except Exception as e:
                        print(f"Neizdevās nolasīt klasi: {e}")
                        klases = ""

                    # Determine transport type from class
                    if "bus" in klases:
                        tips = "A"   # Autobuss
                    elif "trol" in klases:
                        tips = "T"   # Trolejbus
                    elif "tram" in klases:
                        tips = "TR"  # Tramvajs
                    else:
                        tips = "?"   # Nezināms tips

                    if teksts:
                        print(f"{i+1}. {teksts}{tips}")
        except Exception as e:
            print("Pieturas nav atrastas.", str(e))
        
'''
        try:
            laiks_un_vieta = laiks_un_vieta.text_content().strip()
            print("Maršruta laiks un vieta:", laiks_un_vieta)
        except Exception as e:
            print("Laiks un vieta nav atrasts.", str(e))

        # Mēģinām iegūt pieturas
        page.wait_for_selector(".num num2 trol", ".num num2 bus", timeout=10000)
        pieturas = page.locator(".stop")

        count = pieturas.count()
        if page.locator(".stop").count() == 0:
            print("Pieturas nav atrastas (nav ielādētas vai mainīts selektors).")
        else:
            pieturas = page.locator(".stop").element_handles()
            redzamas = [e.text_content().strip() for e in pieturas if e.is_visible()]
            print(f"Atrastas {len(redzamas)} redzamās pieturas:")
            for i, p in enumerate(redzamas, 1):
                print(f"{i}. {p}")

        browser.close()
'''
# lietotāja izvelne lietotājam
def galvenais():
    user = int(input("Kurš lietotājs (1 vai 2): "))
    adrese = ""
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
        if rout == 1:   
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/56.95859;24.0845/56.97311;24.19454/2025-05-19 "
        elif rout == 2: 
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/56.95859;24.0845/4977,8073/2025-05-19"
        elif rout == 3: 
            adrese = "https://saraksti.rigassatiksme.lv/index.html#plan/56.95859;24.0845/3031,3054/2025-05-19"
        else:
            print("Nav tāds maršruts")  
    else:
        print("Nav tāds lietotājs")
        return
    laiks = str(input("kādā laikā?(formātā - 13:00): "))
    adrese = adrese + "/" + laiks
    transp = int(input("Kurš transports (1 - viss,  2 - tikai Autobusu, 3 - tikai Tramvaju/Trole): "))
    

    #if adrese:
    #    print(f"lādē datus")
    iegut_marsrutu(adrese, transp)
#print(f"Lādējas datus no: {adrese}")
#iegut_marsrutu(adrese)


if __name__ == "__main__":
    galvenais()


# jāpaskatās būs kā var uztaisīt lai var user mēģināt vēlreiz, bet tas tā