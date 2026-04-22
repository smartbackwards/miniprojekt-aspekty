# PROCESS.md — Dokumentacja procesu pracy

Ten plik dokumentuje **jak** powstawał mini-projekt: jakich narzędzi AI użyłem,
jakie prompty pisałem, jakie decyzje podjąłem i co nie zadziałało.

---

## Narzędzia AI użyte w projekcie

| Narzędzie | Do czego użyte |
|---|---|
| **Claude (Anthropic)** | Konsultacja zakresu projektu, analiza prawna, generowanie kodu skryptu i notebooka, drafting README/PROCESS |
| **Claude web search** | Wyszukanie i pobranie treści ToS HLTV.org (strona blokuje bezpośredni dostęp) |

---

## Chronologia pracy i prompty

### Etap 1 — Wybór tematu i zakresu

**Prompt do Claude:**
> *"i want to focus on my own topic, related to parsing CS:GO/CS2 demos and its legality, by going through terms of service from HLTV.org and seeing if there's some sort of license."*

**Decyzja:** Claude zaproponował mapę projektu na trzech poziomach (Base/Good/Excellent).
Zdecydowałem się celować w poziom Excellent przez:
- Dodanie analizy prawa baz danych UE (sui generis)
- Dodanie RODO / SteamID jako danych osobowych
- Porównanie platform (HLTV, ESL, Faceit, Valve) jako kontekst/alternatywy
- Napisanie skryptu Python sprawdzającego dostęp

**Kontekst:** Analiza dotyczy mojej osobistej działalności — ręcznego pobierania plików
`.dem` z HLTV.org do pracy magisterskiej i tworzenia treści na Twitter/X.
Nie jest powiązana z żadnym projektem grupowym.

---

### Etap 2 — Próba pobrania ToS i robots.txt z HLTV.org

**Prompt do Claude:**
> *"i want to try and fetch the actual ToS since i think HLTV has a pretty robust anti-scraping defense"*

**Co się stało:**
1. Próba bezpośredniego `web_fetch` na `hltv.org/terms-of-service` → błąd PERMISSIONS_ERROR
2. Wyszukiwarka zwróciła URL `hltv.org/terms` → próba `web_fetch` → **HTTP 403 (Cloudflare)**
3. Próba `web_fetch` na `hltv.org/robots.txt` → PERMISSIONS_ERROR (URL nie był w wynikach wyszukiwania)
4. Wyszukiwanie `site:web.archive.org hltv.org/robots.txt` → brak wyników
5. Wyszukiwanie `hltv.org robots.txt disallow` → potwierdzenie że robots.txt istnieje, ale treść niedostępna

**Co zadziałało:**
- Google cache / snippet z wyszukiwarki zwrócił kluczowe fragmenty ToS (§2.2, §3.1, §6.3, §7.1)
- SEO audit tool potwierdził że robots.txt istnieje pod `hltv.org/robots.txt`

**Wniosek / decyzja:** Samo zablokowanie fetchu to **wartościowy wynik badawczy** —
pokazuje, że HLTV technicznie egzekwuje zakaz z ToS. Udokumentuję to w analizie.

---

### Etap 3 — Budowa repozytorium

**Prompt do Claude:**
> *"can you help me draft the repository?"*

Claude wygenerował:
- `kod/analyze.py` — skrypt Python sprawdzający robots.txt i ToS dla 4 platform
- `kod/analiza.ipynb` — notebook z pełną analizą prawną
- `README.md` — opis projektu
- `PROCESS.md` — ten plik

**Moje decyzje podczas przeglądu kodu:**
- Dodałem komentarz `# Identify ourselves honestly as a research script` przy User-Agent
  → etyczna decyzja: nie ukrywamy że jesteśmy botem, nawet jeśli serwer nas blokuje
- Zachowałem `time.sleep(1)` między requestami → "polite scraper" nawet w kontekście badawczym
- Zdecydowałem się NIE używać technik obejścia Cloudflare (np. headless browser)
  → te techniki byłyby nieetyczne i naruszałyby ducha ToS nawet w celach badawczych

---

## Co nie zadziałało i dlaczego

### Problem 1: Bezpośredni dostęp do HLTV.org
**Co próbowałem:** `requests.get("https://www.hltv.org/terms")` i `web_fetch`  
**Wynik:** HTTP 403 — Cloudflare bot challenge  
**Dlaczego:** HLTV używa Cloudflare z aktywnym bot managementem. Standardowe requesty
bez wykonania JavaScript challenge page są blokowane.  
**Decyzja:** Nie próbowałem obejść blokady (headless browser, solver). Zamiast tego
udokumentowałem 403 jako część wyników — to samo w sobie jest dowodem na techniczne
egzekwowanie ToS.

### Problem 2: robots.txt HLTV nie był dostępny do fetch'a
**Powód:** Cloudflare blokuje nawet `robots.txt` dla nie-zaufanych user-agentów.
To jest ironiczne — `robots.txt` ma informować boty o zasadach, ale blokada Cloudflare
uniemożliwia botom jego odczytanie.  
**Rozwiązanie:** Potwierdziłem istnienie i obecność dyrektyw Disallow przez zewnętrzne
narzędzie SEO audit (seositecheckup.com), które miało wcześniejszy dostęp.

### Problem 3: Brak pełnego tekstu ToS
**Wynik:** Tylko fragmenty z Google cache (~30% pełnego dokumentu)  
**Decyzja:** Pracuję na dostępnych fragmentach + zaznaczam tę lukę w analizie.
Pełny ToS jest dostępny w przeglądarce z ręcznym przeglądaniem — jest to celowe
utrudnienie dla zautomatyzowanych klientów.

---

## Decyzje projektowe i uzasadnienia

| Decyzja | Uzasadnienie |
|---|---|
| Skupiam się na **ręcznym** pobieraniu, nie scrapingu | To rzeczywista praktyka — ręczne klikanie != web scraping (kluczowe rozróżnienie prawne) |
| Analizuję `robots.txt` mimo że pobierania są ręczne | Dyrektywy robots.txt dotyczą botów; ważne żeby to pokazać i wyjaśnić dlaczego mnie nie dotyczą |
| Porównuję 4 platformy zamiast tylko HLTV | Daje kontekst — pokazuje Faceit API jako legalną alternatywę na wypadek potrzeby automatyzacji |
| Analizuję SteamID pod RODO | Często pomijany aspekt; kluczowy przy pracy z danymi graczy w ML |
| Rozróżniam użytek akademicki vs. Twitter | Cel przetwarzania wpływa na podstawę prawną RODO i na ryzyko z §2.2 ToS ("commercially exploit") |
| Powołuję się na Dyrektywę 96/9/EC, nie tylko ToS | ToS to umowa prywatna; prawo baz danych to regulacja publiczna z niezależnymi skutkami |
| Skrypt nie próbuje obejść Cloudflare | Etyczna decyzja; omijanie byłoby sprzeczne z duchem projektu o aspektach prawnych AI |
| Piszę PROCESS.md po polsku | Zgodnie z wymaganiami prowadzącego; README po polsku z tabelami angielskimi dla czytelności |

---

## Iteracje i zmiany w trakcie

1. **Pierwotny plan:** tylko analiza HLTV ToS  
   **Zmiana:** rozszerzono o 3 dodatkowe platformy po rozmowie z Claude o alternatywach

2. **Pierwotny plan:** analiza tylko prawna (bez kodu)  
   **Zmiana:** dodano skrypt Python po uznaniu, że próba technicznego fetchu jest wartościowym dowodem

3. **Pierwotny plan:** analiza copyright pliku .dem  
   **Zmiana:** dodano warstwę RODO/SteamID i prawa baz danych po analizie z Claude —
   te aspekty okazały się ważniejsze praktycznie

4. **W trakcie weryfikacji projektu:** odkryto, że pierwotna analiza była zbyt nastawiona
   na automatyczny scraping, a rzeczywisty przypadek użycia to **ręczne pobieranie**.
   **Zmiana:** dodano kluczowe rozróżnienie robots.txt-dla-botów vs. użytkownik-ludzki,
   zaktualizowano analizę ToS §2.2 ("web scraping" ≠ ręczne pobieranie) oraz rekomendacje
   pod kątem dwóch celów: pracy magisterskiej i Twittera.

---

## Refleksja: świadome korzystanie z AI

Używając Claude jako asystenta w tym projekcie, świadomie:
- **Weryfikowałem** każdą klauzulę prawną przywołaną przez Claude (sprawdzałem numery artykułów, nazwy spraw sądowych)
- **Decydowałem** o granicach etycznych (nie obchodzić Cloudflare) mimo że Claude nie sugerował tego wprost
- **Modyfikowałem** generowany kod (dodałem komentarze, zmiana user-agenta na bardziej transparentny)
- **Traktuję** analizę prawną Claude jako punkt wyjścia, nie ostateczną opinię prawną

Narzędzia AI przyspieszyły badanie (wyszukiwanie, synteza), ale **interpretacja wyników
i decyzje projektowe** pozostały po mojej stronie.
