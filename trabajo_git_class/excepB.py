values = (1, 0) # se define una tupla 
#x,y=19,30
#print(divmod(10,3))
try:
    q, r = divmod(*values) # divmod es una funcion 
    #print('q=',q)
    print(f'q={q}') #
    print(f'r={r}') #
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)