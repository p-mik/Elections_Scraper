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
|-------------|------------|

Spuštění programu: 

```python elections_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vystup.csv```

Průběh programu: 

```
Skript se spustil.
Validace argumentů... OK
Stahuji data z url https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
Zahajuji analýzu dat
Analýza dat... OK
Data byla uložena do souboru vystup.csv.
```

Částečný výstup: 

```
Kód okrsku,Název obce,Registrovaní voliči,Vydané obálky,Platné hlasy,Občanská demokratická strana...
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
```