from urllib.parse import urljoin
#import requests_cache
import requests
import json
import pandas as pd
import streamlit as st


#requests_cache.install_cache("api_cache")
# TODO: Replace with https://stackoverflow.com/questions/32287885/caching-functions-in-python-to-disk-with-expiration-based-on-version


def edhrec_stringify(cardname):
    """
    Gets the EDHREC url given a cardname

    :param cardname: The name of the card
    :return:
    """

    deletions = [",", "'", '"', "&"]
    for c in deletions:
        cardname = cardname.replace(c, "")
    cardname = cardname.lower()
    cardname = "-".join(cardname.split())
    return cardname


def get_edhrec_url(cardname):
    return urljoin("https://edhrec.com/commanders/", edhrec_stringify(cardname))


@st.cache_data(persist="disk")
def get_edhrec_commander_analysis(cardname):
    url = f"https://json.edhrec.com/pages/commanders/{edhrec_stringify(cardname)}.json"
    response = requests.get(url)
    cards_edh_df = pd.DataFrame(response.json()["cardlist"])
    cards = [card["name"] for card in response.json()["cardlist"]]
    full_cards = get_edhrec_card_info(cards)
    full_cards_info = pd.DataFrame(list(full_cards.json()["cards"].values()))
    merged = pd.merge(cards_edh_df, full_cards_info, on="name", how="outer")
    merged["deck_rate"] = merged["num_decks"] / merged["potential_decks"]

    def extract_tcgplayer_price(json_str):
        try:
            json_obj = json_str#json.loads(json_str)
            tcgplayer_price = json_obj.get('tcgplayer', {}).get('price', None)
            return tcgplayer_price
        except json.JSONDecodeError:
            return None

    merged['tcgplayer_price'] = merged['prices'].apply(extract_tcgplayer_price)
    return merged

    # Return Name, Type, Synergy, Inclusion Rate, Price


def get_edhrec_decklinks(cardname):
    url = f"https://json.edhrec.com/pages/decks/{edhrec_stringify(cardname)}.json"
    response = requests.get(url)
    links = []
    for item in response.json()["table"]:
        links.append(urljoin("https://edhrec.com/deckpreview/", item["urlhash"]))
    return links


def get_edhrec_decklist(url):
    url = url.strip("/")
    hash = url.split("/")[-1]
    url = f"https://edhrec.com/api/deckpreview/{hash}"
    response = requests.get(url)
    return response.json()["cards"]

def get_edhrec_card_info(cardnames):
    names = [edhrec_stringify(cardname) for cardname in cardnames]
    payload = {"format": "dict", "names": names}
    headers = {'content-type': 'application/json'}
    url = "https://edhrec.com/api/cards/"
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response

if __name__ == '__main__':
    cards = get_edhrec_commander_analysis("Krenko, Mob Boss")
    cards.to_csv("test.csv")