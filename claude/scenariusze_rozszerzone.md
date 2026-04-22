# Analiza scenariuszy rozszerzonych — HLTV.org i dane CS2

**Uzupełnienie mini-projektu** — Aspekty prawne, społeczne i etyczne w sztucznej inteligencji
**Autor:** Bartosz Tramś  
**Data:** Kwiecień 2025  

*Dokument ma charakter edukacyjny i nie stanowi porady prawnej.*

---

## Cel dokumentu

Analiza czterech scenariuszy wykraczających poza bazowy przypadek użycia
(ręczne pobieranie demo do pracy magisterskiej), które generują dodatkowe
ryzyko prawne. Każdy scenariusz zawiera opis problemu, uzasadnienie prawne
i rekomendowane rozwiązanie.

Scenariusze:
- Monetyzacja postów na platformie X (Twitter)
- Pobieranie setek gigabajtów / tysięcy meczów
- Lokalna baza danych graczy (`players.json`) a RODO
- Własna strona ze statystykami CS2

---

## Scenariusz 1 — Monetyzacja postów na Twitterze

**Problem:** ToS HLTV §2.2 — *"commercially exploit the Website or any of its
content in any manner."*

**Uzasadnienie:** Słowo "any of its content" jest szerokie. Jeśli statystyki
tworzone na podstawie danych z plików `.dem` pobranych z HLTV generują przychód
(Twitter Ads Revenue, subskrypcje Twitter Blue, linki afiliacyjne), HLTV może
argumentować że treść jest wykorzystywana komercyjnie bez licencji.

Nie ma znaczenia, że dane zostały przetworzone — zakaz dotyczy treści
"any of its content", a dane statystyczne z meczów wciąż pochodzą z zasobów HLTV.

**Rekomendacja:**
- Skontaktuj się z HLTV mailowo z zapytaniem o zgodę na tworzenie komercyjnych treści opartych na ich danych — wiele firm esportowych udziela takiej zgody twórcom, zwłaszcza jeśli posty promują ich platformę
- Alternatywnie: FACEIT Data API ma jawne warunki dotyczące użytku komercyjnego przez aplikacje trzecie

---

## Scenariusz 2 — Setki gigabajtów i tysiące meczów

**Problem:** Ta skala pobierania zmienia kategorię prawną, nawet przy zachowaniu ręcznego charakteru pobierania.

**Uzasadnienie — Dyrektywa 96/9/EC, art. 7:**

Prawo sui generis zakazuje *"extraction or re-utilization of substantial parts"*
bazy danych. Pojęcie "substantial" jest rozumiane **ilościowo i jakościowo**.
Tysiące meczów stanowią ilościowo istotną część archiwum HLTV.

TSUE w sprawach *Fixtures Marketing* (C-46/02, 2004) wyjaśnił, że systematyczne
pobieranie nieistotnych części w celu zrekonstruowania całości jest też naruszeniem
— tzw. "spin-off protection" nie stanowi tarczy przed takim działaniem.

**Uzasadnienie — granica ręczne vs. automatyczne:**

Przy tysiącach plików ręczne pobieranie staje się de facto systematyczną ekstrakcją,
nawet jeśli technicznie każde kliknięcie jest ręczne. Sądy oceniają cel i efekt,
nie tylko metodę.

**Rekomendacja:**

Przy tej skali wymagana jest licencja lub formalna zgoda HLTV:
- Napisz do HLTV — opisz projekt (praca naukowa), zakres, lokalny i niekomercyjny charakter bazy
- Jeśli projekt jest akademicki, uczelnia może pomóc sformułować prośbę o zgodę badawczą
- Alternatywnie: `demo.faceit.com` oferuje dostęp do demo przez API z jasnymi warunkami licencyjnymi

---

## Scenariusz 3 — Lokalna baza danych graczy (`players.json`) a RODO

**Problem:** Plik łączący ID HLTV gracza z aliasem, krajem, imieniem i nazwiskiem
oraz SteamID to klasyczna baza danych osobowych w rozumieniu RODO.

**Uzasadnienie:**

RODO art. 4(1) definiuje dane osobowe jako *"wszelkie informacje dotyczące
zidentyfikowanej lub możliwej do zidentyfikowania osoby fizycznej."*

| Pole w `players.json` | Kwalifikacja RODO |
|---|---|
| Imię i nazwisko | **Dane osobowe wprost** |
| SteamID | **Dane osobowe** (TSUE *Breyer*, C-582/14) |
| Alias gracza | Dane osobowe — pseudonim powiązany z tożsamością |
| Kraj | Dane osobowe w połączeniu z pozostałymi |
| ID HLTV | Dane osobowe — identyfikator powiązany z osobą |

RODO stosuje się **niezależnie od tego, że baza jest lokalna** — art. 2 obejmuje
każde przetwarzanie danych osobowych, w tym przechowywanie na własnym dysku.
"Przetwarzanie" (art. 4(2)) to m.in. zbieranie, przechowywanie i organizowanie danych.

**Co musisz zapewnić:**

- **Podstawa prawna** (art. 6) — dla badań: art. 6(1)(f) uzasadniony interes lub art. 6(1)(a) zgoda (nierealistyczna przy danych historycznych zawodowców)
- **Minimalizacja danych** (art. 5(1)(c)) — jeśli do importu meczów wystarczy alias + SteamID, imię i nazwisko jest zbędne i nie powinno być przechowywane
- **Bezpieczeństwo** (art. 32) — szyfrowanie dysku lub kontrola dostępu do pliku
- **Określony cel** — "przyspieszenie importu meczów do prywatnej bazy badawczej" to akceptowalny cel przy niekomercyjnym użytku

**Wyłączenie "household exemption":**

Jako osoba prywatna przetwarzająca dane do celów czysto osobistych możesz korzystać
z wyłączenia art. 2(2)(c) RODO — ale **tylko dopóki dane nie są udostępniane publicznie**.
Stworzenie publicznej strony (Scenariusz 4) wyklucza to wyłączenie.

---

## Scenariusz 4 — Własna strona ze statystykami CS2

**Problem:** Scenariusz o największym ryzyku prawnym — łączy wszystkie poprzednie kwestie.

**Uzasadnienie — Dyrektywa 96/9/EC:**

Publiczne udostępnienie statystyk obliczonych z demo pobranych z HLTV to
*"re-utilization of substantial part"* ich bazy. Nawet przy przetworzeniu
danych do innej formy (statystyki zamiast surowych plików), TSUE w sprawie
*Football Dataco v. Yahoo!* (C-604/10, 2012) wskazał, że ochrona bazy dotyczy
nakładów na zebranie danych, nie ich twórczego opracowania. Strona korzystałaby
z nakładów HLTV niezależnie od formy prezentacji.

**Uzasadnienie — ToS §2.2:**

Regulamin zakazuje *"construct and build a similar or competitive website, product,
or service."* Strona ze statystykami meczowymi CS2 jest dokładnie tym, co HLTV
robi. Nawet jeśli nie konkurujesz bezpośrednio cenowo, ryzyko naruszenia jest wysokie.

**Uzasadnienie — RODO:**

Publiczne wyświetlanie statystyk z imieniem gracza, aliasem lub SteamID = publiczne
udostępnienie danych osobowych. Wyłączenie "household exemption" (Scenariusz 3)
odpada automatycznie. Wymagana pełna podstawa prawna RODO dla każdej kategorii
wyświetlanych danych. Publiczny charakter kariery esportowej zawodowca nie jest
sam w sobie podstawą prawną.

**Rekomendacja jeśli chcesz to zrobić legalnie:**

| Krok | Uzasadnienie |
|---|---|
| Skontaktuj się z HLTV o licencję na dane | Jedyna pewna ścieżka legalna przy tej skali |
| Użyj FACEIT API jako źródła | Ma warunki dopuszczające aplikacje trzecie z kluczem API |
| Wyświetlaj tylko statystyki zagregowane | Zmniejsza ryzyko RODO — bez identyfikacji graczy |
| Nie wyświetlaj SteamID i nazwisk publicznie | Pseudonimizacja obniża ryzyko RODO |
| Dodaj politykę prywatności i prawo do usunięcia | Obowiązek przy publicznym przetwarzaniu danych |

---

## Podsumowanie ryzyk

| Scenariusz | Ryzyko ToS §2.2 | Ryzyko Dyrektywy 96/9 | Ryzyko RODO | Rozwiązanie |
|---|---|---|---|---|
| Monetyzacja Twittera | **WYSOKIE** | Niskie | Niskie | Zgoda HLTV lub FACEIT API |
| Tysiące demo lokalnie | Średnie | **WYSOKIE** | Średnie | Formalna zgoda HLTV |
| `players.json` lokalnie | Niskie | Niskie | **ŚREDNIE** | Minimalizacja danych, podstawa art. 6 |
| Publiczna strona | **WYSOKIE** | **WYSOKIE** | **WYSOKIE** | Licencja HLTV lub FACEIT API + RODO compliance |

**Wspólny mianownik:** Im bardziej komercyjny i publiczny cel, tym silniejsza potrzeba
formalnej zgody HLTV. Email z zapytaniem to najtańsze i najskuteczniejsze rozwiązanie
dla scenariuszy 1, 2 i 4.

---

## Źródła

- HLTV.org Terms of Service (plik `HLTV_TOS.md`)
- HLTV.org robots.txt (plik `HLTV_robots.txt`)
- Dyrektywa 96/9/EC o ochronie prawnej baz danych
- TSUE C-30/14, *Ryanair v. PR Aviation* (2015)
- TSUE C-582/14, *Breyer v. Bundesrepublik Deutschland* (2016)
- TSUE C-46/02, *Fixtures Marketing v. Oy Veikkaus* (2004)
- TSUE C-604/10, *Football Dataco v. Yahoo!* (2012)
- hiQ Labs v. LinkedIn (9th Cir. 2022)
- RFC 9309 — Robots Exclusion Protocol
