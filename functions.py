# enigma machine

def plug(char, plug_board):
    return plug_board[char]

# char to number
def char_to_number(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.index(char)
    return index

# number to char
def number_to_char(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num]


# reflector - find index of letter, then return opposite (25 - index)
def reflect(num):
    reflection = 25 - num
    return reflection


# input
def input_message():
    message = str(input("input message:\n")).lower()
    return message

# rotor 1
def rotor_1(char, step, direction):
    # set switcher once and forget it
    switcher = {
        0:2,
        1:4,
        2:6,
        3:8,
        4:10,
        5:12,
        6:14,
        7:16,
        8:18,
        9:20,
        10:22,
        11:24,
        12:1,
        13:3,
        14:5,
        15:7,
        16:9,
        17:11,
        18:13,
        19:15,
        20:17,
        21:19,
        22:21,
        23:23,
        24:25,
        25:0
    }
    if direction == "f":
        val = ((char + step) + 26) % 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                return (k - step + 26) % 26

# rotor 2
def rotor_2(char, step, direction):
    # set switcher once and forget it
    switcher = {
        0:3,
        1:6,
        2:9,
        3:12,
        4:15,
        5:18,
        6:21,
        7:24,
        8:2,
        9:5,
        10:8,
        11:11,
        12:14,
        13:17,
        14:0,
        15:23,
        16:1,
        17:4,
        18:7,
        19:10,
        20:13,
        21:16,
        22:19,
        23:22,
        24:25,
        25:20
    }
    if direction == "f":
        val = ((char + step) + 26) % 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                return (k - step + 26) % 26

# rotor 3
def rotor_3(char, step, direction):
    # set switcher once and forget it
    switcher = {
        0:4,
        1:8,
        2:12,
        3:16,
        4:20,
        5:24,
        6:0,
        7:7,
        8:11,
        9:15,
        10:19,
        11:23,
        12:2,
        13:6,
        14:10,
        15:14,
        16:18,
        17:22,
        18:1,
        19:5,
        20:9,
        21:13,
        22:17,
        23:21,
        24:25,
        25:3
    }
    if direction == "f":
        val = ((char + step) + 26) % 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                return (k - step + 26) % 26
