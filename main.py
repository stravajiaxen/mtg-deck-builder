import streamlit as st
from builder.lists import *
from builder.edhrec import *
from builder.compare import *
from builder.moxfield import *
from builder.mtgjson import *
from streamlit_option_menu import option_menu
import pandas as pd

import requests

@st.cache_data(persist="disk")
def get_collection():
    return {
        "Volrath, The Shapestealer": get_decklist("L_CrzCH_qUerNwVK5j-xFg"),
        "Niv-Mizzet, Parun": get_decklist("RX2bhkt9wk6JkDuF164I2A"),
        "Ezuri, Claw of Progress": get_decklist("zl1Xt5XLBEyTlGbUn-Mk0w"),
        "Nicol Bolas, the Ravager": get_decklist("K8HGNiyIU02QogqrSYCcBg"),
        "Sevinne, the Chronoclasm": get_original_cards("https://mtgjson.com/api/v5/decks/MysticIntellect_C19.json"),
        "Commons": get_commons_from_sets(*["MOM", "ONE", "BRO", "DMU", "SNC", "NEO", "VOW",
                                        "MID", "AFR", "STX", "KHM", "ZNR", "WAR", "XLN",
                                        "HOU", "AKH", "AER", "DTK", "MH1", "MH2", "LTR",
                                        "DMR", "JMP", "J22"]),
        "Collection": list(my_cards["Name"]),
    }

collections = get_collection()

all_cards = [item for sublist in collections.values() for item in sublist]
#prices = pd.DataFrame(requests.get("https://mtgjson.com/api/v5/AllPricesToday.json").json()["data"])


def show_edhrec_from_cardname(cardname):
    embedded_url = edhrec_stringify(cardname)
    embedded_url = r"https://edhrec.com/commanders/" + embedded_url

    # TODO: This looks and acts kinda crappy. Improve it!
    st.components.v1.html(f'<iframe src="{embedded_url}" width=800 height=600></iframe>')


def show_commanders():
    """
    Show the commanders tab
    :return:
    """

    # I can view a list of commanders and compare them to my collection
    commander_list = top_commanders_2_years  # TODO: Make this a dropdown
    selected_commander = st.selectbox("Choose a commander", commander_list)
    #comparison = recommended_cards(my_cards, selected_commander)
    st.write(f"Useful Cards I own for {selected_commander}:")
    commander_recs = get_edhrec_commander_analysis(selected_commander)
    st.write(commander_recs[commander_recs["name"].isin(my_cards["Name"])])
    #st.write(my_cards[my_cards["Name"].isin(comparison["Cards"])])

def show_collection():
    # Improve this by changing how I get the dataframe by comparing to actual moxfield decklists
    fil = st.text_input("Find a Card:")
    # st.write(my_cards[my_cards["Name"].str.contains(fil, case=False)])

    # Allow me to browse lists of collections
    #   Full Collection
    #   Moxfield Decks

    # Allow me to download a list and view it visually and sort, with card images
    #   - consider exporting it to another app to view

def show_compare():
    st.write("TODO: Select multiple saved collections and mess with them")
    #st.write(get_decklist("uHvbX5Y9NUWnTMBV4UOWpw"))  # Scion of the ur-dragon test deck
    st.write(collections['Commons'])

def main():
    st.title("MTG Commander Analysis App")
    with st.sidebar:
        selected = option_menu("Main Menu", ["Commanders", 'Collection', 'Compare'],
                               icons=['house', 'gear', 'house'], menu_icon="cast", default_index=1)
        st.write(selected)

    if selected == "Commanders":
        show_commanders()
    if selected == "Collection":
        show_collection()
    if selected == "Compare":
        show_compare()
    # show_edhrec_from_cardname("Ezuri, Claw of Progress")


if __name__ == "__main__":
    main()
