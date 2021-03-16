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
    input_value = input_message()
    output = ""
    rotor_1_index = int(input("enter the number for rotor 1's starter position:\n"))   # starting value
    rotor_2_index = int(input("enter the number for rotor 2's starter position:\n"))   # starting value
    rotor_3_index = int(input("enter the number for rotor 3's starter position:\n"))   # starting value

    for char in input_value:
        # validate - escape spaces and punctuation
        if char.isalpha() == 0:
            output += char
        else:
            # put through plug board
            plugged = plug(char) 

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
            rot_3_ref = rotor_1(reflection, rotor_3_index, "b") 

            # go through rotor 2 backwards
            rot_2_ref = rotor_1(rot_3_ref, rotor_2_index, "b")  

            # go through rotor 1 backwards
            rot_1_ref = rotor_1(rot_2_ref, rotor_1_index, "b")  

            # convert number to character
            return_char = number_to_char(rot_1_ref) 

            # back through plug board
            return_plug = plug(return_char)


            # add value to output
            output += return_plug
            
            # add new setting for the rotors
            rotor_1_index += 1
            if rotor_1_index == 26:
                rotor_1_index = 0
                rotor_2_index += 1
            if rotor_2_index == 26:
                rotor_2_index = 0
                rotor_3_index += 1
            if rotor_3_index == 26:
                rotor_3_index = 0


    print(output)

if __name__ == "__main__":
    main()