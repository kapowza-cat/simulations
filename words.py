def filter_five_letter_words(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                # .strip() removes whitespace and newline characters
                word = line.strip()
                
                # Check if the length is exactly 5
                if len(word) == 5:
                    outfile.write(word + '\n')
                    
        print(f"Success! Filtered words saved to {output_file}")
        
    except FileNotFoundError:
        print("Error: The file 'all_words.txt' was not found.")

# Run the function
filter_five_letter_words('all words.txt', 'five_letter_words.txt')