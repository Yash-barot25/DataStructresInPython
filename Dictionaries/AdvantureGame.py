Locations = {0: "You'r standing front of your computer learning python",
             1: "You'r at your home 430 mcmurchy south ave",
             2: "You'r at tuckshop of brampton towers",
             3: "You'r in garden",
             4: "You'r inside of shopper's drug-mart",
             5: "You'r at 440 mcmurchy eve "}

exits = {0: {"Q": 0},
         1: {"N": 4, "S": 5, "E": 3, "W": 2, "Q": 0},
         2: {"N": 4, "S": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"W": 2, "S": 1, "Q": 0},
         5: {"E": 3, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "WEST": "W",
              "EAST": "E",
              "SOUTH": "S",
              "NORTH": "N"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # availableExits = ""
    # for location in exits[loc].keys():
    #     availableExits += location + ", "

    print(Locations[loc])

    if loc == 0:
        break

    description = input("Available exits are " + availableExits + " => ").upper()
    if len(description) > 1:
        for word in vocabulary:
            if word in description:
                description = vocabulary[word]

    if description in exits[loc]:
        loc = exits[loc][description]
    else:
        print("You can't go in that direction")
