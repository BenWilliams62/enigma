# enigma

## description
Just a quick enigma program. Meant to emulate the function of a 3 wheel enigma machine. Command-line interface.

## Time Complexity
- Plug board: O(1)
- Rotor (forwards): O(1)
- Rotor (backwards): O(26) - has to loop through 25 values to find the correct key
- Reflector: O(1)
- Character converters: O(26) - has to loop through 25 values to find the index

## How to use
1. clone this repository
2. configure the settings.json file
  - rotorSwitch1, rotorSwitch2, rotorSwitch3, rotor1Index, rotor2Index, and rotor3Index must be integeres between 0 and 25
  - plugboard, rotor1, rotor2, and rotor3 must use every letter once as a key and once as a value
4. Run the enigma.py file
> python enigma.py
5. enter the digits for rotor starting positions
6. enter your message

## License
No official license. Open for all users
