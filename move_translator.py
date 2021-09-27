'''
Translates chess.com move notation into string that arduino can use to make a
move.

ZacharyHeras, May 24th, 2021

'''

## Use dictionary to define each square
## Determine move string length to categorize it into a read-type
## Figure out what piece is moving where
## If piece is moving into occupied square, remove other piece
## Place piece into new square location

# Defines all of the positions on the board with pieces in starting positions
# positions = {
#     "1": "R", # A8
#     "2": "N", # B8
#     "3": "B", # C8
#     "4": "Q", # D8
#     "5": "K", # E8
#     "6": "B", # F8
#     "7": "N", # G8
#     "8": "R", # H8
#
#     "9": "P",  # A7
#     "10": "P", # B7
#     "11": "P", # C7
#     "12": "P", # D7
#     "13": "P", # E7
#     "14": "P", # F7
#     "15": "P", # G7
#     "16": "P", # H7
#
#     "17": "-",
#     "18": "-",
#     "19": "-",
#     "20": "-",
#     "21": "-",
#     "22": "-",
#     "23": "-",
#     "24": "-",
#
#     "25": "-",
#     "26": "-",
#     "27": "-",
#     "28": "-",
#     "29": "-",
#     "30": "-",
#     "31": "-",
#     "32": "-",
#
#     "33": "-",
#     "34": "-",
#     "35": "-",
#     "36": "-",
#     "37": "-",
#     "38": "-",
#     "39": "-",
#     "40": "-",
#
#     "41": "-",
#     "42": "-",
#     "43": "-",
#     "44": "-",
#     "45": "-",
#     "46": "-",
#     "47": "-",
#     "48": "-",
#
#     "49": "P",
#     "50": "P",
#     "51": "P",
#     "52": "P",
#     "53": "P",
#     "54": "P",
#     "55": "P",
#     "56": "P",
#
#     "57": "R",
#     "58": "N",
#     "59": "B",
#     "60": "Q",
#     "61": "K",
#     "62": "B",
#     "63": "N",
#     "64": "R"
#
# }



print("enter chess.com notation")

moveNotation = input()

# Handels pawn moves when there is only one possible pawn for move
if (moveNotation[0].islower()):
    for i in range(0, 9):
        if (positions.get(8) == P):
            moveNotation
else:
    print(moveNotation[0])

print(moveNotation)
