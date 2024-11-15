"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Petr Mikulka
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

def validuj_argumenty(): # kontorla, jestli byly zadány všechny argumenty
    if len(sys.argv) != 3:
        print("Chyba: Musíte zadat 2 argumenty")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def stahni_data(url): # stahování dat pro analýzu
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování dat: {e}")
        sys.exit(1)

def ulož_html(html, nazev_souboru): # Ukládám si obsah HTML pro kontrolu
    with open(nazev_souboru, "w", encoding="utf-8") as f:
        f.write(html)

def analyzuj_html(html): # Procházím stránku vyšší úrovně a dávám dohromady odkazi na nižšší celky
    soup = BeautifulSoup(html, "html.parser")
    tabulky = soup.find_all("table")
    data = []

    for tabulka in tabulky:
        radky = tabulka.find_all("tr")[2:]
        for radek in radky:
            bunky = radek.find_all("td")
            if bunky:
                kod_okrsku = bunky[0].text.strip()
                nazev_obce = bunky[1].text.strip()
                odkaz = "https://www.volby.cz/pls/ps2017nss/" + bunky[0].find("a")["href"]
                data.append([kod_okrsku, nazev_obce, odkaz])

    return data

def analyzuj_detail(url):
    html = stahni_data(url)
    soup = BeautifulSoup(html, "html.parser")

    registrovani_volici = soup.find("td", headers="sa2").text.strip()
    vydane_obalky = soup.find("td", headers="sa3").text.strip()
    platne_hlasy = soup.find("td", headers="sa6").text.strip()

    tabulky = soup.find_all("table")

    relevantni_tabulky = tabulky[1:3]  # Potřebuju stahovat data z druhé a třetí tabulky

    nazvy_stran = []
    hlasy_pro_strany = []

    for tabulka in relevantni_tabulky:
        nazvy_stran.extend( # Názvy stran
            [td.text.strip() for td in tabulka.find_all("td", class_="overflow_name")]
        )

        hlasy_pro_strany.extend( #Hlasy stran
            [
                radek.find_all("td")[2].text.strip()
                for radek in tabulka.find_all("tr")
                if len(radek.find_all("td")) > 2  # Zkontrolujeme, že řádek má alespoň 3 buňky
            ]
        )

    obec_data = [registrovani_volici, vydane_obalky, platne_hlasy] + hlasy_pro_strany # Spojení dat
    return obec_data, nazvy_stran

def uloz_vysledky_csv(data, hlavicka, nazev_souboru): # Uložení výsledků do CSV
    with open(nazev_souboru, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(hlavicka)
        writer.writerows(data)
    print(f"Data byla uložena do souboru {nazev_souboru}.")

def program():
    print("Skript se spustil.")
    url, vystupni_soubor = validuj_argumenty()

    print("Validace argumentů... OK") # První ČEK

    html = stahni_data(url)
    ulož_html(html, "stazena_stranka.html")

    print(f"Stahuji data z url {sys.argv[1]}")
    print("Zahajuji analýzu dat")
    obce_data = analyzuj_html(html)
    vsechny_vysledky = []
    hlavicka = []

    for idx, obec in enumerate(obce_data):
        kod_okrsku, nazev_obce, detail_url = obec
        # print(f"Zpracovávám obec: {nazev_obce} (Kód okrsku: {kod_okrsku})")
        detail_data, nazvy_stran = analyzuj_detail(detail_url)

        if idx == 0:
            hlavicka = ["Kód okrsku", "Název obce", "Registrovaní voliči", "Vydané obálky", "Platné hlasy"] + nazvy_stran # Hlavička

        vysledek = [kod_okrsku, nazev_obce] + detail_data
        vsechny_vysledky.append(vysledek)

    print("Analýza dat... OK")

    uloz_vysledky_csv(vsechny_vysledky, hlavicka, vystupni_soubor)

# Spustí program bez další složitosti
program()
