def sync_text_files(file_a_path, file_b_path):
    # 1. Read files and store lines in sets (removes duplicates and allows fast lookups)
    with open(file_a_path, 'r') as f:
        # .strip() removes whitespace/newlines
        set_a = {line.strip() for line in f if line.strip()}

    with open(file_b_path, 'r') as f:
        set_b = {line.strip() for line in f if line.strip()}

    # 2. Find words in B that are NOT in A (Set Difference)
    missing_words = set_b - set_a

    if missing_words:
        print(f"Missing words found: {len(missing_words)}")
        for word in sorted(missing_words):
            print(f" - {word}")

        # 3. Update File A by appending the missing words
        with open(file_a_path, 'a') as f:
            for word in missing_words:
                f.write(f"\n{word}")
        
        print(f"\nSuccessfully updated {file_a_path}.")
    else:
        print("All words from File B are already present in File A.")

# Usage
sync_text_files('large_list.txt', 'small_list.txt')