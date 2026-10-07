"""New York's 62 counties with county seat and OPWDD region / regional office.
Sources: OPWDD regional maps and DDRO county lists (opwdd.ny.gov/opwdd-maps)."""

# (county, seat, OPWDD region number, regional office)
NY_COUNTIES = [
    # Region 3 - Capital District office
    ("Albany", "Albany", 3, "Capital District"), ("Fulton", "Johnstown", 3, "Capital District"),
    ("Montgomery", "Fonda", 3, "Capital District"), ("Rensselaer", "Troy", 3, "Capital District"),
    ("Saratoga", "Ballston Spa", 3, "Capital District"), ("Schenectady", "Schenectady", 3, "Capital District"),
    ("Schoharie", "Schoharie", 3, "Capital District"), ("Warren", "Queensbury", 3, "Capital District"),
    ("Washington", "Fort Edward", 3, "Capital District"),
    # Region 3 - Taconic office
    ("Columbia", "Hudson", 3, "Taconic"), ("Dutchess", "Poughkeepsie", 3, "Taconic"),
    ("Greene", "Catskill", 3, "Taconic"), ("Putnam", "Carmel", 3, "Taconic"), ("Ulster", "Kingston", 3, "Taconic"),
    # Region 3 - Hudson Valley office
    ("Orange", "Goshen", 3, "Hudson Valley"), ("Rockland", "New City", 3, "Hudson Valley"),
    ("Sullivan", "Monticello", 3, "Hudson Valley"), ("Westchester", "White Plains", 3, "Hudson Valley"),
    # Region 2 - Sunmount (North Country)
    ("Clinton", "Plattsburgh", 2, "Sunmount (North Country)"), ("Essex", "Elizabethtown", 2, "Sunmount (North Country)"),
    ("Franklin", "Malone", 2, "Sunmount (North Country)"), ("Hamilton", "Lake Pleasant", 2, "Sunmount (North Country)"),
    ("Jefferson", "Watertown", 2, "Sunmount (North Country)"), ("St. Lawrence", "Canton", 2, "Sunmount (North Country)"),
    # Region 2 - Central New York
    ("Cayuga", "Auburn", 2, "Central New York"), ("Cortland", "Cortland", 2, "Central New York"),
    ("Herkimer", "Herkimer", 2, "Central New York"), ("Lewis", "Lowville", 2, "Central New York"),
    ("Madison", "Wampsville", 2, "Central New York"), ("Oneida", "Utica", 2, "Central New York"),
    ("Onondaga", "Syracuse", 2, "Central New York"), ("Oswego", "Oswego", 2, "Central New York"),
    # Region 2 - Broome
    ("Broome", "Binghamton", 2, "Broome"), ("Chenango", "Norwich", 2, "Broome"), ("Delaware", "Delhi", 2, "Broome"),
    ("Otsego", "Cooperstown", 2, "Broome"), ("Tioga", "Owego", 2, "Broome"), ("Tompkins", "Ithaca", 2, "Broome"),
    # Region 1 - Finger Lakes
    ("Chemung", "Elmira", 1, "Finger Lakes"), ("Livingston", "Geneseo", 1, "Finger Lakes"),
    ("Monroe", "Rochester", 1, "Finger Lakes"), ("Ontario", "Canandaigua", 1, "Finger Lakes"),
    ("Schuyler", "Watkins Glen", 1, "Finger Lakes"), ("Seneca", "Waterloo", 1, "Finger Lakes"),
    ("Steuben", "Bath", 1, "Finger Lakes"), ("Wayne", "Lyons", 1, "Finger Lakes"),
    ("Wyoming", "Warsaw", 1, "Finger Lakes"), ("Yates", "Penn Yan", 1, "Finger Lakes"),
    # Region 1 - Western New York
    ("Allegany", "Belmont", 1, "Western New York"), ("Cattaraugus", "Little Valley", 1, "Western New York"),
    ("Chautauqua", "Mayville", 1, "Western New York"), ("Erie", "Buffalo", 1, "Western New York"),
    ("Genesee", "Batavia", 1, "Western New York"), ("Niagara", "Lockport", 1, "Western New York"),
    ("Orleans", "Albion", 1, "Western New York"),
    # Region 4 - New York City
    ("Bronx", "The Bronx", 4, "Metro NY"), ("Kings", "Brooklyn", 4, "Brooklyn"),
    ("New York", "Manhattan", 4, "Metro NY"), ("Queens", "Queens", 4, "Bernard M. Fineson"),
    ("Richmond", "Staten Island", 4, "Staten Island"),
    # Region 5 - Long Island
    ("Nassau", "Mineola", 5, "Long Island"), ("Suffolk", "Riverhead", 5, "Long Island"),
]
REGION_NAMES = {1: "Region 1: Western New York and Finger Lakes", 2: "Region 2: Central New York, Broome and North Country",
                3: "Region 3: Capital District, Taconic and Hudson Valley", 4: "Region 4: New York City", 5: "Region 5: Long Island"}
NYC_NAMES = {"Bronx": "The Bronx", "Kings": "Brooklyn", "New York": "Manhattan", "Queens": "Queens", "Richmond": "Staten Island"}

# Where Spectrum Arch expects to meet families in person (Clifton Park base).
PRIMARY = {"Albany", "Fulton", "Montgomery", "Rensselaer", "Saratoga", "Schenectady", "Schoharie", "Warren", "Washington", "Columbia", "Greene"}
CDTA = {"Albany", "Rensselaer", "Saratoga", "Schenectady"}
TOWNS = {
    "Saratoga": "Saratoga Springs, Clifton Park, Halfmoon, Malta, Ballston Spa, Wilton, Mechanicville, and Waterford",
    "Albany": "Albany, Colonie, Latham, Guilderland, Bethlehem, Delmar, Cohoes, and Watervliet",
    "Schenectady": "Schenectady, Niskayuna, Glenville, Scotia, and Rotterdam",
    "Rensselaer": "Troy, Rensselaer, East Greenbush, North Greenbush, and Brunswick",
    "Warren": "Glens Falls, Queensbury, and Lake George",
    "Washington": "Hudson Falls, Fort Edward, Greenwich, and Granville",
    "Columbia": "Hudson, Chatham, Kinderhook, and Valatie",
    "Greene": "Catskill, Coxsackie, and Cairo",
    "Fulton": "Gloversville and Johnstown",
    "Montgomery": "Amsterdam and Fonda",
    "Schoharie": "Cobleskill and Schoharie",
}
# Front Door phone numbers confirmed on OPWDD materials; other offices link to OPWDD's contact page.
FRONT_DOOR = {"Capital District": "518-388-0398", "Taconic": "518-388-0398", "Hudson Valley": "845-947-6390"}

def slug(county):
    return county.lower().replace(".", "").replace(" ", "-") + "-county"
