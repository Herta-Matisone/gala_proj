# gala_proj
Noslēguma projekts ir jūsu iespēja izmantot jauniegūtās prasmes, lai izstrādātu pilnvērtīgo programmatūru noteikto uzdevuma risināšanai. Projektā jāizmanto zināšanas, kas ir iegūtas kursa laikā, bet projekta uzdevumu jāģenerē jums pašiem. Mēs gribam, lai Jūs izveidotu sistēmu, kas automatizēs kādu no jūsu ikdienas uzdevumiem.  

Tā kā programmatūras izstrāde reti kad ir vienas personas darbs, jums tiek dota iespēja sadarboties ar vienu vai diviem kursabiedriem šī gala projekta izstrādes laikā. Protams, tiek sagaidīts, ka katrs students jebkurā šādā grupā vienlīdzīgi piedalās grupas projekta izstrādē. Turklāt tiek sagaidīts, ka divu vai trīs personu grupas projekta apjoms attiecīgi būs divreiz vai trīsreiz lielāks nekā vienas personas projekts. 

---

## Uzdevums
Izveidot programmu, kas nolasa informācij no rīgas satiksmes maršruta mājas lapas, dodot iespēju lietotājam izvēlēties vienu no 3 iestatītajiem maršrutiem, laiku un trasnporta veidu. Programma pasniedz iegūto informāciju lietotājam lasāmā un saprotamā veidā. 

## Uzdevuma aktualitāte
Uzdevuma programma veidota ikdienišķo maršrutu meklēšanas sistematizēšanai. Padarot neskaitāmu ikdienišķu maršrutu meklēšanu internetā par īsu informācijas ievadi vienā programmas logā ar glīti izklātu informāciju. 

## Bibliotēkas
### playwright.sync_api 
(no playwright)
Playwright ir automatizācijas bibliotēka, ko izmanto, lai kontrolētu pārlūkprogrammas. Tā ļauj uzprogrammēt lietotāja darbību simulāciju.
Specifiskā bibliotēka izmantot, jo ir nepieciešam ielādēt un piekļūt JavaScript failiem un datiem. 

## Funkcijas
### def iegut_marsrutu(adrese, transp)
Galvenā funkcija, kas apmeklē norādīto Rīgas satiksmes maršruta plānotāja lapu, gaida datu ielādi, un izvelk informāciju par pieturām un transporta veidiem pēc tam formatējot.

Parametri:  
adrese – saite uz maršruta lapu ar laika parametru.  
transp – norāda, kāds transporta veids jārāda (viss, tikai autobusi, vai tikai tramvaji/trolejbusi).  

### sync_playwright()
Nodrošina automātisku pārlūka startēšanu un aizvēršanu.  
Nodrošina resursu tīrību un pareizu sesijas pārvaldību, bez nepieciešamības manuāli aizvērt pārlūku.  

### page.goto(...), page.wait_for_load_state(...)
goto – ielādē norādīto URL.  
wait_for_load_state("networkidle") – gaida, līdz lapa pārtrauc tīkla aktivitāti (t.i., viss ir ielādēts).  
Rīgas Satiksmes lapa izmanto JavaScript dinamisku ielādi – šīs metodes nodrošina, ka visa informācija ir ielādēta pirms datu nolasīšanas.  

###  Elementu meklēšana (locator, inner_text, count, nth)
page.locator("#planner_header")  
page.locator(".ib") – meklē pieturas  
braucamie.nth(i).inner_text() – iegūst konkrēta elementa tekstu  
Izmanto CSS selektorus, lai atlasītu specifiskus HTML elementus un nolasītu datus.  

### Transporta tipu filtrēšana pēc klasēm
evaluate("e => e.className"): Iegūst HTML elementa klases, lai noteiktu, kāda tipa transports tas ir (bus, trol, tram).  
Izmanto noteiktu transporta veidu, ir jāizlasa CSS klase, jo saturs vizuāli var būt vienāds.

---
Herta Matisone 241RDB177  
Laura Ruta Rengarte 241RDB130






