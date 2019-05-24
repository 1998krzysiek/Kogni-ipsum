import random
luzacki_kognitywista = ["Sprawdź to emipirycznie. ", "Amfetamina jest nieszkodliwa. ", "Jak kogni to tylko na UAM-ie. ", "Praca po kogni? Ja umiem wszystko. ", "Lubię palić marihuanę w nowych wcześniej nie znanych mi miejscach. ", "Meto to porażka. ", "Jasion to przemiła kobieta. ", "Idziesz na wykład do Grega? ", "Uczyłeś się na Algo? Bo ja będę ściągał chyba. ", "Niedługo będę was hackował. ", "Żałuję że nie było mnie na SSAK-U. ", "Zastanawiam się nad doktoratem z kogni. ", "Mariusz Urbański to klasa. ", "Nie zdałem meto. ", "Zdałem meto, mogę już umierać. ", "Toyota produkuje najlepsze samochody. ", "Pierwszy semestr na kogni jest sztosem. ", "Nie ulegał fałszywym heurystykom. ", "Tekst Loftus mnie rozwalił. ", "Opuścić zajęcia z Rasiem, to przypał. ", "Znam wszystkie rodzaje wnioskowań więc nie mów, że moje rozumowanie jest błędne. ", "Czy moglibyście wypełnić dla mnie ankietkę? ", "Nie mam czasu, uczę się na Meto. ", "Nie ogarniam SPSS-A. ", "Przeczytałeś teorię podwójnego kodowania Paivo. ", "Wolisz wcześniejszego czy późniejszego Wittgensteina. ", "Nie wyspałem się, ale mam dzisiaj wykład z Filo, więc sobie, to odbiję. ", "W 15 minut na Międzychodzką? Najwyżej się spóźnię. ", "Ty chodzisz na Algo czy na BPZ? ", "Dawaj do Zenona na piłeczkę, nie sprawdza nieobecności. ", "Co za farmazon mówił, że Zenon nie sprawdza nieobecności na w-fie? ", "Angielski z Kasprem, a komu to potrzebne. ", "Najwyżej wezmę warunek z PP? ", "A ten esej z Epi to na kiedy mamy zrobić? ", "O czym pisałeś esej z Epi? ", "Jakie jest twoje stanowisko w sporze o uniwersalia? ", "Pomożesz mi z MPK, bo nie ogarniam. ", "Ogarnę meto w jeden dzień. ", "Greg co gada. ", "Podobno warto iść na programowanie do Jukiego. ", "Podeślę Ci fajny filmik z Ted-a. ", "Język niemiecki? A komu to potrzebne. ", "Naming and grapsing common objects, to najlepszy artykuł jaki czytałem. ", "Ogarniamy w końcu tą prezentację na WDK? Jutro mamy deadline. ", "Tylko konceptualizm! ", "Tylko nominazim! ", "Lubię czytać Hume'a. ", "Robimy kogni obóz na Woodstock'u. ", "Czemu ja zapisałem się na w-f o ósmej to nie wiem. ", "Dlaczego ja zapisałem się na w-f na Morasko... ", "Dane neurofizjologiczne oraz neuropsychologiczne wspierają tezę, że w korze mózgowej naczelnych znajdują się dwa pasma projekcji wzrokowych: brzuszny strumień 'percepcyjny' oraz grzbietowy strumień 'działania'.",
"Najbardziej przekonującym dowodem na rzecz trafności hipotezy wyróżniającej dwa 'mózgi wzrokowe' jest pacjentka DF, która pomimo głębokich zaburzeń percepcji wzrokowej kształtu przedmiotów, potrafi wykorzystywać informację o kształcie w trakcie kontroli chwytu przedmiotów.",
"Iluzje zwodzą oko, a nie rękę.", "Dowodem przemawiającym za istnieniem dwóch strumieni brzusznych była pacjentka DF, która cierpiała na agnozję wzrokową.",
"Afordancje to sposobności oddziaływania na obiekty środowiska, związane z ich charakterystykami oraz zdolnościami percepcyjnymi, doświadczeniem i ogólnymi ujmiejętnościami danej jednostki.",
"Pomysłodawcą teorii afrodancji był Gibson.", "Słyszałeś o ślepowidzeniu?",
"Francis Bacon pragnął stworzyć z wiedzy narzędzie do realizowania praktycznych celów.",
"Zmysły ludzkie są z natury łatwe do pomylenia.", "Ludzie próbują doapsować elementy do znanych wzorców.",
"Wybrałeś już po której stronie stoisz w sporze o uniwersalia?",
"Według Platona, kondcja człowieka przypomina stan ludzi przebywających w jaskini.",
"Platon podzielił świat na dwie warstwy - realną i idealną.", "Każda idea ma swój odpowiednik realny.",
"Cienie idei, które dostrzegamy, to świat zjawisk." "Kwantyfikatory umożliwiają zapisanie zdań w krótszej formie.",
"W matematyce zdanie jest rozumiane jako wyrażenie, o którym można powiedzieć, że jest prawdziwe lub fałszywe.",
"Związek naszych świadomych wrażeń z tym, co dochodzi do kory wzrokowej z oka, jest strasznie mały.",
"Solipsyzm jest poglądem głoszącym, że istnieje tylko jednostkowy podmiot poznający, cała zaś rzeczywistość jest jedynie zbiorem jego subiektywnych wrażeń.",
"Jako podstawowe właściwości percepcji wymienia się recepcję sensoryczną i percepcję umysłową.",
"Kiedy opisujemy czyjeś spostrzeżenia, zakładamy równocześnie, że dana osoba nabywa przekonanie dotyczące tego, co jest akurat postrzegane.",
"Celem kognitywistyki jest całościowe spojrzenie na zagadnienie umysłu, tzn. zagadnienia poznania w ogóle (możliwości poznawcze, procesy empiryczne, strukturę myślenia), powstawania umysłu i funkcjonowania jego.",
"Niektóre informacje, które w danym momencie są poza naszą świadomością, mogą jednak być dostępne świadomości lub przynajmniej procesom poznawczym.",
"W habituacji, w miarę jak przyzwyczajamy się do danego bodźca, zaczynamy stopniowo coraz mniej zwracać na niego uwagę.",
"Cztery główne funkcje uwagi to: uwaga selektywna, czujność i detekcja sygnału, poszukiwanie oraz uwaga podzielna.",
"Miarą tendencji centralnej dla zmiennych nominalnych jest dominanta.",
"Mirą rozproszenia dla zmiennych porządkowych są kwartyle, odchylenia ćwiartkowe i pozycyjny współczynnik zmienności.",
"Opis statystyczny nie polega na przepisywaniu właściwych wartości z raportów SPSS.",
"Badanie zostało przeprowadzone według planu Solomona.", "Szukam chętnych do badań! Wyślesz linka?",
"Aktywizacja pewnych schematów, idei, może mieć znaczący wpływ na zmianę naszego zachowania w sposób widoczny, a jednocześnie zupełnie przez nas nieuświadamiany.",
"Listy w języku Python to uporządkowane zbiory dowolnych obiektów, włączając w to inne listy.",
"Python posiada szereg wbudowanych metod do obsługi tekstu. m.in. string.",
"Człowiek zamknięty w Chińskim Pokoju jest odizolowany od świata zewnętrznego – trzeba więc mu umoŜliwić kontakt z otoczeniem, by mógł rozumieć i mieć inne stany umysłowe.",
"Logika to nauka o języku jako systemie znaków słownych.",
"Każde zdanie jest albo prawdziwe albo fałszywe.",
"Już Arystoteles...", "LEMAAAAT", "Istnieje również immaterialna odmiana idealizmu obiektywnego, ale ma ona charakter immanentny; jej autorem jest G. Berkeley.",
"Przedmioty materialne są dane za pośrednictwem ich reprezentacji (wrażeń) w umyśle, stąd nie możemy mówić o poznaniu źródłowym czy poznaniu wprost.",
"Czy spostrzegamy świat takim, jakim jest naprawdę, czy też, to jak go widzimy zależy od subiektywistycznej specyfiki naszych systemów zmysłowych i konstruktów umysłowych?",
"Problem umysł-ciało jest obecnie uważany za kluczowy w filozofii umysłu.", "W eksperymencie Stroopa osoby badane mają określić kolor atramentu, którym napisano słowo i powstrzymać się przed przeczytaniem samego słowa.",
"Następnie badani decydowali, czy litera kontrolna była w prezentowanym zbiorze pokazana.", "Percepcja odpowiada za odbieranie informacji z otoczenia.",
"Z badania wynika, że przeszukiwanie wzrokowe różni się od innych zachowań wizualnych.", "Czy zdałeś już meto?", "Pobrałeś już SPSSa?", "Zaliczenie z filozofii jest ustne??!",
"A Pani jak sądzi?", "Odczuwam niepokój filozoficzny."]
#### pobiera określoną ilość zdań z listy

def losowanie_cytatu(lista_kogni,wybor):
    for i in range(wybor):
        cytat=random.choice(lista_kogni)
        lista_kogni.remove(cytat)
        print(cytat,end="")


### Tutaj będzie losowało akapity
def ilosc_akapitow(lista_kogni, wybor):
    for j in range(wybor+1):
        if j==1:
            None
        else:
            print('\n')

        for i in range(0, random.randint(3,15)):
            cytat=random.choice(lista_kogni)
            lista_kogni.remove(cytat)
            print(cytat,end="")


