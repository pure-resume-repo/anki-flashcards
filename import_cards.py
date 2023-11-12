import argparse
import random

import genanki
import yaml

# Command-line argument parsing
parser = argparse.ArgumentParser(
    description="Generate Anki flashcards from a YAML file."
)
parser.add_argument(
    "file",
    help="Path to the YAML file containing terms and definitions.",
)
parser.add_argument(
    "deck_name",
    help="The name of the Anki deck to be created.",
)
args = parser.parse_args()

# Read YAML file
with open(args.file) as f:
    data = yaml.safe_load(f)


# Function to generate a random ID
def generate_random_id():
    return random.randint(1000000000, 9999999999)


# Anki model and deck setup with random IDs
my_model = genanki.Model(
    generate_random_id(),
    "Simple Model",
    fields=[{"name": "Term"}, {"name": "Definition"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Term}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Definition}}',
        }
    ],
)

# Create deck with a dynamic name based on the command-line argument
my_deck = genanki.Deck(generate_random_id(), args.deck_name)

# Create Anki cards
for term, definition in data.items():
    my_note = genanki.Note(
        model=my_model,
        fields=[term, definition],
    )
    my_deck.add_note(my_note)

# Generate Anki package (.apkg) with a dynamic file name based on the command-line argument
package_name = f"{args.deck_name.replace(' ', '_')}.apkg"
genanki.Package(my_deck).write_to_file(package_name)

print(f"Anki deck has been generated as '{package_name}'.")
