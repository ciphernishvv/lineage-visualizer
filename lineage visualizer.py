# LINEAGE VISUALIZER - PYTHON PROJECT
# Console Based Version

# ---------------- DATABASE ---------------- #

surnames_db = {
    "patel": {
        "branches": {
            "Gujarat Patidars": [
                (1000, "Gujarat", "Agricultural landowners"),
                (1400, "Rajasthan", "Trade migration"),
                (1800, "Maharashtra", "Expansion during Maratha rule"),
                (2000, "USA, UK, Canada", "Modern global diaspora")
            ]
        },
        "info": """
Meaning: Village headman
Origin: Gujarat
Community: Patidar
Patels historically managed agricultural lands.
Large migration during 19th and 20th centuries.
"""
    },
    "sinha": {
    "branches": {
        "Kayastha Families": [
            (1200, "Bihar", "Administrative scribes"),
            (1600, "Bengal", "Court officials"),
            (1800, "Kolkata", "British administration"),
            (2000, "Urban India", "Professional migration")
        ]
    },
    "info": "Common among Kayastha community in Bihar and Bengal."
},

"das": {
    "branches": {
        "Devotional Usage": [
            (1000, "Bengal", "Vaishnav devotion"),
            (1500, "Odisha", "Temple services"),
            (1800, "Assam", "Regional expansion"),
            (2000, "Eastern India", "Very widespread")
        ]
    },
    "info": "Means 'servant of God'. Common in Bengal and Odisha."
},

"dutta": {
    "branches": {
        "Bengali Kayasthas": [
            (1200, "Bengal", "Administrative families"),
            (1600, "Dhaka", "Trade expansion"),
            (1800, "Kolkata", "Urban elites"),
            (2000, "India & Abroad", "Global presence")
        ]
    },
    "info": "Common Bengali surname among Kayasthas."
},

"banerjee": {
    "branches": {
        "Bengali Brahmins": [
            (1000, "West Bengal", "Priestly families"),
            (1500, "Nadia", "Scholars"),
            (1800, "Kolkata", "Education roles"),
            (2000, "Global", "Professional diaspora")
        ]
    },
    "info": "Anglicized form of Bandopadhyay. Bengali Brahmin surname."
},
    "shah": {
    "branches": {
        "Jain & Vaishya Traders": [
            (1000, "Gujarat", "Merchant families"),
            (1500, "Rajasthan", "Trade links"),
            (1800, "Mumbai", "Business expansion"),
            (2000, "Global", "Strong diaspora")
        ]
    },
    "info": "Common among Jain and Vaishya communities."
},

"mehta": {
    "branches": {
        "Administrative Title": [
            (1200, "Gujarat", "Revenue officials"),
            (1600, "Rajasthan", "Court service"),
            (1800, "Bombay", "Finance roles"),
            (2000, "India & Abroad", "Urban professionals")
        ]
    },
    "info": "Originally a title meaning accountant or minister."
},

"desai": {
    "branches": {
        "Land Revenue Officers": [
            (1300, "Gujarat", "Village chiefs"),
            (1700, "Maharashtra", "Administrative roles"),
            (1800, "Bombay Presidency", "Regional governance"),
            (2000, "Global", "Modern professionals")
        ]
    },
    "info": "Title used for village headmen and revenue collectors."
},

"trivedi": {
    "branches": {
        "Brahmin Scholars": [
            (1000, "Gujarat", "Vedic scholars"),
            (1500, "Rajasthan", "Religious service"),
            (1800, "Central India", "Temple priests"),
            (2000, "Urban India", "Academic migration")
        ]
    },
    "info": "Means 'knower of three Vedas'. Brahmin surname."
},
    "patil": {
    "branches": {
        "Village Chiefs": [
            (1200, "Maharashtra", "Local administrators"),
            (1600, "Maratha Empire", "Military officers"),
            (1800, "Deccan", "Agricultural heads"),
            (2000, "India & Abroad", "Common surname")
        ]
    },
    "info": "Title for village headman in Maharashtra."
},

"deshmukh": {
    "branches": {
        "Regional Chiefs": [
            (1400, "Deccan", "Tax collection"),
            (1600, "Maratha rule", "Administrative officers"),
            (1800, "British India", "Landholders"),
            (2000, "Urban India", "Widespread")
        ]
    },
    "info": "Means chief of a district."
},

"pawar": {
    "branches": {
        "Maratha Clan": [
            (1300, "Maharashtra", "Warrior families"),
            (1700, "Maratha Empire", "Military roles"),
            (1800, "Central India", "Expansion"),
            (2000, "Across India", "Common surname")
        ]
    },
    "info": "Maratha clan surname."
},

"kulkarni": {
    "branches": {
        "Village Accountants": [
            (1200, "Maharashtra", "Record keepers"),
            (1600, "Deccan Sultanates", "Administrative service"),
            (1800, "British era", "Clerical roles"),
            (2000, "India & Abroad", "Professional migration")
        ]
    },
    "info": "Traditional village accountant title."
},
    "gill": {
    "branches": {
        "Jat Sikh Clan": [
            (1200, "Punjab", "Agricultural clan"),
            (1600, "Majha region", "Local leadership"),
            (1800, "British Punjab", "Military recruitment"),
            (2000, "Canada, UK", "Strong diaspora")
        ]
    },
    "info": "Common Jat Sikh surname in Punjab."
},

"sidhu": {
    "branches": {
        "Jat Clan": [
            (1300, "Punjab", "Warrior-agricultural clan"),
            (1700, "Sikh Confederacy", "Military roles"),
            (1800, "Punjab region", "Landowners"),
            (2000, "Global", "Large overseas migration")
        ]
    },
    "info": "Prominent Jat clan surname in Punjab."
},

"sandhu": {
    "branches": {
        "Punjab Clan": [
            (1200, "Punjab", "Agricultural community"),
            (1600, "Doaba region", "Local expansion"),
            (1800, "British India", "Army service"),
            (2000, "UK, Canada", "Diaspora presence")
        ]
    },
    "info": "Widely found Sikh surname in Punjab."
},

"brar": {
    "branches": {
        "Malwa Clan": [
            (1400, "Punjab (Malwa)", "Farming community"),
            (1700, "Sikh rule", "Military participation"),
            (1800, "Punjab", "Landholders"),
            (2000, "India & Abroad", "Migration abroad")
        ]
    },
    "info": "Jat Sikh clan surname mainly in Malwa region."
},
    "rathore": {
    "branches": {
        "Rajput Clan": [
            (1200, "Marwar", "Rajput rulers"),
            (1500, "Rajasthan", "Kingdom expansion"),
            (1800, "North India", "Noble families"),
            (2000, "Across India", "Widely present")
        ]
    },
    "info": "Major Rajput clan of Rajasthan."
},

"sisodia": {
    "branches": {
        "Mewar Dynasty": [
            (1200, "Mewar", "Royal lineage"),
            (1500, "Udaipur", "Rajput resistance"),
            (1800, "Rajasthan", "Regional nobility"),
            (2000, "India", "Clan descendants")
        ]
    },
    "info": "Rajput clan of Mewar region."
},

"shekhawat": {
    "branches": {
        "Shekhawati Rajputs": [
            (1400, "Shekhawati", "Local rulers"),
            (1600, "Rajasthan", "Fort governance"),
            (1800, "Jaipur state", "Administrative service"),
            (2000, "Across India", "Common Rajput surname")
        ]
    },
    "info": "Rajput clan from Shekhawati region."
},

"tanwar": {
    "branches": {
        "Tomar/Tanwar Lineage": [
            (1100, "Delhi region", "Early rulers"),
            (1400, "Rajasthan", "Clan settlements"),
            (1800, "North India", "Agricultural groups"),
            (2000, "India", "Widespread surname")
        ]
    },
    "info": "Associated with Tomar Rajput lineage."
},
    "reddy": {
    "branches": {
        "Andhra Landholders": [
            (1200, "Andhra Pradesh", "Local chieftains"),
            (1500, "Deccan", "Military service"),
            (1800, "Madras Presidency", "Agricultural elites"),
            (2000, "India & USA", "Professional diaspora")
        ]
    },
    "info": "Common surname in Andhra Pradesh and Telangana."
},

"rao": {
    "branches": {
        "Title Usage": [
            (1300, "Deccan", "Royal title"),
            (1600, "South India", "Administrative officers"),
            (1800, "Mysore & Hyderabad", "Regional service"),
            (2000, "Across India", "Common surname")
        ]
    },
    "info": "Title meaning king or chief, later became surname."
},

"nair": {
    "branches": {
        "Kerala Community": [
            (1200, "Kerala", "Warrior-noble class"),
            (1600, "Travancore", "Military service"),
            (1800, "Kerala", "Landholding community"),
            (2000, "India & Gulf", "Migration abroad")
        ]
    },
    "info": "Prominent community surname in Kerala."
},

"iyer": {
    "branches": {
        "Tamil Brahmins": [
            (1000, "Tamil Nadu", "Temple priests"),
            (1500, "South India", "Scholars"),
            (1800, "Madras", "Education sector"),
            (2000, "Global", "Professional diaspora")
        ]
    },
    "info": "Tamil Brahmin surname."
},
    "kumar": {
    "branches": {
        "Title Based Usage": [
            (1200, "North India", "Royal title"),
            (1600, "Across India", "Adopted widely"),
            (1800, "British India", "Formal documentation"),
            (2000, "Global", "Very common surname")
        ]
    },
    "info": "Means prince or young man. Very widely used."
},

"raj": {
    "branches": {
        "Title Origin": [
            (1200, "North India", "Royal reference"),
            (1600, "Central India", "Clan usage"),
            (1800, "India", "Adopted as surname"),
            (2000, "Global", "Common modern surname")
        ]
    },
    "info": "Derived from word meaning king or rule."
},

"roy": {
    "branches": {
        "Bengal & North India": [
            (1300, "Bengal", "Landholding families"),
            (1700, "Eastern India", "Administrative roles"),
            (1800, "British India", "Zamindars"),
            (2000, "India & Abroad", "Urban migration")
        ]
    },
    "info": "Derived from word Raja. Common in Bengal."
},

"jain": {
    "branches": {
        "Jain Community": [
            (1000, "Rajasthan", "Merchant families"),
            (1500, "Gujarat", "Trade expansion"),
            (1800, "North India", "Business community"),
            (2000, "Global", "Strong diaspora")
        ]
    },
    "info": "Surname indicating Jain religious community."
},
    "bhawsar": {
    "branches": {
        "Bhavsar Community": [
            (1200, "Gujarat", "Traditional weaving and textile community"),
            (1500, "Rajasthan", "Trade migration"),
            (1800, "Maharashtra", "Cloth merchants"),
            (2000, "India & Abroad", "Urban business families")
        ]
    },
    "info": "Bhavsar (Bhawsar) community traditionally associated with textile and dyeing occupations in Western India."
},

"sachdeva": {
    "branches": {
        "Punjabi Khatri": [
            (1400, "Punjab", "Khatri trading families"),
            (1700, "Lahore region", "Administrative and business roles"),
            (1800, "Delhi", "Migration during colonial era"),
            (2000, "India, UK, Canada", "Post-partition diaspora")
        ]
    },
    "info": "Sachdeva is a Punjabi Khatri surname, many families migrated after the 1947 partition."
},

"abrol": {
    "branches": {
        "Kashmiri/Punjabi Khatri": [
            (1300, "Kashmir", "Scholarly and trading families"),
            (1600, "Punjab", "Migration southward"),
            (1800, "North India", "Business and administration"),
            (2000, "India & Abroad", "Modern diaspora")
        ]
    },
    "info": "Abrol is traditionally linked to Khatri communities of Kashmir and Punjab."
},

"butola": {
    "branches": {
        "Uttarakhand rajput": [
            (1200, "Garhwal", "rajputs"),
            (1500, "Uttarakhand hills", "Village settlements"),
            (1800, "Dehradun", "Administrative roles"),
            (2000, "Delhi & Urban India", "Migration to cities")
        ]
    },
    "info": "Butola surname is commonly found in the Garhwal region of Uttarakhand majorly used by rajput community of uttarakhand. ut."
},

"dhoundiyal": {
    "branches": {
        "Garhwali brahmins": [
            (1200, "Garhwal (Uttarakhand)", "Religious scholars"),
            (1500, "Hill regions", "Temple service"),
            (1800, "Dehradun", "Education roles"),
            (2000, "India & Abroad", "Urban professionals")
        ]
    },
    "info": "Dhoundiyal is a Garhwali Brahmin surname from Uttarakhand."
},

"sahu": {
    "branches": {
        "Trading & Agricultural Communities": [
            (1100, "Eastern India", "Village traders"),
            (1500, "Bihar & Odisha", "Agricultural expansion"),
            (1800, "Central India", "Business communities"),
            (2000, "Across India", "Widely used surname")
        ]
    },
    "info": "Sahu is a common surname in Bihar, Odisha, and Chhattisgarh, often linked to trading communities."
},

"dhariwal": {
    "branches": {
        "Punjabi Clan": [
            (1400, "Punjab", "Agricultural clan"),
            (1700, "Sikh Confederacy", "Military participation"),
            (1800, "British Punjab", "Regional migration"),
            (2000, "India, UK, Canada", "Diaspora presence")
        ]
    },
    "info": "Dhariwal is a jaat community majorly found in haryana."
},

"chaudhary": {
    "branches": {
        "North Indian Landholders": [
            (1200, "Rajasthan", "Revenue collectors"),
            (1500, "Haryana", "Agricultural chiefs"),
            (1800, "Uttar Pradesh", "Village administration"),
            (2000, "Across India", "Widespread surname")
        ],
        "Bihar Branch": [
            (1300, "Bihar", "Zamindari families"),
            (1700, "Eastern India", "Land administration"),
            (1900, "Urban Bihar", "Political roles"),
            (2000, "India", "Common modern surname")
        ]
    },
    "info": "Chaudhary means landholder or revenue officer. Used by multiple communities across North India."
},

"thakur": {
    "branches": {
        "Rajput Usage": [
            (1200, "Rajasthan", "Warrior nobility"),
            (1500, "Central India", "Feudal lords"),
            (1800, "North India", "Landholding families"),
            (2000, "Across India", "Common surname")
        ],
        "Bihar Usage": [
            (1400, "Bihar", "Village chiefs"),
            (1700, "Eastern India", "Agricultural elites"),
            (1900, "Bihar & UP", "Regional influence"),
            (2000, "India", "Widely used title and surname")
        ]
    },
    "info": "Thakur is a title meaning lord or noble. Used by Rajputs and other communities in North India."
},

    "gupta": {
        "branches": {
            "North Indian Guptas": [
                (1000, "Uttar Pradesh", "Trading communities"),
                (1200, "Bihar", "Business settlements"),
                (1600, "Rajasthan", "Mercantile expansion"),
                (2000, "India, USA, UK", "Modern urban diaspora")
            ]
        },
        "info": """
Origin: North India
Associated Community: Vaishya/Bania
Historical Connection: Gupta dynasty period influence
Primarily involved in trade and commerce.
"""
    },

    "jha": {
        "branches": {
            "Maithil Brahmins": [
                (1000, "Mithila (Bihar)", "Scholarly Brahmin community"),
                (1400, "Nepal", "Cultural expansion"),
                (1800, "Kolkata", "Administrative roles"),
                (2000, "Delhi, Mumbai", "Urban migration")
            ]
        },
        "info": """
Origin: Mithila region
Community: Maithil Brahmin
Traditionally scholars and priests.
Strong presence in Bihar and Nepal.
"""
    },

    "chaudhary": {
        "branches": {
            "North Indian Landholders": [
                (1200, "Rajasthan", "Revenue collectors"),
                (1500, "Haryana", "Agricultural chiefs"),
                (1800, "Uttar Pradesh", "Village administration"),
                (2000, "Across India", "Widespread usage")
            ]
        },
        "info": """
Meaning: Landholder / Tax collector
Used by multiple communities across North India.
Represents leadership or administrative authority.
"""
    },

    "saini": {
        "branches": {
            "Northern Agricultural Community": [
                (1000, "Punjab", "Farming community"),
                (1400, "Haryana", "Regional expansion"),
                (1800, "Rajasthan", "Agricultural migration"),
                (2000, "India & Abroad", "Modern mobility")
            ]
        },
        "info": """
Origin: Northern India
Traditionally agricultural background.
Present in Punjab, Haryana, Rajasthan.
"""
    },
"sharma": {
    "branches": {
        "North Indian Brahmins": [
            (1000, "Kashmir", "Scholarly Brahmin families"),
            (1400, "Uttar Pradesh", "Temple and court scholars"),
            (1800, "Delhi", "Administrative services"),
            (2000, "Across India & Abroad", "Urban migration")
        ]
    },
    "info": "Common Brahmin surname across North India. Traditionally priests and scholars."
},

"singh": {
    "branches": {
        "Rajput & Sikh Usage": [
            (1200, "Rajasthan", "Warrior clans"),
            (1500, "Punjab", "Adopted widely"),
            (1800, "North India", "Military service"),
            (2000, "Global", "Very common surname")
        ]
    },
    "info": "Means 'Lion'. Used by Rajputs and widely adopted by Sikhs."
},

"yadav": {
    "branches": {
        "Yaduvanshi Community": [
            (1000, "Mathura", "Krishna lineage traditions"),
            (1400, "Bihar", "Agricultural groups"),
            (1800, "Uttar Pradesh", "Regional expansion"),
            (2000, "Across India", "Political & rural presence")
        ]
    },
    "info": "Associated with Yadu lineage traditions. Common in UP and Bihar."
},

"agarwal": {
    "branches": {
        "Vaishya Traders": [
            (1000, "Haryana", "Agroha region traders"),
            (1400, "Rajasthan", "Mercantile growth"),
            (1800, "Delhi", "Business community"),
            (2000, "Global", "Major business diaspora")
        ]
    },
    "info": "Prominent trading community surname from North India."
},
}
# ---------------- SURNAME EVOLUTION ---------------- #
surname_evolution = {
    "jha": ["Upadhyaya", "Ojha", "Jha"],
    "banerjee": ["Bandopadhyay", "Banerjee"],
    "mukherjee": ["Mukhopadhyay", "Mukherjee"],
    "chatterjee": ["Chattopadhyay", "Chatterjee"],
    "verma": ["Varma", "Verma"],
    "srivastava": ["Shrivastava", "Srivastava"],
    "ojha": ["Upadhyaya", "Ojha"],
    "upadhyaya": ["Upadhyaya"]
}

def get_evolution(surname_input):
    surname_input = surname_input.strip().lower()

    if surname_input in surname_evolution:
        return surname_evolution[surname_input]
    else:
        return ["No record found"]


# ------------- FUNCTION TO PRINT TABLE ------------- #

def print_table(data):
    print("\n{:<10} {:<25} {:<40}".format("Year", "Region", "Notes"))
    print("-" * 75)
    for year, region, notes in data:
        print("{:<10} {:<25} {:<40}".format(year, region, notes))
    print("-" * 75)


# ---------------- MAIN PROGRAM ---------------- #

print("========== LINEAGE VISUALIZER ==========")
print("\nDisclaimer:")
print("This project shows surname evolution based on available historical and cultural references.")
print("It may not represent exact genealogical or caste lineage.")
print("Data is for educational and visualization purposes only.\n")

surname_input = input("Enter your surname: ").lower()
result = get_evolution(surname_input)
print("Evolution:", " → ".join(result))

if surname_input in surnames_db:
    surname_data = surnames_db[surname_input]

    print("\nMigration History Found!")

    branches = surname_data["branches"]

    # If multiple branches exist
    if len(branches) > 1:
        print("\nMultiple historical branches found for this surname.\n")

    for branch_name, migration_data in branches.items():
        print(f"\nBranch: {branch_name}")
        print_table(migration_data)

    # Ask for more info
    more_info = input("\nDo you want more information about this surname? (yes/no): ").lower()

    if more_info == "yes":
        print("\n===== Detailed Information =====")
        print(surname_data["info"])
    else:
        print("\nThank you for using Lineage Visualizer!")

else:
    print("\nSurname not found in database.")
    print("Try another surname.")

print("\n========== PROGRAM END ==========")
