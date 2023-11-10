import requests

def get_original_cards(url):
    response = requests.get(url)
    # return response.json()
    return [card["name"] for card in response.json()["data"]["mainBoard"]]


def get_commons_from_sets(*setlist):
    url = "https://mtgjson.com/api/v5/{setname}.json"
    cards = []
    for s in setlist:
        proper_url = url.format(setname=s)
        response = requests.get(proper_url)
        cards += [card["name"] for card in response.json()["data"]["cards"] if card["rarity"] == "common"]

    return list(set(cards))
