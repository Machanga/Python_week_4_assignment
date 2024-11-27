# question 1
def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()  
        modified_content = content.upper()  

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)  
        print(f"Content has been modified and written to {output_file}")
        
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_filename = 'input.txt'
output_filename = 'output.txt'

modify_file(input_filename, output_filename)


# question 2
def get_file():
    filename = input("Please enter the filename: ")

    try:
        with open(filename, 'r') as file:
            print("File opened successfully!")
            content = file.read()
            print(content)  
            
    except FileNotFoundError:
        print("Error: The file does not exist.")
        
    except PermissionError:
        print("Error: You do not have permission to read the file")
        
    except Exception as e:
        print("An unexpected error occurred: {e}")
get_file()
