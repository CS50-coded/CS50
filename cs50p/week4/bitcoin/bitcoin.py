import argparse
import requests

CONST_BITCOIN_ENDPOINT = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Bitcoin",
        description="Calculate the cost for user's bitcoin amount")
    parser.add_argument("amount", type=float)
    args = parser.parse_args()

    try:
        res = requests.get(CONST_BITCOIN_ENDPOINT)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"An HTTP error occurred: {e}")
    else:
        data = res.json()
        print(f"${float(data["bpi"]["USD"]["rate_float"]) * args.amount:,.4f}")


if __name__ == "__main__":
    main()
