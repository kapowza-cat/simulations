import json

# Replace 'my_words.txt' with the name of your text file
input_file = 'five_letter_words.txt' 
output_file = 'words.json'

word_dict = {}

try:
    with open(input_file, 'r') as f:
        # Read lines, remove whitespace, and skip empty lines
        words = [line.strip().upper() for line in f if line.strip()]
        
        # Create the dictionary structure: {"word1": "APPLE", "word2": "BEACH", ...}
        for index, word in enumerate(words):
            word_dict[f"word{index + 1}"] = word

    # Save as formatted JSON
    with open(output_file, 'w') as f:
        json.dump(word_dict, f, indent=4)

    print(f"Success! {len(words)} words converted to {output_file}")

except FileNotFoundError:
    print("Error: Could not find your text file. Make sure it's in the same folder.")