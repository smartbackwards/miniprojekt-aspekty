# Opinia prawna — Legalność parsowania demo plików CS2 z HLTV.org

*Dokument ma charakter edukacyjny i nie stanowi porady prawnej.*  
*Sporządzono: Kwiecień 2025*

---

## 1. Stan faktyczny

Działalność osobista zakłada **ręczne** pobieranie i parsowanie plików `.dem`
(GOTV demo) z profesjonalnych meczów CS2. Pliki są pobierane wyłącznie przez
przeglądarkę (kliknięcie linku, pobranie pliku) — bez żadnego automatycznego
skryptu, crawlera ani scrapera. Jedynym źródłem danych jest serwis HLTV.org.

Cele przetwarzania:
- **Praca magisterska** — analiza danych meczowych CS2, uczenie maszynowe (użytek niekomercyjny, akademicki)
- **Posty na platformie X (Twitter)** — tworzenie statystyk i wizualizacji do publikacji

---

## 2. Analiza techniczna dostępu i rola robots.txt

| Aspekt | Wynik | Znaczenie prawne |
|---|---|---|
| HTTP status `/terms` | 403 Forbidden | Blokada Cloudflare = techniczne egzekwowanie ToS wobec botów |
| HTTP status `robots.txt` | 403 Forbidden | Ironicznie — robots.txt blokowany przez anty-botowy system |
| Obecność robots.txt | Potwierdzona (plik dostarczony) | Zawiera `Disallow: /download/demo*` |
| Infrastruktura | Cloudflare WAF + Bot Management | Aktywna ochrona przed automatycznym ruchem |

### Kluczowe rozróżnienie: robots.txt a ręczne pobieranie

`robots.txt` to konwencja skierowana **wyłącznie do zautomatyzowanych botów
i crawlerów** (standard RFC 9309). Nie ma charakteru prawnie wiążącego dla
użytkowników-ludzi. Dyrektywa `Disallow: /download/demo*` oznacza, że
robot/crawler nie powinien odwiedzać tych ścieżek automatycznie — **nie
zakazuje ręcznego kliknięcia i pobrania pliku przez użytkownika w przeglądarce**.

**Wniosek techniczny:** Sama obecność `Disallow: /download/demo*` nie przesądza
o nielegalności ręcznego pobierania. Decydują regulamin (ToS) i prawo.

---

## 3. Analiza regulaminów

### HLTV.org Terms of Service (§2.2)

Regulamin **wprost zakazuje**:
- data mining
- web scraping
- komercyjnego wykorzystania treści
- budowania konkurencyjnych usług

**Interpretacja w kontekście ręcznego pobierania:**  
Terminy "data mining" i "web scraping" w rozumieniu branżowym i prawnym odnoszą
się do **zautomatyzowanych procesów** masowego zbierania danych. Ręczne
pobieranie pojedynczego pliku `.dem` przez przeglądarkę nie spełnia tej definicji
i nie stanowi naruszenia §2.2.

Potencjalnie problemowy jest zakaz "commercially exploit the Website or any of
its content" — posty na Twitterze monetyzowane reklamami lub subskrypcjami
mogłyby podpadać pod tę klauzulę. Posty niekomercyjne (brak monetyzacji) lub
akademickie są bezpieczniejsze.

**Podstawa prawna regulaminu:** Prawo duńskie (HLTV.org A/S, CVR 27652913,
Kopenhaga). W relacjach B2C na terenie UE zastosowanie mają też przepisy
konsumenckie UE.

**Skutek akceptacji ToS:** Każdy użytkownik odwiedzający stronę akceptuje
warunki. Naruszenie ToS = naruszenie umowy.

### Valve Steam Subscriber Agreement

Zezwala na **niekomercyjne, osobiste** używanie gry i jej zasobów.
Demo pliki wygenerowane lokalnie przez CS2 mogą być parsowane na własny użytek.
Demo pobrane z HLTV podlegają regulaminowi HLTV, nie Valve.

---

## 4. Prawo Unii Europejskiej

### 4.1 Dyrektywa 96/9/EC — Sui Generis Database Right

HLTV.org inwestował przez ponad 10 lat w gromadzenie, weryfikację i indeksowanie
plików demo. Spełnia kryteria "istotnych nakładów" z art. 7 Dyrektywy.

**Zakres ochrony:** Wyodrębnienie lub wtórne użycie **istotnej części** bazy
(ilościowo lub jakościowo) bez zgody producenta jest zakazane.

**Ważne:** Prawo sui generis jest **niezależne od ToS** — obowiązuje z mocy
prawa unijnego nawet jeśli użytkownik nie zaakceptował regulaminu.

### 4.2 RODO — Przetwarzanie SteamID64

SteamID64 to pseudonimowy identyfikator jednoznacznie powiązany z kontem Steam
(= osobą fizyczną). Zgodnie z TSUE (C-582/14, *Breyer*):

> Pseudonimowe identyfikatory są danymi osobowymi jeżeli identyfikacja jest
> możliwa przy rozsądnym wysiłku po stronie administratora lub osoby trzeciej.

W przypadku SteamID64: profil Steam jest publiczny, identyfikacja jest trywialna.

**Skutek:** Przetwarzanie SteamID w plikach `.dem` wymaga podstawy prawnej
z art. 6 RODO. Dla projektu badawczego:
- art. 6(1)(f) — uzasadniony interes administratora (wymaga testu równowagi)
- art. 6(1)(a) — zgoda (nierealistyczna przy danych historycznych)

---

## 5. Precedensy orzecznicze

| Sprawa | Orzeczenie | Zastosowanie |
|---|---|---|
| TSUE C-30/14, *Ryanair v. PR Aviation* (2015) | ToS może zakazywać działań dopuszczonych przez prawo baz danych | Wzmacnia zakaz z ToS HLTV |
| TSUE C-582/14, *Breyer v. Bundesrepublik* (2016) | Pseudonimowe ID = dane osobowe | SteamID podlega RODO |
| 9th Cir., *hiQ v. LinkedIn* (2022) | Scraping publicznych danych może być dozwolony (CFAA, USA) | **Nie stosuje się w UE** |
| BGH, *Automobil-Datenbank* (2014, DE) | Systematyczne pobieranie narusza prawo baz danych | Analogia do masowego pobierania demo |

---

## 6. Rekomendacje

### Dozwolone (bez ryzyka prawnego)
- **Ręczne pobieranie** pojedynczych demo z HLTV.org przez przeglądarkę do celów akademickich
- Parsowanie pobranych demo na własny użytek (praca magisterska)
- Parsowanie **lokalnych demo** z własnych meczów CS2
- Tworzenie niekomercyjnych postów na Twitterze na podstawie własnoręcznie obliczonych statystyk

### Ryzykowne (wymagające analizy)
- Publikowanie postów na Twitterze, jeśli konto jest **monetyzowane** (reklamy, subskrypcje) — §2.2 "commercially exploit"
- Przetwarzanie SteamID bez pseudonimizacji — wymaga podstawy z art. 6 RODO
- Masowe ręczne pobieranie bardzo dużej liczby demo w krótkim czasie (może naruszać prawo sui generis Dyrektywy 96/9/EC)
- Automatyzowanie pobierania w jakiejkolwiek formie — naruszenie §2.2

### Zakazane
- Automatyczne pobieranie (scraping) demo z HLTV.org
- Budowanie systemu automatycznie indeksującego demo z HLTV
- Komercyjne wykorzystanie danych z HLTV bez umowy licencyjnej

### Działania mitygujące
1. Pseudonimizuj SteamID przed przechowywaniem w bazie projektu (hash + salt)
2. Jeśli Twitter jest monetyzowany, rozważ kontakt z HLTV o zgodę lub zmień źródło na Faceit API
3. Dla pracy magisterskiej: odnotuj w metodologii że dane pobrano ręcznie i wyłącznie do celów badawczych
4. Zachowaj umiar w liczbie pobieranych plików — nie symuluj masowego pobierania

---

*Niniejszy dokument ma charakter edukacyjny. W przypadku wątpliwości prawnych
należy skonsultować się z prawnikiem specjalizującym się w prawie IT/IP.*
