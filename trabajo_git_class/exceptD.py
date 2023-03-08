def edad ():
    try:
        tuedad=int(input("introduce tu edad" )) #se pide el ingreso 
        print(f'tu edad es  {tuedad}')
        #print('Tu edad es ',tuedad)
    except ValueError as e:    #
        print(e)
        print("La edad debe ser un valor numerico...")
        edad()
    else:
        print('Viene por el else')

edad()