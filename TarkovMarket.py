from requests import get
from json import loads
import os
from rich.console import Console
from rich.table import Table
from SpeechRecognition import *
import keyboard


print("Made by Victor Angel#4300\n")

apiKey = "oC0gJBLoR17SFv8T"

out = Console()

os.system("title Tarkov Market Lookup")

def getJSON(item, apiKey):

    url = "https://tarkov-market.com/api/v1/item?q={}&x-api-key={}".format(item, apiKey)

    r = get(url)
    j = loads(r.text)

    return j


def getInfo(item, apiKey):

    # item = input("What item would you like to check? ")

    j = getJSON(item, apiKey)

    price = j[0]["price"]
    symbol = j[0]["traderPriceCur"]
    item = j[0]["name"]
    traderPrice = j[0]["traderPrice"]
    traderName = j[0]["traderName"]
    changeD = j[0]["diff24h"]
    changeW = j[0]["diff7days"]
    slots = j[0]["slots"]

    return price, symbol, item, traderPrice, traderName, changeD, changeW, slots


while True:
    try:
        if keyboard.is_pressed('home'):
            price, symbol, item, traderPrice, traderName, changeD, changeW, slots = getInfo(str(speechToText()), apiKey)
            textToSpeech(str(price))

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

            table.add_row(item, "{}{:0,}".format(symbol, price), "{}{:0,}".format(symbol, int(price/slots)), traderName, "{}{:0,}".format(symbol, traderPrice), "{}%".format(changeD), "{}%".format(changeW))
            
            os.system("cls" if os.name == "nt" else "clear")

            out.print(table)

    except Exception as e:
        print("Nothing found! / Error:",e)

        continue