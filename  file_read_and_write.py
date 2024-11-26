def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, replace 'old' with 'new')
        modified_content = content.replace("old", "new")
        
        # Open the output file in write mode and save the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: There was an issue with reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = "input.txt"
output_file = "output.txt"
modify_file(input_file, output_file)