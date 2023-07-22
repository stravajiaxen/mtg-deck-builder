import streamlit as st
from builder.lists import *
from builder.deck import *


def show_edhrec_from_cardname(cardname):
    embedded_url = edhrec_stringify(cardname)
    embedded_url = r"https://edhrec.com/commanders/" + embedded_url

    # TODO: This looks and acts kinda crappy. Improve it!
    st.components.v1.html(f'<iframe src="{embedded_url}" width=800 height=600></iframe>')

def main():
    st.title("MTG Commander Analysis App")
    show_edhrec_from_cardname("Ezuri, Claw of Progress")


if __name__ == "__main__":
    main()
