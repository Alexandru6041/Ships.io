from game_elements.question import Question

DEFAULT_SIZE = 3072
TIME_LIMIT = 30
Question_List = [
            Question("In ce tara s-a nascut Albert Hitler", ["Germania", "Austria", "Elvetia"], 1),
            Question("Cate zile are un an bisect", ["366", "365", "354"], 0),
            Question("Care este cel mai mare mamifer din lume?", ["Leul", "Elefantul", "Balena"], 2),
            Question("De unde izvoraste Dunarea", ["Germania", "Romania", "Ungaria"], 0),
            Question("Care este capitala Egiptului", ["Cairo", "Alexandria", "Asyut"], 0),
            Question("Cati ani a durat Razboiul de 100 de ani", ["100", "99", "116"], 2),
            Question("Care este cel mai rapid animal din lume", ["Ghepardul", "Hiena", "Leul"], 0),
            Question("Care este cel mai lung fluviu din Europa", ["Dunarea", "Volga", "Nil"], 1),
            Question("Cate state are Statele Unite ale Americii", ["46", "50", "61"], 1),
            Question("Care este capitala Islandei?", ["Berlin", "Dublin", "Reykjavik"], 2),
            Question("Care este cel mai inalt varf de munte de pe Terra", ["Kilimanjaro", "Everest", "Moldoveanu"], 1),
            Question("Ce echipa a castigat Liga Campionilor in 2012", ["Chelsea", "Barcelona", "Real Madrid"], 1),
            Question("Cate laturi are un hexagon", ["5", "6", "8"], 1),
            Question("Care este cea mai mare padure tropicala din lume", ["Amazon", "Daintree", "Kinabalu"], 0),
            Question("Care este cel mai selectionat jucator din istoria nationalei de fotbal a Romaniei", ["Gica Hagi", "Lionel Messi", "Dorinel Munteanu"], 2),
            Question("Cati ani are un deceniu", ["10", "12", "100"], 0),
            Question("Cine a exclamat 'Evrika'", ["Aristotel", "Arhimede", "Platon"], 0),
            Question("Care este continentul pe care nu traiesc ursi", ["Australia", "Africa", "Antartica"], 2),
            Question("Ce culoare are cutia neagra a unui avion", ["Neagra", "Rosie", "Portocalie"], 2),
            Question("In ce an a fost infiintata ONU", ["2007", "1989", "1947"], 2),
            Question("Cine a scris Odiseea", ["Platon", "Homer", "Mihai Eminescu"], 1),
            Question("Care este cea mai mare planeta din Sistemul Solar", ["Mercur", "Pluto", "Jupiter"], 2),
            Question("Cine a fost primul om pe Luna in 1969", ["Neil Armstrong", "Garry Kasparov", "Dumitru Prunariu"], 0),
            Question("Cine a pictat 'Mona Lisa'", [], ),
            Question("Care este cartea sacra a religiei iudaice", ["Evanghelia", "Tora", "Coranul"], 1),
            Question("Care a fost capitala Imperiului Roman", ["Constantinopol", "Roma", "Bucuresti"], 1),
            Question("Cine a sculptat statuia David", ["Michelangelo", "Leonardo Da Vinci", "Constantin Brancoveanu"], 0),
            Question("Care a fost capitala Moldovei", ["Galati", "Barlad", "Iasi"], 2),
            Question("Cine a fost primul om care a ajuns pe Everest", ["Edmund Hillary", "Tenzing Norgay", "George Mallory"], 0),
            Question("Care este cel mai mare oras din Romania", ["Bucuresti", "Cluj-Napoca", "Timisoara"], 0)
    ]

TARGET_AREA = (4, 4)
KILLSIGNAL = '!KILL'
OK_MESSAGE = '!O'