from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Cliente:
    nombre: Optional[str] = None
    edad: Optional[int] = None
    direccion: Optional[str] = None
    creditos_disponibles: Optional[int] = None
    productos: List[str] = field(default_factory=list)

    def __str__(self):
        return (f"Cliente: {self.nombre}, Edad: {self.edad}, "
                f"Dirección: {self.direccion}, Créditos disponibles: {self.creditos_disponibles}, productos: {self.productos}")

    @classmethod
    def crear_cliente(cls, nombre: str, edad: int, direccion: str, creditos_disponibles: int, productos: List[str]):
        cliente = cls(nombre, edad, direccion, creditos_disponibles, productos)
        print(cliente)
        return cliente
    
    @staticmethod
    def ingresar_productos() -> List[str]:
        productos_list = []
        while True:
            producto = input("Ingresa un producto o escriba 'fin' para terminar: ")
            if producto.lower() == 'fin':
                break
            productos_list.append(producto)
            
        return productos_list

    def solicitar_cadena(mensaje: str) -> str:
     while True:
        valor = input(mensaje)
        if valor.strip():
            return valor
        
        print("El nombre no puede estar vacío, intente nuevamente")
    
    def solicitar_entero(mensaje: str) -> int:
        while True:
            valor = input(mensaje)
            try:
                return int(valor)
            except ValueError:
                print("La edad tiene que ingresarse en formato válido. Intente nuevamente")