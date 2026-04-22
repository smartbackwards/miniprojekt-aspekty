# Legalność pobierania i parsowania demo plików CS2 z HLTV.org

**Mini-projekt** — Aspekty prawne, społeczne i etyczne w sztucznej inteligencji
**Autor:** Bartosz Tramś  
**Data:** Kwiecień 2025  

---

## Cel projektu

Analiza prawna i techniczna legalności **ręcznego** pobierania oraz parsowania
plików `.dem` (GOTV demo) z serwisu HLTV.org w kontekście działalności osobistej:
pracy magisterskiej z dziedziny CS2/ML oraz tworzenia postów na platformie X (Twitter).

Projekt odpowiada na pytania:
- Czym różni się ręczne pobieranie pliku od automatycznego scrapingu w rozumieniu prawa?
- Co mówi `robots.txt` HLTV i komu te dyrektywy dotyczą?
- Co mówi regulamin HLTV na temat scrapingu i korzystania z treści?
- Kto jest właścicielem danych zawartych w pliku `.dem`?
- Jakie przepisy UE (prawo baz danych, RODO) mają zastosowanie?
- Jakie są praktyczne rekomendacje compliance dla mojego przypadku użycia?

## Struktura repozytorium

```
miniprojekt/
├── README.md                           # Ten plik
├── PROCESS.md                          # Dokumentacja procesu, prompty AI, decyzje
├── instructions.txt                    # Wymagania mini-projektu od prowadzącego
├── hltv_files/
│   ├── HLTV_TOS.md                     # Pełny regulamin HLTV.org (Terms of Service)
│   ├── HLTV_privacy.md                 # Polityka prywatności HLTV.org
│   ├── HLTV_cookies.md                 # Polityka cookies HLTV.org
│   └── HLTV_robots.txt                 # Plik robots.txt HLTV.org
├── claude/
│   ├── legal_opinion.md                # Opinia prawna: analiza legalności pobierania demo
│   └── scenariusze_rozszerzone.md      # Analiza scenariuszy: Twitter, skala, RODO, strona WWW
├── kod/
│   ├── analyze.py                      # Skrypt: robots.txt + ToS fetch z obsługą błędów
│   └── analiza.ipynb                   # Notebook: pełna analiza prawna + wizualizacje
└── wyniki/
    ├── fetch_results.json              # Surowe wyniki HTTP (generowane przez skrypt)
    ├── access_status.png               # Wykres dostępności platform
    ├── platform_comparison.csv         # Tabela porównawcza platform
    └── compliance_checklist.csv        # Checklista compliance dla projektu
```

## Jak uruchomić

### Wymagania

- Python 3.9+
- pip

### Instalacja

```bash
pip install requests beautifulsoup4 rich pandas matplotlib jupyter
```

### Uruchomienie skryptu

```bash
cd kod
python analyze.py
```

Skrypt sprawdzi robots.txt i dostępność stron ToS dla HLTV oraz porównawczych platform (ESL, Faceit, Valve).
Wyniki zostaną zapisane do `wyniki/fetch_results.json`.

### Uruchomienie notebooka

```bash
cd kod
jupyter notebook analiza.ipynb
```

Notebook zawiera pełną analizę prawną, wizualizacje i compliance checklist.
Uruchom wszystkie komórki po kolei (`Kernel → Restart & Run All`).

## Kluczowe wyniki

| Platforma | robots.txt | ToS — scraping | Publiczne API |
|---|---|---|---|
| HLTV.org | Istnieje (Cloudflare blokuje odczyt) | **ZAKAZANY** (§2.2) | NIE |
| Faceit | Do sprawdzenia | Zakazany | **TAK** (klucz darmowy) |
| ESL Gaming | Do sprawdzenia | Zakazany | NIE |
| Valve / Steam | 200 OK | Dozwolone (użytek os.) | **TAK** (Steam Web API) |

**Najważniejsze wnioski:**
1. `robots.txt` HLTV zawiera `Disallow: /download/demo*` — ale dyrektywa ta dotyczy **wyłącznie automatycznych botów**, nie użytkowników ręcznie pobierających pliki przez przeglądarkę
2. ToS §2.2 zakazuje "web scraping" — ręczne klikanie i pobieranie pliku nie mieści się w tej definicji
3. Użytek niekomercyjny (praca magisterska) jest bezpieczniejszy prawnie niż komercyjny (monetyzowane posty)
4. SteamID64 w plikach `.dem` to dane osobowe w rozumieniu RODO — wymaga podstawy prawnej do przetwarzania
5. Baza demo HLTV jest chroniona prawem sui generis (Dyrektywa 96/9/EC) — dotyczy masowego pobierania, nie pojedynczych plików

## Czego projekt nie robi

- Nie dostarcza porad prawnych (analiza ma charakter edukacyjny)
- Skrypt `analyze.py` nie pobiera ani nie przechowuje plików `.dem`
- Nie obchodzi zabezpieczeń Cloudflare ani żadnych innych mechanizmów anty-botowych

## Kontekst osobisty

Analiza powstała w bezpośrednim związku z moją działalnością — ręcznym pobieraniem
plików `.dem` z HLTV.org do pracy magisterskiej (ML/CS2) oraz tworzenia treści na
platformę X (Twitter). Kluczowym pytaniem było, czy obecna praktyka jest legalna
i jakie są jej granice — szczególnie w kontekście różnicy między użytkiem
akademickim a publikacjami w mediach społecznościowych.

## Źródła

- HLTV.org Terms of Service: https://www.hltv.org/terms (cache Google, 2025-01-27)
- Dyrektywa 96/9/EC o ochronie prawnej baz danych
- TSUE C-30/14, Ryanair v. PR Aviation (2015)
- TSUE C-582/14, Breyer v. Bundesrepublik Deutschland (2016)
- hiQ Labs v. LinkedIn (9th Cir. 2022)
- Valve Steam Subscriber Agreement: https://store.steampowered.com/subscriber_agreement/
- Faceit Data API: https://developers.faceit.com/
