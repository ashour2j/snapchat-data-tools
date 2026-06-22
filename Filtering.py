def filter_lines_by_word():
    # 1. Ask for the source file name
    source_file = input("Enter the name of the .txt file to search: ").strip()
    
    # 2. Ask for the word to filter
    search_word = input("Enter the word you want to filter for: ").strip()
    
    # 3. Define the output filename based on the search word
    output_filename = f"{search_word}.txt"

    try:
        # Open the source to read and the new file to write
        with open(source_file, 'r', encoding='utf-8') as f_in:
            # We gather the matching lines first to see if we found anything
            # matching_lines = [line for line in f_in if search_word.lower() in line.lower()]
            
            matches = []
            for line in f_in:
                # Case-insensitive check: matches "Word", "WORD", or "word"
                if search_word.lower() in line.lower():
                    matches.append(line)

        if matches:
            # Write the results to the new file
            with open(output_filename, 'w', encoding='utf-8') as f_out:
                f_out.writelines(matches)
            
            print(f"--- Process Complete ---")
            print(f"Found {len(matches)} lines containing '{search_word}'.")
            print(f"Results exported to: {output_filename}")
        else:
            print(f"No lines found containing the word: '{search_word}'")

    except FileNotFoundError:
        print(f"Error: Could not find '{source_file}'. Make sure the file is in the same folder as this script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    filter_lines_by_word()