import sys
import requests


def main():
    
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    
    price = get_price()

    print(f"${n * price:,.4f}")


def get_price():
    api_key = "YourApiKey"  
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not retrieve bitcoin price")


main()