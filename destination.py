def destinations(key):
    country = {'Canada':["CN Tower","Parliament Hill","Banff National Park","Niagara Falls"], 
           'India':["Mumbai", "Jaipur", "Taj Mahal", "Ranthambore National Park"],
           'China':["Great Wall", "Forbidden City", "Tiananmen Square", "Temple of Heaven"],
           'USA':["Grand Canyon", "Yosemite National Park", "Lake Tahoe", "Golden Gate Bridge"],
           'Russia':["State Hermitage Museum", "St. Basil's Cathedral", "The Moscow Kremlin", "Red Square"],
           'Spain':["La Sagrada Familia", "Park Guell", "Alhambra", "Museo Nacional de Prado"],
           'Thailand':["The Grand Palace", "Wat Arun Ratchawararam Ratchaworamahawihan","Railay Beach","Chatuchak Weekend Market"],
           'Australia':["Great Barrier Reef", "Sydney Opera House", "Uluru", "Kakadu National Park"],
           'Egypt':["The Egyptian Museum", "Valley of the Kings", "Karmak", "Great Sphinx of Giza"],
           'South Africa':["Kruger National Park", "Maclear's Beacon", "KirstenBosch National Botanical Garden", "Boulder's Beach"],
           'Mexico':["Chichen Itza", "Tulum Archaeological Zone", "Frida Kahlo Museum", "Xcaret Park"],
           'Brazil':["Christ the Redeemer", "Sugarloaf Mountain","Museum of Art of Sao Paulo Assis Chateaubriand", "Copacabana Beach"],
           'Saudi Arabia':["Masjid al-Haram", "Abraj Al-Bait Towers", "Center Point", "Masmak Fortress"],
           'Ethiopia':["Simien Mountains National Park", "Rock-Hewn Churches, Lalibela", "Blue Nile Falls", "Bale Mountains National Park"]}

    print("Tourist Attractions in", key, ":", country[key])
