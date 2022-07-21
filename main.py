import typer
import requests

app = typer.Typer()

@app.command()
def all():
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
    # Making list for multiple crypto's
    currencies = ["BTCGBP", "LTCGBP", "ETHGBP", "XRPGBP", "DOGEGBP"]
    currenciesNames = ["Bitcoin", "Litecoin", "Ethereum", "Ripple", "Dogecoin"]
    j = 0
  
    # running loop to print all crypto prices
    for i in currencies:
    
        # completing API for request
        url = key+currencies[j]  
        data = requests.get(url)
        data = data.json()
        price = data['price'].rstrip("0")
        print(f"{currenciesNames[j]} price is £{price}")
        j = j+1

@app.command()
def bitcoin():
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCGBP"
    
    data = requests.get(key)
    data = data.json()
    price = data['price'].rstrip("0")
    print(f"Bitcoin price is £{price}")

@app.command()
def litecoin():
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol=LTCGBP"
    
    data = requests.get(key)
    data = data.json()
    price = data['price'].rstrip("0")
    print(f"Litecoin price is £{price}")

@app.command()
def ripple():
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPGBP"
    
    data = requests.get(key)
    data = data.json()
    price = data['price'].rstrip("0")
    print(f"Ripple price is £{price}")

@app.command()
def dogecoin():
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEGBP"
    
    data = requests.get(key)
    data = data.json()
    price = data['price'].rstrip("0")
    print(f"Dogecoin price is £{price}")
    

if __name__ == "__main__":
    app()