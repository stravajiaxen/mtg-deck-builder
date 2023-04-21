from urllib.parse import urljoin
import requests
import requests_cache
import pandas as pd
import os

requests_cache.install_cache("api_cache")

location = r"C:\Users\matts\Documents\coding\mtg_deck_builder"
fname = "All_Cards_2023_Apr_15_18-35.csv"
my_cards = pd.read_csv(os.path.join(location, fname), sep="\t")
dont_use = [
    'Breena',
    'Millicent',
    'Niv',
    'Osgir',
    'Captain ngathrod',
    'Chulane',
]
free_cards = my_cards[~my_cards["List name"].isin(dont_use)]
free_cards = free_cards.drop(free_cards[free_cards["Name"] == "The Locust God"].index)

top_commanders_today = """
Atraxa, Praetors' Voice
Tymna the Weaver
Lathril, Blade of the Elves
Isshin, Two Heavens as One
The Ur-Dragon
Sidar Jabari of Zhalfir
Thrasios, Triton Hero
Miirym, Sentinel Wyrm
Zimone and Dina
Atraxa, Grand Unifier
Yuriko, the Tiger's Shadow
Jodah, the Unifier
Wilhelt, the Rotcleaver
Gishath, Sun's Avatar
Prosper, Tome-Bound
Shorikai, Genesis Engine
Shalai and Hallar
Edgar Markov
Rograkh, Son of Rohgahh
Korvold, Fae-Cursed King
Teysa Karlov
Muldrotha, the Gravetide
Thalia and The Gitrog Monster
Kenrith, the Returned King
Urtet, Remnant of Memnarch
Giada, Font of Hope
Krenko, Mob Boss
Henzie "Toolbox" Torre
Animar, Soul of Elements
Ghyrson Starn, Kelermorph
Urza, Chief Artificer
Kaalia of the Vast
Malcolm, Keen-Eyed Navigator
Esika, God of the Tree
Omnath, Locus of All
Chatterfang, Squirrel General
Kraum, Ludevic's Opus
Omnath, Locus of Creation
K'rrik, Son of Yawgmoth
Magus Lucea Kane
Urabrask
Atla Palani, Nest Tender
Rashmi and Ragavan
Meren of Clan Nel Toth
Brimaz, Blight of Oreskos
Vial Smasher the Fierce
Winota, Joiner of Forces
Sakashima of a Thousand Faces
Go-Shintai of Life's Origin
Tevesh Szat, Doom of Fools
Ardenn, Intrepid Archaeologist
Sythis, Harvest's Hand
Kinnan, Bonder Prodigy
Breya, Etherium Shaper
Queen Marchesa
Alela, Artful Provocateur
Tivit, Seller of Secrets
Vishgraz, the Doomhive
Tana, the Bloodsower
Najeela, the Blade-Blossom
Sisay, Weatherlight Captain
Captain N'ghathrod
Zur the Enchanter
Etali, Primal Conqueror
Nekusar, the Mindrazer
Jetmir, Nexus of Revels
Arcades, the Strategist
Ixhel, Scion of Atraxa
Light-Paws, Emperor's Voice
Dihada, Binder of Wills
Urza, Lord High Artificer
Rin and Seri, Inseparable
Marneus Calgar
Raffine, Scheming Seer
Aesi, Tyrant of Gyre Strait
Niv-Mizzet, Parun
Liesa, Shroud of Dusk
Sheoldred, the Apocalypse
Satoru Umezawa
Ishai, Ojutai Dragonspeaker
Magda, Brazen Outlaw
Yarok, the Desecrated
Jeska, Thrice Reborn
Solphim, Mayhem Dominus
Elesh Norn, Mother of Machines
Feather, the Redeemed
Kykar, Wind's Fury
Brago, King Eternal
The Scarab God
Goro-Goro and Satoru
Sefris of the Hidden Ways
Lord Windgrace
Be'lakor, the Dark Master
Syr Gwyn, Hero of Ashvale
Yoshimaru, Ever Faithful
Tovolar, Dire Overlord
Zaxara, the Exemplary
Marchesa, the Black Rose
Ovika, Enigma Goliath
Veyran, Voice of Duality
Kess, Dissident Mage
Jodah, Archmage Eternal
Obeka, Brute Chronologist
Anowon, the Ruin Thief
Faldorn, Dread Wolf Herald
Baba Lysaga, Night Witch
Anhelo, the Painter
Silas Renn, Seeker Adept
Kasla, the Broken Halo
Hinata, Dawn-Crowned
Kibo, Uktabi Prince
Braids, Arisen Nightmare
Varina, Lich Queen
Kodama of the East Tree
Mishra, Eminent One
Myrkul, Lord of Bones
Rocco, Cabaretti Caterer
Ikra Shidiqi, the Usurper
Karumonix, the Rat King
Ivy, Gleeful Spellthief
Queza, Augur of Agonies
Xyris, the Writhing Storm
Ziatora, the Incinerator
Myrel, Shield of Argive
Tom Bombadil
Kalamax, the Stormsire
Osgir, the Reconstructor
Oloro, Ageless Ascetic
Chulane, Teller of Tales
Krark, the Thumbless
Chishiro, the Shattered Blade
Ramos, Dragon Engine
Slimefoot and Squee
Admiral Beckett Brass
Reyhan, Last of the Abzan
Yidris, Maelstrom Wielder
Tiamat
Tergrid, God of Fright
Imotekh the Stormlord
Orvar, the All-Form
Millicent, Restless Revenant
Nicol Bolas, the Ravager
Aminatou, the Fateshifter
Yawgmoth, Thran Physician
Sidisi, Brood Tyrant
Elas il-Kor, Sadistic Pilgrim
Bright-Palm, Soul Awakener
Burakos, Party Leader
Kroxa and Kunoros
Galea, Kindler of Hope
Kozilek, the Great Distortion
Yargle and Multani
Strefan, Maurer Progenitor
Haldan, Avid Arcanist
Pako, Arcane Retriever
Thrun, Breaker of Silence
Hidetsugu and Kairi
Bruse Tarl, Boorish Herder
Omnath, Locus of Rage
Morophon, the Boundless
Kyler, Sigardian Emissary
Dina, Soul Steeper
Gimbal, Gremlin Prodigy
Zevlor, Elturel Exile
Ratadrabik of Urborg
Raggadragga, Goreguts Boss
Adrix and Nev, Twincasters
Jinnie Fay, Jetmir's Second
Elsha of the Infinite
Rona, Herald of Invasion
Minsc & Boo, Timeless Heroes
Ezuri, Claw of Progress
Tatsunari, Toad Rider
Fynn, the Fangbearer
Jhoira, Weatherlight Captain
Kediss, Emberclaw Familiar
Zethi, Arcane Blademaster
Volo, Guide to Monsters
Kumena, Tyrant of Orazca
Wernog, Rider's Chaplain
Falco Spara, Pactweaver
Extus, Oriq Overlord
Phenax, God of Deception
Marwyn, the Nurturer
The First Sliver
The Howling Abomination
Kynaios and Tiro of Meletis
Zada, Hedron Grinder
Tuvasa the Sunlit
Narset, Enlightened Master
Elenda and Azor
Kenessos, Priest of Thassa
The Mimeoplasm
Inalla, Archmage Ritualist
The Gitrog Monster
Minn, Wily Illusionist
Alesha, Who Smiles at Death
Ghave, Guru of Spores
Ayula, Queen Among Bears
Neyali, Suns' Vanguard
Anje Falkenrath
Elminster
The Locust God
Xenagos, God of Revels
Arahbo, Roar of the World
Tasha, the Witch Queen
Tasigur, the Golden Fang
Hazezon, Shaper of Sand
Jared Carthalion
Grist, the Hunger Tide
Nethroi, Apex of Death
Derevi, Empyrial Tactician
Slicer, Hired Muscle
Sliver Overlord
Ghired, Conclave Exile
Ezuri, Stalker of Spheres
Grand Arbiter Augustin IV
Koma, Cosmos Serpent
Borborygmos and Fblthp
Saskia the Unyielding
Akiri, Line-Slinger
Juri, Master of the Revue
Umbris, Fear Manifest
Wilson, Refined Grizzly
Torbran, Thane of Red Fell
Selvala, Heart of the Wilds
Heliod, the Radiant Dawn
Skullbriar, the Walking Grave
Trostani, Selesnya's Voice
Araumi of the Dead Tide
Karador, Ghost Chieftain
Elenda, the Dusk Rose
Talrand, Sky Summoner
Magnus the Red
Ravos, Soultender
Hapatra, Vizier of Poisons
Rakdos, Lord of Riots
Yurlok of Scorch Thrash
Tayam, Luminous Enigma
Kamiz, Obscura Oculus
Breena, the Demagogue
Lonis, Cryptozoologist
Marrow-Gnawer
Chiss-Goria, Forge Tyrant
Athreos, God of Passage
Vorinclex, Monstrous Raider
Zedruu the Greathearted
Urza, Lord Protector
Abaddon the Despoiler
Brudiclad, Telchor Engineer
Edgin, Larcenous Lutenist
Mizzix of the Izmagnus
Polukranos Reborn
Dargo, the Shipwrecker
Okaun, Eye of Chaos
Zndrsplt, Eye of Wisdom
Omnath, Locus of Mana
Inga and Esika
Gargos, Vicious Watcher
Kwain, Itinerant Meddler
Maelstrom Wanderer
Emmara, Soul of the Accord
Gisa and Geralf
Rionya, Fire Dancer
Halana and Alena, Partners
Doran, the Siege Tower
Galazeth Prismari
Errant and Giada
Magar of the Magic Strings
Jan Jansen, Chaos Crafter
Mishra, Claimed by Gix
Kardur, Doomscourge
Greasefang, Okiba Boss
Jon Irenicus, Shattered One
Breeches, Brazen Plunderer
Kadena, Slinking Sorcerer
Ognis, the Dragon's Lash
Slimefoot, the Stowaway
Runo Stromkirk
Otharri, Suns' Glory
Meria, Scholar of Antiquity
Riku of Two Reflections
Graaz, Unstoppable Juggernaut
Evelyn, the Covetous
Ghalta, Primal Hunger
Ayara, First of Locthwain
Prossh, Skyraider of Kher
Roon of the Hidden Realm
Vadrik, Astral Archmage
Kelsien, the Plague
Jarad, Golgari Lich Lord
Obuun, Mul Daya Ancestor
Kydele, Chosen of Kruphix
Toggo, Goblin Weaponsmith
Chainer, Nightmare Adept
Saint Traft and Rem Karolus
Yennett, Cryptic Sovereign
Bjorna, Nightfall Alchemist
Cecily, Haunted Mage
Djeru and Hazoret
Jin-Gitaxias
Gavi, Nest Warden
Nine-Fingers Keene
Syr Konrad, the Grim
Goreclaw, Terror of Qal Sisma
Cadira, Caller of the Small
Gix, Yawgmoth Praetor
Megatron, Tyrant
Arixmethes, Slumbering Isle
Nalia de'Arnise
Titania, Protector of Argoth
Elesh Norn
Heliod, Sun-Crowned
Baeloth Barrityl, Entertainer
Ruric Thar, the Unbowed
Baru, Wurmspeaker
General Ferrous Rokiric
Toxrill, the Corrosive
Sidar Kondo of Jamuraa
Ich-Tekik, Salvage Splicer
Beledros Witherbloom
Optimus Prime, Hero
Lathiel, the Bounteous Dawn
Katilda and Lier
Rhys the Redeemed
Lynde, Cheerful Tormentor
Tatyova, Benthic Druid
Neera, Wild Mage
Zurgo Helmsmasher
Emry, Lurker of the Loch
Reaper King
Baral and Kari Zev
Mondrak, Glory Dominus
Wyleth, Soul of Steel
Abdel Adrian, Gorion's Ward
Grolnok, the Omnivore
Tinybones, Trinket Thief
Scion of the Ur-Dragon
Kamahl, Heart of Krosa
Silvar, Devourer of the Free
Trynn, Champion of Freedom
Garth One-Eye
Ashling the Pilgrim
Karametra, God of Harvests
Zask, Skittering Swarmlord
Shirei, Shizo's Caretaker
Codie, Vociferous Codex
The Council of Four
Jorn, God of Winter
Uril, the Miststalker
Sen Triplets
Ghalta and Mavren
Azusa, Lost but Seeking
Ranar the Ever-Watchful
Yedora, Grave Gardener
Glissa, the Traitor
Shanna, Purifying Blade
Toothy, Imaginary Friend
Ukkima, Stalking Shadow
Wyll, Blade of Frontiers
Jaheira, Friend of the Forest
Pramikon, Sky Rampart
Titania, Voice of Gaea
The Beamtown Bullies
Pir, Imaginative Rascal
Niv-Mizzet Reborn
Xenk, Paladin Unbroken
Mayael the Anima
Ashnod the Uncaring
Zacama, Primal Calamity
Akiri, Fearless Voyager
Grenzo, Dungeon Warden
Tor Wauki the Younger
Soul of Windgrace
Liliana, Heretical Healer
Lae'zel, Vlaakith's Champion
Adeline, Resplendent Cathar
Maarika, Brutal Gladiator
Willowdusk, Essence Seer
Purphoros, God of the Forge
Orah, Skyclave Hierophant
Gluntch, the Bestower
Averna, the Chaos Bloom
Cazur, Ruthless Stalker
Imoti, Celebrant of Bounty
Vrondiss, Rage of Ancients
Otrimi, the Ever-Playful
Esior, Wardwing Familiar
Carth the Lion
The Archimandrite
Old Stickfingers
Zurgo and Ojutai
Gyome, Master Chef
Thantis, the Warweaver
Atarka, World Render
Rafiq of the Many
Hamza, Guardian of Arashin
Othelm, Sigardian Outcast
Katilda, Dawnhart Prime
Zurzoth, Chaos Rider
Darien, King of Kjeldor
Octavia, Living Thesis
Shadrix Silverquill
Glissa Sunslayer
Rodolf Duskbringer
Daretti, Scrap Savant
Firesong and Sunspeaker
Etali, Primal Storm
Marisi, Breaker of the Coil
Marath, Will of the Wild
Liberator, Urza's Battlethopter
Kathril, Aspect Warper
Neyith of the Dire Hunt
Sheoldred
Feldon of the Third Path
Quintorius, Loremaster
Rivaz of the Claw
Wulfgar of Icewind Dale
Ganax, Astral Hunter
Armix, Filigree Thrasher
Bruvac the Grandiloquent
Baral, Chief of Compliance
Azami, Lady of Scrolls
Doric, Nature's Warden
Mazzy, Truesword Paladin
Estrid, the Masked
Ezuri, Renegade Leader
Olivia, Crimson Bride
Preston, the Vanisher
Zur, Eternal Schemer
Themberchaud
Bruna, Light of Alabaster
Yorion, Sky Nomad
Elmar, Ulvenwald Informant
Akroma, Vision of Ixidor
Ludevic, Necro-Alchemist
Ragavan, Nimble Pilferer
Liesa, Forgotten Archangel
Greensleeves, Maro-Sorcerer
Edric, Spymaster of Trest
Shabraz, the Skyshark
Gale, Waterdeep Prodigy
Alaundo the Seer
Karlov of the Ghost Council
Vaevictis Asmadi, the Dire
Jolene, the Plunder Queen
Balmor, Battlemage Captain
Tetsuo, Imperial Champion
Neheb, the Eternal
Firkraag, Cunning Instigator
Raphael, Fiendish Savior
Gilanra, Caller of Wirewood
Mishra, Tamer of Mak Fawa
Ghen, Arcanum Weaver
Tekuthal, Inquiry Dominus
Kruphix, God of Horizons
Ghoulcaller Gisa
Bruenor Battlehammer
Volrath, the Shapestealer
Killian, Ink Duelist
Chandra, Fire of Kaladesh
Brallin, Skyshark Rider
Rashmi, Eternities Crafter
Selvala, Explorer Returned
Raiyuu, Storm's Edge
Hofri Ghostforge
Orthion, Hero of Lavabrink
Lord Xander, the Collector
Kroxa, Titan of Death's Hunger
Archelos, Lagoon Mystic
Child of Alara
Omnath, Locus of the Roil
Balan, Wandering Knight
Belbe, Corrupted Observer
Blim, Comedic Genius
Jenson Carthalion, Druid Exile
Leinore, Autumn Sovereign
Perrie, the Pulverizer
Saheeli, the Gifted
Queen Kayla bin-Kroog
Braids, Conjurer Adept
Urza, Prince of Kroog
Ayara, Widow of the Realm
Auntie Blyte, Bad Influence
Zaffai, Thunder Conductor
Phelddagrif
Kresh the Bloodbraided
Sarulf, Realm Eater
Yusri, Fortune's Flame
Mogis, God of Slaughter
Kethis, the Hidden Hand
Trazyn the Infinite
Teysa, Orzhov Scion
""".strip().split("\n")

top_commanders_2_years = """
Adrix and Nev, Twincasters
Aesi, Tyrant of Gyre Strait
Alela, Artful Provocateur
Anhelo, the Painter
Animar, Soul of Elements
Anowon, the Ruin Thief
Arcades, the Strategist
Ardenn, Intrepid Archaeologist
Atla Palani, Nest Tender
Atraxa, Praetors' Voice
Brago, King Eternal
Breya, Etherium Shaper
Captain N'ghathrod
Chatterfang, Squirrel General
Chulane, Teller of Tales
Dina, Soul Steeper
Edgar Markov
Esika, God of the Tree
Feather, the Redeemed
Galea, Kindler of Hope
Ghyrson Starn, Kelermorph
Giada, Font of Hope
Gishath, Sun's Avatar
Go-Shintai of Life's Origin
Henzie "Toolbox" Torre
Hinata, Dawn-Crowned
Ikra Shidiqi, the Usurper
Ishai, Ojutai Dragonspeaker
Isshin, Two Heavens as One
Jeska, Thrice Reborn
Jetmir, Nexus of Revels
Jodah, Archmage Eternal
Jodah, the Unifier
K'rrik, Son of Yawgmoth
Kaalia of the Vast
Kalamax, the Stormsire
Kenrith, the Returned King
Kess, Dissident Mage
Kinnan, Bonder Prodigy
Kodama of the East Tree
Korvold, Fae-Cursed King
Kozilek, the Great Distortion
Krark, the Thumbless
Kraum, Ludevic's Opus
Krenko, Mob Boss
Kykar, Wind's Fury
Lathril, Blade of the Elves
Liesa, Shroud of Dusk
Light-Paws, Emperor's Voice
Lord Windgrace
Magda, Brazen Outlaw
Malcolm, Keen-Eyed Navigator
Marchesa, the Black Rose
Marrow-Gnawer
Meren of Clan Nel Toth
Miirym, Sentinel Wyrm
Morophon, the Boundless
Muldrotha, the Gravetide
Myrkul, Lord of Bones
Najeela, the Blade-Blossom
Nekusar, the Mindrazer
Niv-Mizzet, Parun
Obeka, Brute Chronologist
Oloro, Ageless Ascetic
Omnath, Locus of Creation
Orvar, the All-Form
Osgir, the Reconstructor
Prosper, Tome-Bound
Queen Marchesa
Ramos, Dragon Engine
Rin and Seri, Inseparable
Rograkh, Son of Rohgahh
Sakashima of a Thousand Faces
Satoru Umezawa
Sefris of the Hidden Ways
Shorikai, Genesis Engine
Silas Renn, Seeker Adept
Sisay, Weatherlight Captain
Syr Gwyn, Hero of Ashvale
Sythis, Harvest's Hand
Tana, the Bloodsower
Tergrid, God of Fright
Tevesh Szat, Doom of Fools
Teysa Karlov
The First Sliver
The Scarab God
The Ur-Dragon
Thrasios, Triton Hero
Tovolar, Dire Overlord
Tymna the Weaver
Urza, Lord High Artificer
Veyran, Voice of Duality
Vial Smasher the Fierce
Volo, Guide to Monsters
Wilhelt, the Rotcleaver
Winota, Joiner of Forces
Yarok, the Desecrated
Yuriko, the Tiger's Shadow
Zaxara, the Exemplary
Zur the Enchanter
""".strip().split("\n")


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

def recommended_cards(mine, commander):
    cards = set(get_edhrec_commander_analysis(commander, format="basic"))
    owned_cards = set(mine.Name)
    got_em = owned_cards.intersection(cards)
    full_df = mine[mine["Name"].isin(got_em)]
    full_df["Price"] = full_df["Price"].str[1:].astype(float)
    full_df = full_df.drop_duplicates(subset=["Name"])
    price = full_df["Price"].sum()
    return {"Number": len(got_em), "Price": price, "Cards": got_em}

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
