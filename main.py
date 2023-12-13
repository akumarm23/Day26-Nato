# NATO Phonetic Names v0.1

import pandas

# Load the NATO phonetic alphabet data from the CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Using a dictionary comprehension to iterate over rows in the DataFrame and create the mapping
ph_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(ph_dict)  # Uncomment to check the created dictionary

def generate_phonetic():
    # Get user input for a word and convert it to uppercase
    word = input("Enter a word: ").upper()
    try:
        # Create a list of phonetic code words using the dictionary created earlier
        output = [ph_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters from A-Z please.\n")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()


# END OF CODE
