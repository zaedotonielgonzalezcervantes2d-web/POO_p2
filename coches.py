print("\033n")

class Coches:
    """Clase principal / Super clase / Clase padre."""

    def __init__(self, color: str, marca: str, modelo: str,
                 velocidad: int, caballaje: int, plazas: int):
        # Atributos protegidos (#)
        self._color = color
        self._marca = marca
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    # Métodos
    def acelerar(self):
        self._velocidad += 10
        print(f"{self._marca} acelera. Velocidad actual: {self._velocidad} km/h")

    def frenar(self):
        self._velocidad = max(0, self._velocidad - 10)
        print(f"{self._marca} frena. Velocidad actual: {self._velocidad} km/h")

    def __str__(self):
        return (f"{type(self).__name__}: color={self._color}, marca={self._marca}, "
                f"modelo={self._modelo}, velocidad={self._velocidad}, "
                f"caballaje={self._caballaje}, plazas={self._plazas}")


class Camiones(Coches):
    """Clase secundaria / Sub clase / Clase hija (hereda de Coches)."""

    def __init__(self, color: str, marca: str, modelo: str,
                 velocidad: int, caballaje: int, plazas: int,
                 eje: int, capacidad_carga: int):
        super().__init__(color, marca, modelo, velocidad, caballaje, plazas)
        self.__eje = eje
        self.__capacidad_carga = capacidad_carga

    def cargar(self, tipo_carga):
        print(f"El camión {self._marca} está cargando: {tipo_carga} "
              f"(capacidad máxima: {self.__capacidad_carga} kg)")

    def acelerar(self):
        self._velocidad += 5
        print(f"El camión {self._marca} acelera lentamente. "
              f"Velocidad actual: {self._velocidad} km/h")

    def frenar(self):
        self._velocidad = max(0, self._velocidad - 5)
        print(f"El camión {self._marca} frena con cuidado. "
              f"Velocidad actual: {self._velocidad} km/h")

    def __str__(self):
        return (f"{super().__str__()}, eje={self.__eje}, "
                f"capacidadCarga={self.__capacidad_carga}")


class Camionetas(Coches):
    """Clase secundaria / Sub clase / Clase hija (hereda de Coches)."""

    def __init__(self, color: str, marca: str, modelo: str,
                 velocidad: int, caballaje: int, plazas: int,
                 traccion: str, cerrada: bool):
        super().__init__(color, marca, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def transportar(self, num_pasajeros: int):
        if num_pasajeros <= self._plazas:
            print(f"La camioneta {self._marca} transporta {num_pasajeros} pasajeros.")
        else:
            print(f"La camioneta {self._marca} solo tiene {self._plazas} plazas, "
                  f"no puede transportar a {num_pasajeros}.")

    def acelerar(self):
        self._velocidad += 8
        print(f"La camioneta {self._marca} acelera. "
              f"Velocidad actual: {self._velocidad} km/h")

    def frenar(self):
        self._velocidad = max(0, self._velocidad - 8)
        print(f"La camioneta {self._marca} frena. "
              f"Velocidad actual: {self._velocidad} km/h")

    def __str__(self):
        return (f"{super().__str__()}, traccion={self.__traccion}, "
                f"cerrada={self.__cerrada}")


if __name__ == "__main__":
    
    coche1 = Coches("Blanco", "VW", "2022", 220, 150, 5)
    coche2 = Coches("Azul", "Nissan", "2020", 180, 150, 6)

   
    camion1 = Camiones("Negro", "Dina", "2020", 180, 300, 12, 8, 2500)
    camion2 = Camiones("Azul", "Star", "2019", 150, 200, 14, 6, 2000)


    camioneta1 = Camionetas("Amarillo", "Renault", "2025", 240, 250, 8, "delantera", True)
    camioneta2 = Camionetas("Blanca", "Nissan", "2020", 180, 150, 0, "trasera", False)

    for vehiculo in (coche1, coche2, camion1, camion2, camioneta1, camioneta2):
        print(vehiculo)

    print()
    coche1.acelerar()
    coche2.frenar()
    camion1.cargar("Materiales de construcción")
    camion1.acelerar()
    camion2.frenar()
    camioneta1.transportar(5)
    camioneta2.transportar(3)
    camioneta1.acelerar()
    camioneta2.frenar()