# enigma machine

# plug board - swap some letters
plug_board = {
    "a":"z",
    "b":"y",
    "c":"x",
    "d":"w",
    "e":"v",
    "f":"u",
    "g":"t",
    "h":"s",
    "i":"r",
    "j":"q",
    "k":"p",
    "l":"o",
    "m":"n",
    "n":"m",
    "o":"l",
    "p":"k",
    "q":"j",
    "r":"i",
    "s":"h",
    "t":"g",
    "u":"f",
    "v":"e",
    "w":"d",
    "x":"c",
    "y":"b",
    "z":"a"
}

def plug(char):
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
        val = (char + step)
        if val > 25:
            val -= 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                if k - step < 0:
                    return k - step + 26
                return k - step

# rotor 2
def rotor_2(char, step, direction):
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
        val = (char + step)
        if val > 25:
            val -= 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                if k - step < 0:
                    return k - step + 26
                return k - step

# rotor 3
def rotor_3(char, step, direction):
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
        val = (char + step)
        if val > 25:
            val -= 26
        return switcher[val]
    else:
        for k, v in switcher.items():
            if v == char:
                if k - step < 0:
                    return k - step + 26
                return k - step
