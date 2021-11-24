class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro
        
    def agregar(self, producto):#Agrega los productos al carro
        if (str(producto.id) not in self.carro.keys()):#Si el producto no está en el carro lo agrega
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url               
            }
        else: #Si el producto esta en el carro lo agrega
            for key, value in self.carro.items(): #Recorremos los items del carro 
                if key==str(producto.id): #Si coincide la id_producto con el producto nuevo, lo incrementamos en 1 y salimos del bucle
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()
        
    def guardar_carro(self): #Actualizamos el carro 
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminar(self, producto):#Eliminamos  producto
        producto.id=str(producto)
        if producto.id in self.carro:
            del self.carro[producto.id]# Elimina el producto del carro
            self.guardar_carro()#Actualiza y guarda el carro
    
    def restar_producto(self, producto):#Eliminamos de a un producto
        for key, value in self.carro.items(): #Recorremos los items del carro 
                if key==str(producto.id): #Si coincide la id_producto con el producto nuevo, lo restamos en 1 y salimos del bucle
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:#Si la cantidad de unidades del producto es menor que uno
                        self.eliminar(producto)
                    break
        self.guardar_carro()
        
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True