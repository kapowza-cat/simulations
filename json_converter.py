import json

with open('five_letter_words.txt', 'r') as f:
    # Create a list of words, removing newlines
    word_list = [line.strip() for line in f if line.strip()]

# Save as a JSON array
with open('words.json', 'w') as f:
    json.dump(word_list, f)