from builder.edhrec import get_edhrec_commander_analysis


def recommended_cards(mine, commander):
    cards = set(get_edhrec_commander_analysis(commander, format="basic"))
    owned_cards = set(mine.Name)
    got_em = owned_cards.intersection(cards)
    full_df = mine[mine["Name"].isin(got_em)]
    full_df["Price"] = full_df["Price"].str[1:].astype(float)
    full_df = full_df.drop_duplicates(subset=["Name"])
    price = full_df["Price"].sum()
    return {"Number": len(got_em), "Price": price, "Cards": got_em}
