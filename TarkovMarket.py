from requests import get
from json import loads
import os
from rich.console import Console
from rich.table import Table

os.system("cls" if os.name == "nt" else "clear")

print("---------------------------------------------\nMade by Ṿictor#4300\nAll information provided by tarkov-market.com\n---------------------------------------------\n")


out = Console()

os.system("title Tarkov Market Lookup")

def getJSON(item):

    url = "https://api.victorangel.xyz/market?item={}".format(item)

    r = get(url)

    j = loads(r.text)

    return j


def getInfo():

    item = input("What item would you like to check? ")

    j = getJSON(item)

    price = j[0]["price"]

    symbol = j[0]["traderPriceCur"]

    item = j[0]["name"]

    traderPrice = j[0]["traderPrice"]
    
    traderName = j[0]["traderName"]

    changeD = j[0]["diff24h"]
    
    changeW = j[0]["diff7days"]

    slots = j[0]["slots"]

    link = j[0]["wikiLink"]

    tmLink = j[0]["link"]

    return price, symbol, item, traderPrice, traderName, changeD, changeW, slots, link, tmLink


while True:
    try:
        price, symbol, item, traderPrice, traderName, changeD, changeW, slots, link, tmLink = getInfo()

        table = Table(show_header=True, header_style="bold cyan")

        table.add_column("Item")

        table.add_column("Price")

        table.add_column("Per Slot")
        
        table.add_column("Trader")

        table.add_column("Trader Price")

        if changeD >= 0:
            table.add_column("Δ 24h", style="bold green")
        else:
            table.add_column("Δ 24h", style="bold red")

        if changeW >= 0:
            table.add_column("Δ 7d", style="bold green")
        else:
            table.add_column("Δ 7d", style="bold red")

        table.add_column("TM")

        table.add_row("[link={}]{}[/link]".format(link, item), "{}{:0,}".format(symbol, price), "{}{:0,}".format(symbol, int(price/slots)), traderName, "{}{:0,}".format(symbol, traderPrice), "{}%".format(changeD), "{}%".format(changeW), "[link={}]TM[/link]".format(tmLink))
        
        os.system("cls" if os.name == "nt" else "clear")

        out.print(table)

    except Exception as e:
        print("Nothing found! / Error:",e)

        continue