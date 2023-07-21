
import main

import functools

def compras(): 
    b =[]
    for i in main.productos:
        b += list(filter(lambda data:data["producto"]==i,main.datas))

    soloPrecios = list(map(lambda item:item["price"], b))
    result = functools.reduce(lambda counter,precio: counter+precio,soloPrecios )
    return soloPrecios,result


if __name__ == '__main__':
    compras()






















    
