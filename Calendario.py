anio = int(input('Ingrese un anio: '))


if anio < 1583:
    print('Esta fuera del calendario Gregoriano')
elif anio % 4 != 0:
    print("Es un año común")
elif anio % 100 != 0:
    print('Es un año bisiesto')
elif anio % 400 != 0:
    print('Es un año común')
elif anio < 1583:
    print('Esta fuera del calendario Gregoriano')
else:
    print('Anio bisiesto')



