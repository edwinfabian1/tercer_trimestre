#https://docs.python.org/es/3/library/exceptions.html
b=123456
a=int(input("ingrese un valor menor a 20 "))
# IndentationError
def error(a,b):

    if a <=20:
            
            print("error")
    else:
            print("esta bien")
try:  
            print("esta mal")

except IndentationError: 
        error(a)


