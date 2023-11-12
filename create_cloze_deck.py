import argparse
import random

import genanki
import yaml

# Command-line argument parsing
parser = argparse.ArgumentParser(
    description="Generate Anki flashcards from a YAML file."
)
parser.add_argument(
    "file", help="Path to the YAML file containing terms and definitions."
)
parser.add_argument("deck_name", help="The name of the Anki deck to be created.")
args = parser.parse_args()

# Read YAML file
with open(args.file) as f:
    data = yaml.safe_load(f)


# Function to generate a random ID
def generate_random_id():
    return random.randint(1000000000, 9999999999)


# Cloze model setup with random ID
cloze_model = genanki.Model(
    generate_random_id(),
    "Cloze Model",
    fields=[{"name": "Text"}],
    templates=[
        {
            "name": "Cloze",
            "qfmt": "{{cloze:Text}}",
            "afmt": "{{cloze:Text}}",
        },
    ],
    model_type=genanki.Model.CLOZE,
)

# Create deck with a dynamic name based on the command-line argument
my_deck = genanki.Deck(generate_random_id(), args.deck_name)

# Create Anki cards with cloze deletions
for term, definition in data.items():
    cloze_text = f"{term} {{c1::{definition}}}"
    my_note = genanki.Note(
        model=cloze_model,
        fields=[cloze_text],
    )
    my_deck.add_note(my_note)

# Generate Anki package (.apkg) with a dynamic file name based on the command-line argument
package_name = f"{args.deck_name.replace(' ', '_')}.apkg"
genanki.Package(my_deck).write_to_file(package_name)

print(f"Anki deck with cloze deletions has been generated as '{package_name}'.")
