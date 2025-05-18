
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
        page.wait_for_load_state("domcontentloaded")

        try:
            page.wait_for_selector("h1", timeout=10000)  # gaida līdz 10 sekundēm, lai parādās virsraksts
            virsraksts = page.locator("h1").inner_text()
            print("Maršruta virsraksts:", virsraksts)
        except:
            print("Virsraksts nav atrasts.")

# Mēģinām atrast pieturas
        try:
            pieturas = page.locator("span, strong, td")
            count = pieturas.count()
            if count == 0:
                print("Pieturas nav atrastas.")
            else:
                print(f"Atrastas {count} pieturas:")
                for i in range(count):
                    teksts = pieturas.nth(i).inner_text()
                    if "Vieta" in teksts:  # Filtrējam pēc teksta
                        print(f"{i+1}. {teksts}")
        except:
            print("Pieturas nav atrastas.")

# Mēģinām atrast laiku un vietu
        try:
            laiks_un_vieta = page.locator("strong").inner_text()
            print("Maršruta laiks un vieta:", laiks_un_vieta)
        except:
            print("Laiks un vieta nav atrasts.")

        # Mēģinām iegūt pieturas
        page.wait_for_selector(".stop", timeout=10000)
        pieturas = page.locator(".stop")
        count = pieturas.count()
        if count == 0:
            print("Pieturas nav atrastas.")
        else:
            print(f"Atrastas {count} pieturas:")
            for i in range(count):
                print(f"{i+1}. {pieturas.nth(i).inner_text()}")

        browser.close()

# lietotāja izvelne lietotājam
def galvenais():
    user = int(input("Kurš lietotājs (1 vai 2): "))
    adrese = ""
    1
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

# Neizdevās līdz galam dabūt lai strādā, turpināšu rīt.