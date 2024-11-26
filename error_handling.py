def read_file():
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_file()