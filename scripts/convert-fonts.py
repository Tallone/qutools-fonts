from fontTools.ttLib import TTFont

if __name__ == "__main__":
    # Path to your .otf file
    otf_path = "/Users/tallone/GitHub/qutools-fonts/hwmct.otf"

    # Path to save the .ttf file
    ttf_path = "hwmct.ttf"

    # Load the .otf font
    font = TTFont(otf_path)

    # Save as .ttf
    font.save(ttf_path)

    print(f"Font successfully converted from {otf_path} to {ttf_path}")
