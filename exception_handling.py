# exception
# try except
# else
# finally
####


try:
    x= int(input('enter value:'))
    y= int(input('enter 2nd value:'))
    out = x / y
    print(out)
except Exception as e:
    print('😭😢',e)
else:
    print("😁 done")
finally:
    print("😏the end")
