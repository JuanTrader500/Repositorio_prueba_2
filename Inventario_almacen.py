#Inventario de un almacen 

print("Welcome to American_clothes")

inventario = []

meany_prooducts = int(input("how meany products do you want to add?\n"))

for i in range(meany_prooducts):

    print(f'White the detail of the {i+1} product:')
    nombre = input("name:")
    precio = float(input('precio:'))
    cantidad = int(input('cantidad disponible:'))
    
    #Creamos un dicicionario para crear un nuevo producto.
    detail = {"id":i+1,"name":nombre,"price":precio,"amount":cantidad}
    
    #Agregamos nuesto diccionario que contiene un nuevo producto a la lista de productos 
    inventario.append(detail)
    

found = int(input("Ingrese el id del producto que quiere buscar:"))

#Declaramos la variable para almacenaar el producto si se encuenta o no
producto_encontrado = None

for producto in inventario:
    time = producto["id"]
    if time == found:
        producto_encontrado = producto
        break

#Imprimir el mensaje si se encontro el producto o no 
if producto_encontrado is not None:
    print(f'El producto con el id {found} es {producto_encontrado} ')
    
else:
    
    print(f"El producto con el id {found} no se encontro ")





