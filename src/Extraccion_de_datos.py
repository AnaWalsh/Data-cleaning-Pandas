import pandas as pd
import numpy as np
from numpy import nan
import re



def clean_countries (string):

    """
    This function cleans the variable Country:
    Arggs:
    - Strings in variable Year.
    Returns:
        a) List of continents where the countries in the string given where found.
        b) Unknown if the country is not found in any continen list given.
    """
    
    Africa = ["AFRICA","ALGERIA","ANGOLA","BENIN","BOTSWANA","BURKINA FASO", "BURUNDI","CAPE VERDE",
          "CAMEROON", "CENTRAL AFRICAN REPUBLIC","CHAD","COMOROS","CONGO",
          "DEMOCRATIC REPUBLIC OF THE","CONGO, REPUBLIC OF THE","COTE D'IVOIRE",
          "DJIBOUTI","EGYPT","EQUATORIAL GUINEA","ERITREA","ESWATINI","ETHIOPIA",
          "GABON","GAMBIA","GHANA","GUINEA","GUINEA-BISSAU","KENYA","LESOTHO","LIBERIA",
          "LIBYA","MADAGASCAR","MALAWI","MALI","MAURITANIA","MAURITIUS","MOROCCO","MOZAMBIQUE",
          "NAMIBIA","NIGER","NIGERIA","RWANDA","SAO TOME AND PRINCIPE","SENEGAL","SEYCHELLES",
          "SIERRA LEONE","SOMALIA", "SOUTH AFRICA","SOUTH SUDAN","SUDAN","TANZANIA","TOGO",
          "TUNISIA","UGANDA","ZAMBIA","ZIMBABWE",]

    Asia = ["ASIA","AFGHANISTAN","ARMENIA","AZERBAIJAN","BAHRAIN","BANGLADESH","BHUTAN","BRUNEI",
            "CAMBODIA","CHINA","CYPRUS","EAST TIMOR","EGYPT","GEORGIA","INDIA","INDONESIA","IRAN",
            "IRAQ","ISRAEL","JAPAN","JORDAN","KAZAKHSTAN","KUWAIT","KYRGYZSTAN","LAOS","LEBANON",
            "MALAYSIA","MALDIVES","MONGOLIA","MYANMAR","NEPAL","NORTH KOREA","OMAN","PAKISTAN",
            "PALESTINE","PHILIPPINES","QATAR","RUSSIA","SAUDI ARABIA","SINGAPORE","SOUTH KOREA",
            "SRI LANKA","SYRIA","TAIWAN","TAJIKISTAN","THAILAND","TURKEY","TURKMENISTAN",
            "UNITED ARAB EMIRATES","UZBEKISTAN","VIETNAM","YEMEN"]

    Oceania = ["OCEANIA","AUSTRALIA", "FIJI", "KIRIBATI", "MARSHALL ISLANDS","MICRONESIA","NAURU",
               "NEW ZEALAND", "PALAU","PAPUA NEW GUINEA","SAMOA","SOLOMON ISLANDS",
               "TONGA","TUVALU","VANUATU"]

    Europe = ["EUROPE","ALBANIA","ANDORRA","ARMENIA","AUSTRIA","AZERBAIJAN","BELARUS","BELGIUM",
              "BOSNIA AND HERZEGOVINA", "BULGARIA","CROATIA","CYPRUS","CZECHIA","DENMARK",
              "ESTONIA","FINLAND","FRANCE","GEORGIA","GERMANY","GREECE","HUNGARY","ICELAND",
              "IRELAND","ITALY","KAZAKHSTAN","KOSOVO","LATVIA","LIECHTENSTEIN","LITHUANIA",
              "LUXEMBOURG","MALTA","MOLDOVA","MONACO","MONTENEGRO","NETHERLANDS","NORTH MACEDONIA",
              "NORWAY","POLAND","PORTUGAL","ROMANIA","RUSSIA","SAN MARINO","SERBIA","SLOVAKIA",
              "SLOVENIA","SPAIN","SWEDEN","SWITZERLAND","TURKEY","UKRAINE","UNITED KINGDOM",
              "VATICAN CITY"]

    North_America = ["NORTH AMERICA","ANTIGUA AND BARBUDA", "BAHAMAS", "BARBADOS", "BELIZE", "CANADA", 
                     "COSTA RICA","CUBA", "DOMINICA", "DOMINICAN REPUBLIC", "EL SALVADOR",
                     "GRENADA", "GUATEMALA", "HAITI", "HONDURAS", "JAMAICA", "MEXICO",
                     "NICARAGUA", "PANAMA", "SAINT KITTS AND NEVIS","SAINT LUCIA",
                     "SAINT VINCENT AND THE GRENADINES", "TRINIDAD AND TOBAGO",
                     "USA"]

    South_America = ["SOUTH AMERICA","ARGENTINA","BOLIVIA","BRAZIL","CHILE","COLOMBIA","ECUADOR","GUYANA"
                     ,"PARAGUAY","PERU","SURINAME","URUGUAY","VENEZUELA"]
    
    string = string.upper().strip()

    if string in Africa:
        return "Africa"
    elif string in Asia:
        return "Asia"
    elif string in Europe:
        return "Europe"
    elif string in Oceania:
        return "Oceania"
    elif string in North_America:
        return "North America"
    elif string in South_America:
        return "South America"
    elif re.search(r'\bsea|ocean', string, re.IGNORECASE) is not None:
        return "Unknown"
    elif re.search(r'\bisl', string, re.IGNORECASE) is not None:
        return "Unknown"
    else:
        return "Unknown"

def clean_activity(string):

    """
    This function cleans the variable Activity.
    Args:
        - Strings on variable Activity
    Returns:
    - Returns all the new categories in the variable Activity after implemented a regrex patron on them.

    """

    if(re.search(r'\bsurf|paddle|windsurf',string, re.IGNORECASE) != None):
        return "Surf"
    elif(re.search(r'\bpulling|cleaning|spear|washing|crayfish|fish|lobster',string, re.IGNORECASE) != None):
        return "Fishing"
    elif(re.search(r'\bphotographing|snorkeling|filming|dive|diving|scuba|diving|feeding',string, re.IGNORECASE) != None):
        return "Diving"
    elif(re.search(r'\bwaist|knee-deep|bathing|swim|float',string, re.IGNORECASE) != None):
        return "Bathing"
    elif(re.search(r'\bfreighter|boat|sank|overboard|wreck|ferry|sunk|sink|founde|submarine',string, re.IGNORECASE) != None):
        return "Sea disaster"
    elif(re.search(r'\bskiing|kayak|rowing|canoe|play|board',string, re.IGNORECASE) != None):
        return "Water sports"
    elif(re.search(r'\bsail|yacht',string, re.IGNORECASE) != None):
        return "Sailing"
    elif(re.search(r'\bcrashed|air|plane',string, re.IGNORECASE) != None):
        return "Plane crash"
    elif(re.search(r'\bshark',string, re.IGNORECASE) != None):
        return "Direct interaction with sharks"
    elif(re.search(r'\binto',string, re.IGNORECASE) != None):
        return "Falls into the sea"
    elif(re.search(r'\badrift',string, re.IGNORECASE) != None):
        return "Adrift"
    elif string == "Unknown":
        return "Unknown"
    else:
        return "Other"

def word_list_count(list):
    """
    This function counts the number of time each word is repeated in the list.
    Args:
        - Strings on variable Species.
    Returns:
    - Returns the a list of all the words in in Species and how many teams it appears on the list.

    """
    counts = dict()
    for pal in list:

        for word in pal.split():
            word = word.lower()
            if(len(word)>3):
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    return counts


def clean_species(string):

    """
    This function cleans the variable Species.
    Args:
        - Strings on variable Species.
    Returns:
    - Returns all the new categories in the variable Species after implemented a regrex patron on them.

    """
    
    if re.search(r'\bwhite', string, re.IGNORECASE) is not None:
        return "White"
    elif re.search(r'\btiger', string, re.IGNORECASE) is not None:
        return "Tiger"
    elif re.search(r'\blemon', string, re.IGNORECASE) is not None:
        return "Lemon"
    elif re.search(r'\bgrey', string, re.IGNORECASE) is not None:
        return "Grey"
    elif re.search(r'\bbull', string, re.IGNORECASE) is not None:
        return "Bull"
    elif re.search(r'\btawny', string, re.IGNORECASE) is not None:
        return "Tawny"
    elif re.search(r'\bwobbegong', string, re.IGNORECASE) is not None:
        return "Wobbegong"
    elif re.search(r'\bblacktip', string, re.IGNORECASE) is not None:
        return "Blacktip"
    elif re.search(r'\bnurse', string, re.IGNORECASE) is not None:
        return "Nurse"
    elif re.search(r'\bblue', string, re.IGNORECASE) is not None:
        return "Blue"
    elif re.search(r'\bcookiecutter', string, re.IGNORECASE) is not None:
        return "Cookiecutter"
    elif re.search(r'\bspinner', string, re.IGNORECASE) is not None:
        return "Spinner"
    elif re.search(r'\bsandtiger', string, re.IGNORECASE) is not None:
        return "Sandtiger"
    elif re.search(r'\bseven', string, re.IGNORECASE) is not None:
        return "Seven"
    elif re.search(r'\bbrown', string, re.IGNORECASE) is not None:
        return "Brown"
    elif re.search(r'\bcarpet', string, re.IGNORECASE) is not None:
        return "Carpet"
    elif re.search(r'\bcaribbean|reef', string, re.IGNORECASE) is not None:
        return "Caribbean"
    elif re.search(r'\bbroadnose', string, re.IGNORECASE) is not None:
        return "Broadnose"
    elif re.search(r'\bangel', string, re.IGNORECASE) is not None:
        return "Angel"
    elif re.search(r'\bdogfish', string, re.IGNORECASE) is not None:
        return "Dogfish"
    elif re.search(r'\bdebris', string, re.IGNORECASE) is not None:
        return "Debris"
    elif re.search(r'\bmako', string, re.IGNORECASE) is not None:
        return "Mako"
    elif re.search(r'\bbronze', string, re.IGNORECASE) is not None:
        return "Bronze"
    elif re.search(r'\bwhaler', string, re.IGNORECASE) is not None:
        return "Whaler"
    elif re.search(r'\bsilky', string, re.IGNORECASE) is not None:
        return "Silky"
    elif re.search(r'\bhammerhead', string, re.IGNORECASE) is not None:
        return "Hammerhead"
    elif re.search(r'\braggedtooth', string, re.IGNORECASE) is not None:
        return "Raggedtooth"
    elif re.search(r'\bgoblin', string, re.IGNORECASE) is not None:
        return "Goblin"
    elif re.search(r'\bwobbegong', string, re.IGNORECASE) is not None:
        return "Wobbegong"
    elif re.search(r'\bporbeagle', string, re.IGNORECASE) is not None:
        return "Porbeagle"
    elif re.search(r'\ballegedly', string, re.IGNORECASE) is not None:
        return "Allegedly"
    elif re.search(r'\bblactip', string, re.IGNORECASE) is not None:
        return "Blactip"
    elif re.search(r'\bzambesi', string, re.IGNORECASE) is not None:
        return "zambesi"
    elif re.search(r'\bthresher', string, re.IGNORECASE) is not None:
        return "Thresher"
    elif re.search(r'\bspurdog', string, re.IGNORECASE) is not None:
        return "Spurdog"
    elif re.search(r'\bdusky', string, re.IGNORECASE) is not None:
        return "Dusky"
    elif re.search(r'\bsmoothhound', string, re.IGNORECASE) is not None:
        return "Smoothhound"
    elif re.search(r'\bbasking', string, re.IGNORECASE) is not None:
        return "Basking"
    elif re.search(r'\bcatshark', string, re.IGNORECASE) is not None:
        return "Catshark"
    elif re.search(r'\bscyliorhinus', string, re.IGNORECASE) is not None:
        return "Scyliorhinus"
    elif re.search(r'\bdogfish', string, re.IGNORECASE) is not None:
        return "Dogfish"
    elif re.search(r'\bcanicula', string, re.IGNORECASE) is not None:
        return "Canicula"
    elif re.search(r'\bcatsharks', string, re.IGNORECASE) is not None:
        return "Catsharks"
    elif re.search(r'\blion', string, re.IGNORECASE) is not None:
        return "Lion"
    elif re.search(r'\banglers', string, re.IGNORECASE) is not None:
        return "Anglers"
    elif re.search(r'\blongfin', string, re.IGNORECASE) is not None:
        return "Longfin"
    elif re.search(r'\bcarcharhinus', string, re.IGNORECASE) is not None:
        return "Archarhinus",
    elif re.search(r'\bshortfin', string, re.IGNORECASE) is not None:
        return "Shortfin"
    elif re.search(r'\bsand', string, re.IGNORECASE) is not None:
        return "Sand"
    elif re.search(r'\bstingray', string, re.IGNORECASE) is not None:
        return "Stingray"
    elif re.search(r'\bbonnethed', string, re.IGNORECASE) is not None:
        return "Bonnethed"
    elif re.search(r'\bleucas', string, re.IGNORECASE) is not None:
        return "Leucas"
    elif re.search(r'\bbamboo', string, re.IGNORECASE) is not None:
        return "Bamboo"
    elif re.search(r'\bblack', string, re.IGNORECASE) is not None:
        return "Blackfin"
    elif re.search(r'\bsoupfin', string, re.IGNORECASE) is not None:
        return "Soupfin"
    elif re.search(r'\bleopard', string, re.IGNORECASE) is not None:
        return "Leopard"
    elif re.search(r'\bnakaya', string, re.IGNORECASE) is not None:
        return "Nakaya"
    elif re.search(r'\bnotchfin', string, re.IGNORECASE) is not None:
        return "Notchfin"
    elif re.search(r'\bgirth', string, re.IGNORECASE) is not None:
        return "Girth"
    elif re.search(r'\bsmale', string, re.IGNORECASE) is not None:
        return "Smale"
    elif re.search(r'\bcopper', string, re.IGNORECASE) is not None:
        return "Copper"
    elif re.search(r'\bshovelnose', string, re.IGNORECASE) is not None:
        return "Shovelnose"
    elif re.search(r'\bvicinity', string, re.IGNORECASE) is not None:
        return "Vicinity"
    elif re.search(r'\bsilvertip', string, re.IGNORECASE) is not None:
        return "Silvertip"
    elif re.search(r'\bzambezi', string, re.IGNORECASE) is not None:
        return "Zambezi"
    elif re.search(r'\bbuttery', string, re.IGNORECASE) is not None:
        return "Buttery"
    elif re.search(r'\bmelanopterus', string, re.IGNORECASE) is not None:
        return "Melanopterus"
    else:
        return "Unknown"     