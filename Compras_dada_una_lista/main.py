#este software simula la compra de un producto ("los productos comprados están en productos") y los productos que hay en DATAS ("los productos disponible son ilimitados")



datas = [
    {
        "producto":"arroz",
        "price" : 1200
    },
    {
        "producto":"carne",
        "price" : 16000
    },
    {
        "producto":"buñuelo",
        "price" : 2000
    }
]
print('Productos Disponibles. \n arroz:1200 \n carne:16000 \n buñuelo:2000 \n')
n = int(input("Cantidad de productos comprados: "))
productos = list(map(lambda x: input("Elemento comprado: "),range(n)))



















