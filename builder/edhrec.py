from urllib.parse import urljoin
import requests_cache
import requests


requests_cache.install_cache("api_cache")
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


def get_edhrec_commander_analysis(cardname, format="basic"):
    url = f"https://json.edhrec.com/pages/commanders/{edhrec_stringify(cardname)}.json"
    response = requests.get(url)
    groups = {}
    for group in response.json()["container"]["json_dict"]["cardlists"]:
        groupname = group["header"]
        cards = []
        for card in group["cardviews"]:
            cards.append(card["name"])
        groups[groupname] = cards
    if format == "basic":
        def flatten(l):
            return [item for sublist in l for item in sublist]
        return flatten(groups.values())
    else:
        return groups


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
