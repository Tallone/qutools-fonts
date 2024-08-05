from fontTools import subset
from fontTools.ttLib import TTFont

# Path to your original .ttf font file
ttf_path = "albbpht.ttf"

# Path to save the streamlined .ttf font file
subset_ttf_path = "mini-" + ttf_path

# List of characters you want to keep in the font
with open("scripts/3500chars.txt", 'r') as file:
    characters_to_keep = file.read()

    # Create a subsetter object
    options = subset.Options()
    options.text = characters_to_keep
    font = TTFont(ttf_path)

    # Subset the font
    subsetter = subset.Subsetter(options)
    subsetter.populate(text=characters_to_keep)
    subsetter.subset(font)

    # Save the streamlined font
    font.save(subset_ttf_path)

    print(f"Font successfully subset to contain only specified characters and saved to {subset_ttf_path}")
