<h1>Elections Scraper</h1>
Projekt pro ENGETO

---

<h2>Popis projektu</h2>

Election Scrapper je program, který stahuje výsledky voleb do poslanecké sněmovny z roku 2017.

Uživatel zadá: 
1. URL s výsledky voleb z územního celku (např. [Výsledky pro Prahu](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100))
2. Název souboru, do kterého se mají výsledky uložit (ve formátu CSV)

---

<h2>Instalace knihoven</h2>

Použité knihovny jsou v souboru ```requirements.txt```. Nainstalovat knihvny lze pomocí příkazů: 

```pip install -r requirements.txt```

<h2>Spuštění programu</h2>

Program se spouští souborem elections_scrapper.py a dvěma argumenty.

```python election_scraper.py <odkaz-uzemniho-celku> <vysledny_soubor.csv>```

<h2>Ukázka projektu</h2>

Výsledky pro s Benešov ve Středočeském kraji. 

|Argument|Příklad|
|---------|------|
|URL|"https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"|
|název souboru|vysledky.csv|

Spuštění programu: 

```python elections_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vystup.csv```

Průběh programu: 

```
Skript se spustil.
Validace argumentů... OK
Stahuji data z url https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
Zahajuji analýzu dat
Analýza dat... OK
Data byla uložena do souboru vystup.csv.7
```
