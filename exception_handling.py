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
    print('π­π’',e)
else:
    print("π done")
finally:
    print("πthe end")
