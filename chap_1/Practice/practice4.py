import os

# Specify the directory path (you can change this to any path you want)
directory = "/"

# Get the list of files and folders
contents = os.listdir(directory)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)
