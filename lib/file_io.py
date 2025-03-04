# lib/file_io.py

def write_file(file_name, file_content):
    """Write content to a .txt file."""
    # Add the .txt extension to the file name
    file_name = f"{file_name}.txt"
    
    # Open the file in write mode ('w') to overwrite existing content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to an existing .txt file."""
    # Add the .txt extension to the file name
    file_name = f"{file_name}.txt"
    
    # Open the file in append mode ('a') to add content at the end of the file
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """Read and return the content of a .txt file."""
    # Add the .txt extension to the file name
    file_name = f"{file_name}.txt"
    
    try:
        # Open the file in read mode ('r') to get the content
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        # Return a message if the file doesn't exist
        return f"The file {file_name} does not exist."
