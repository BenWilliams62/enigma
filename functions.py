# enigma machine

# input
def input_message():
    message = str(input("input message:\n")).lower()
    return message

# plug board
def plug(char, plug_board):
    return plug_board[char]

# rotor function
def rotor_function(char, step, direction, switcher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.index(char)
    if direction == "f":
        val = ((index + int(step)) + 26) % 26
        return switcher[alphabet[val]]
    else:
        for k, v in switcher.items():
            if v == char:
                index_k = alphabet.index(k)
                return alphabet[(index_k - int(step) + 26) % 26]

# reflector - find index of letter, then return opposite (25 - index)
def reflect(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.index(char)
    reflection = 25 - index
    return alphabet[reflection]