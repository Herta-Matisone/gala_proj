
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

def iegut_marsrutu(adrese):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Lādējam datus no: {adrese}")

        page.goto(adrese)

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
                print(f"Atrastas {count} pieturas:")
                for i in range(count):
                    teksts = pieturas.nth(i).inner_text()
                    print(teksts)
                    if "Vieta" in teksts:  # Filtrējam pēc teksta
                        print(f"{i+1}. {teksts}")
        except Exception as e:
            print("Pieturas nav atrastas.", str(e))

# Mēģinām atrast bus/trol num
        try:
            pieturass = page.locator(".num.num1.bus, .num.num2.bus, .num.num1.trol, .num.num2.trol") 
            count = pieturass.count()
            if count == 0:
                print("braucamie nav atrasti.")
            else:
                print(f"Atrastas {count} braucamie:")
                for i in range(count):
                    teksts = pieturass.nth(i).inner_text()
                    print(teksts)
                    if "Vieta" in teksts:  # Filtrējam pēc teksta
                        print(f"{i+1}. {teksts}")
        except Exception as e:
            print("braucamie nav atrasti.", str(e))
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
    

    #if adrese:
    #    print(f"lādē datus")
    iegut_marsrutu(adrese)
#print(f"Lādējas datus no: {adrese}")
#iegut_marsrutu(adrese)


if __name__ == "__main__":
    galvenais()






transp = int(input("Kurš transports (1 - viss,  2 - tikai A, 3 - tikai T ): "))
#if tranport == 2 tad print only A, if transport == 3 tad print only T, if == 1 print all  
parsiet = int(input("Vai ar pārsēšanos ar? (1 - Jā, 2 - Nē): "))
# domāju if parsiet == 2 tad, if transport > 1 tad don't print
# ja parsiet == 1 tad neko nedarīt un visu printēt 




# jāpaskatās būs kā var uztaisīt lai var user mēģināt vēlreiz, bet tas tā

# Neizdevās līdz galam dabūt lai strādā, turpināšu rīt.