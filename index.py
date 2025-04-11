def read_and_modify_file():
    # Define filenames
    existing_file = "final.txt"       # File you expect to read from
    new_file = "new_final.txt"        # Name of the new file to write to
    
    existing_file = input("Enter the name of the file to read: ")


    try:
        # Attempt to open and read the existing file
        with open(existing_file, 'r', encoding='utf-8') as infile:
            content = infile.read()   # Read all content from the file

        # Modify the content (convert to uppercase as an example)
        modified_content = content.upper()   # Transform to uppercase

        # Write the modified content to the new file
        with open(new_file, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)  # Write new content

        print(f"Content from '{existing_file}' has been modified and saved to '{new_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{existing_file}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read or write to the file. Details: {e}")

# Run the function
read_and_modify_file()
