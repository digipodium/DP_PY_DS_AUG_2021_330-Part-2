# file handling mode
# r - reading (default)
# w - writing
# a - append

try:                                       # try to run the code in the block
    f = open('msg.txt','a')                # creates a file msg.txt or opens it
    f.write("\nThis is a message in a file") # storing information as text
    f.close()                              # saving and closing file
except Exception as e:                     # handle the error 
    print('error->',e)                     # show the error msg from e variable


# better version
try:
    with open('msg2.txt','a') as f:
        f.write("1,2,3")
        f.write('2,3,4,5')
        f.write('\n kuch to gadbad h!')
except Exception as e:
    print(e)
else:
    print("Successfully created file")