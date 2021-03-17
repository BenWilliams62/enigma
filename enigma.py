from functions import (
    input_message,
    plug,
    reflect,
    rotor_function
)
import json



def main():
    # read in data from settings.json
    with open('./settings.json') as f:
        data = json.load(f)
    
    # set settings
    plug_board = data["plugBoard"]              # plugboard
    rotor_1_switch = data["rotorSwitch1"]       # rotor switch 1
    rotor_2_switch = data["rotorSwitch2"]       # rotor switch 2
    rotor_3_switch = data["rotorSwitch3"]       # rotor switch 3
    rotor_1_setting = data["rotor1"]            # rotor 1
    rotor_2_setting = data["rotor2"]            # rotor 2
    rotor_3_setting = data["rotor3"]            # rotor 3
    rotor_1_index = data["rotor1Index"]         # rotor 1 starting position
    rotor_2_index = data["rotor2Index"]         # rotor 2 starting position
    rotor_3_index = data["rotor3Index"]         # rotor 3 starting position
    

    # dont touch values below here
    input_value = input_message()   # takes an input string
    output = ""                     # sets output as empty string to append values to

    for char in input_value:
        
        if char.isalpha() == 0: # validate - escape spaces and punctuation
            output += char
        else:
            # put through plug board
            plugged = plug(char, plug_board)
            # z - s

            # go through rotor 1
            rot_1 = rotor_function(plugged, rotor_1_index, "f", rotor_1_setting)

            # go through rotor 2
            rot_2 = rotor_function(rot_1, rotor_2_index, "f", rotor_2_setting)

            # go through rotor 3
            rot_3 = rotor_function(rot_2, rotor_3_index, "f", rotor_3_setting)

            # reflect
            reflection = reflect(rot_3)

            # go through rotor 3 backwards
            rot_3_ref = rotor_function(reflection, rotor_3_index, "b", rotor_3_setting)

            # go through rotor 2 backwards
            rot_2_ref = rotor_function(rot_3_ref, rotor_2_index, "b", rotor_2_setting)

            # go through rotor 1 backwards
            rot_1_ref = rotor_function(rot_2_ref, rotor_1_index, "b", rotor_1_setting)

            # back through plug board
            return_plug = plug(rot_1_ref, plug_board)
            


            # add value to output
            output += return_plug
            # h - a
            
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
    print(output.upper())

if __name__ == "__main__":
    main()