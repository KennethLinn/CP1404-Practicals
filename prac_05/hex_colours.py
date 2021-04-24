COLOUR_CODES = {"Alice Blue": "#f0f8ff", "Antique White": "#faebd7",
                "Antique White 1": "#ffefdb", "Antique White 2": "#eedfcc",
                "Antique White 3": "#cdc0b0", "Antique White 4": "#8b8378",
                "Aquamarine 1": "#7fffd4", "Aquamarine 2": "#76eec6",
                "Aquamarine 4": "#458b74", "Azure 1": "#f0ffff"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter colour name: ")