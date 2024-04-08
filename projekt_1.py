'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jitka Mazankova
email: jmazankova@csas.cz
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
];

num_lowercase = 0
num_uppercase = 0
num_title = 0
sum_numeric = 0
num_words = 0
num_numeric = 0


i = 0
for text in TEXTS:
    print(str(i) + ": " + text + "\n")
    i = i + 1
    
vstup = input("Vyber jeden z nasledujicich textu ciselnou volbou\n")

print("Vybral/a jste volbu c." + vstup);

if vstup.isnumeric():
    cislo_odstavce = int(vstup)
    if cislo_odstavce >= 0 and cislo_odstavce < 3:
        seznam_slov = TEXTS[cislo_odstavce].split()
        for slovo in seznam_slov:
            if slovo.isnumeric():
               sum_numeric = sum_numeric + int(slovo)
               num_numeric = num_numeric + 1 
            if slovo.isupper():
                num_uppercase = num_uppercase + 1 
            if slovo.islower():
                num_lowercase = num_lowercase + 1
            if slovo.istitle():
                num_title = num_title + 1
            num_words = num_words + 1
        
        # počet slov,
        print ("".ljust(num_words, "*"), num_words)
        # počet slov začínajících velkým písmenem,
        print ("".ljust(num_title, "*"), num_title)
        # počet slov psaných velkými písmeny,
        print ("".ljust(num_uppercase, "*"), num_uppercase)
        # počet slov psaných malými písmeny,
        print ("".ljust(num_lowercase, "*"), num_lowercase)
        # počet čísel (ne cifer),
        print ("".ljust(num_numeric, "*"), num_numeric)
        # sumu všech čísel (ne cifer) v textu.
        print (sum_numeric)
        print("ok")
    else:
        print("ko")
else:
    print("nebrat")