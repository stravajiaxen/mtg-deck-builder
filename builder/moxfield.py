import requests

def get_decklist(hsh):

    api = f"https://api2.moxfield.com/v3/decks/all/{hsh}"

    response = requests.get(api)

    json = response.json()
    #return json
    main = json["boards"]["mainboard"]["cards"]
    side = json["boards"]["sideboard"]["cards"]

    cards = [main[hsh]["card"]["name"] for hsh in main.keys()]
    cards += [side[hsh]["card"]["name"] for hsh in side.keys()]

    return cards
