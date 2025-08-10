"""
Hex Colours
Estimate: 10 minutes
Actual: 37
"""

COLOUR_NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a"
}


def main():
    """Look up hex codes by colour name (case-insensitive)."""
    print(COLOUR_NAME_TO_HEX)
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        try:
            print(f"{colour_name.title()} is {COLOUR_NAME_TO_HEX[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
