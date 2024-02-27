import requests
import sys

try:

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    rate = url["bpi"]["USD"]["rate"].replace(',', '')
    rate = float(rate) * float(sys.argv[1])
    print(f"${rate:,.4f}")

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except requests.RequestException:
    print("Error")