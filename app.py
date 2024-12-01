import requests

url = "https://api.coingecko.com/api/v3/simple/price"


params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Vérifie si la requête a réussi

    data = response.json()
    bitcoin_price = data["bitcoin"]["usd"]

    print(f"Le prix actuel du Bitcoin est de ${bitcoin_price} USD.")
    print('end')

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête API : {e}")