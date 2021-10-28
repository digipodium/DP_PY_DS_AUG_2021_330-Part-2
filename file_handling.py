import os

# file handling
# reading
# writing
# updating

# simple reading
file = 'readme.md' 
if os.path.exists(file):            # check file existence
    f = open(file)                  # open file
    content = f.read()              # read file
    f.close()                       # close file 
    print("file content", content)
else:
    print("no file found", file)

# better reading

file2 = 'image_view.py'
if os.path.exists(file2):
    with open(file2) as f:
        data = f.read()
    
    print(data)
else:
    print("file not found")