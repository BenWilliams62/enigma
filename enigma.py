from functions import (
    input_message,
    char_to_number,
    number_to_char,
    plug,
    reflect,
    rotor_1,
    rotor_2,
    rotor_3
)


def main():
    # plug board - change the keys to desired plugs.
    # Use every character once as a key and once as a value
    # Set this regularly
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
    # Set these switches irregularly
    rotor_1_switch = 5
    rotor_2_switch = 2
    rotor_3_switch = 13

    # dont touch values below here
    output = ""                     # sets output as empty string to append values to
    print("\nrotor settings:\n")
    rotor_1_index = int(input("enter the number for rotor 1's starter position:\n"))   # starting value
    rotor_2_index = int(input("enter the number for rotor 2's starter position:\n"))   # starting value
    rotor_3_index = int(input("enter the number for rotor 3's starter position:\n"))   # starting value
    print("\n\n")
    input_value = input_message()   # takes an input string

    for char in input_value:
        
        if char.isalpha() == 0: # validate - escape spaces and punctuation
            output += char
        else:
            # put through plug board
            plugged = plug(char, plug_board)

            # convert to number for rotor usage
            num = char_to_number(plugged)

            # go through rotor 1
            rot_1 = rotor_1(num, rotor_1_index, "f")

            # go through rotor 2
            rot_2 = rotor_2(rot_1, rotor_2_index, "f")

            # go through rotor 3
            rot_3 = rotor_3(rot_2, rotor_3_index, "f")

            # reflect
            reflection = reflect(rot_3)

            # go through rotor 3 backwards
            rot_3_ref = rotor_3(reflection, rotor_3_index, "b")

            # go through rotor 2 backwards
            rot_2_ref = rotor_2(rot_3_ref, rotor_2_index, "b")

            # go through rotor 1 backwards
            rot_1_ref = rotor_1(rot_2_ref, rotor_1_index, "b")

            # convert number to character
            return_char = number_to_char(rot_1_ref)

            # back through plug board
            return_plug = plug(return_char, plug_board)


            # add value to output
            output += return_plug
            
            # add new setting for the rotors
            rotor_1_index += 1
            if rotor_1_index > rotor_1_switch:
                rotor_1_index -= 26
                rotor_2_index += 1

            if rotor_2_index > rotor_2_switch:
                rotor_2_index -= 26
                rotor_3_index += 1

            if rotor_3_index > rotor_3_switch:
                rotor_3_index -= 26


    print("\noutput message:\n")
    print(output)

if __name__ == "__main__":
    main()