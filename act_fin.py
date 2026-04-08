from abc import ABC, abstractmethod

class CriaturaBase(ABC):
    def __init__(self, nombre, especie, energia):
        self.nombre = nombre
        self.especie = especie
        self.energia = energia

    @abstractmethod
    def activar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


if __name__ == "__main__":
    try:
        c = CriaturaBase("X", "Y", 100)
    except TypeError as e:
        print("[OK] No se puede instanciar:", e)


class Comunicacion:
    def __init__(self, idioma_inicial):
        self.idioma = idioma_inicial
        self.historial = [idioma_inicial]
        self._mensajes = []

    def cambiar_idioma(self, nuevo_idioma):
        self.idioma = nuevo_idioma
        self.historial.append(nuevo_idioma)
        return f"Idioma cambiado a: {nuevo_idioma}"

    def enviar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)
        return f"Mensaje enviado: {mensaje}"

    def ver_historial_idiomas(self):
        return " -> ".join(self.historial)

    def ver_mensajes(self):
        return " | ".join(self._mensajes) if self._mensajes else "Sin mensajes"


if __name__ == "__main__":
    c = Comunicacion("Binario")
    print(c.cambiar_idioma("Español"))
    print(c.enviar_mensaje("Hola"))
    print(c.ver_historial_idiomas())
    print(c.ver_mensajes())

class Evolucion:
    def __init__(self, nivel_inicial):
        self._nivel = nivel_inicial
        self._experiencia = 0

    def ganar_experiencia(self, puntos):
        if puntos < 0:
            return "No se puede ganar experiencia negativa"
        self._experiencia += puntos
        return f"Experiencia actual: {self._experiencia}"

    def evolucionar(self):
        if self._experiencia < 50:
            return "No hay suficiente experiencia para evolucionar"
        self._nivel += 1
        self._experiencia = 0
        return f"Evolución exitosa. Nivel actual: {self._nivel}"

    def estado_evolucion(self):
        return f"Nivel: {self._nivel} | EXP: {self._experiencia}"


if __name__ == "__main__":
    e = Evolucion(1)
    print(e.ganar_experiencia(60))
    print(e.evolucionar())
    print(e.estado_evolucion())


class CriaturaDigital(CriaturaBase, Comunicacion, Evolucion):

    def __init__(self, nombre, especie, energia, idioma, nivel, estabilidad):
        CriaturaBase.__init__(self, nombre, especie, energia)
        Comunicacion.__init__(self, idioma)
        Evolucion.__init__(self, nivel)

        self.__activa = False
        self._estabilidad = estabilidad

    @property
    def estabilidad(self):
        return self._estabilidad

    @estabilidad.setter
    def estabilidad(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Estabilidad inválida")
        if valor > 100:
            raise ValueError("Máximo 100")
        self._estabilidad = valor

    def activar(self):
        if self.__activa:
            return f"{self.nombre} ya está activa."
        self.__activa = True
        return f"{self.nombre} activada."

    def __str__(self):
        estado = "Activa" if self.__activa else "Inactiva"
        return f"{self.nombre} ({self.especie}) | Energía: {self.energia} | Nivel: {self._nivel} | Estabilidad: {self._estabilidad} | Estado: {estado}"


if __name__ == "__main__":

    c1 = CriaturaDigital("Zyra", "Bio", 80, "Binario", 1, 70)
    c2 = CriaturaDigital("Orion", "Cyber", 90, "Código", 2, 80)
    c3 = CriaturaDigital("Nova", "Energía", 75, "Frecuencia", 3, 60)

    criaturas = [c1, c2, c3]

    print("\n--- POLIMORFISMO ---")
    for c in criaturas:
        print(c.activar())

    print("\n--- OBJETOS ---")
    for c in criaturas:
        print(c)

    print("\n--- FUNCIONES ---")
    print(c1.cambiar_idioma("Español"))
    print(c2.ganar_experiencia(60))
    print(c2.evolucionar())

    print("\n--- ENCAPSULAMIENTO ---")
    print(c1.estabilidad)
    c1.estabilidad = 95
    print(c1.estabilidad)

    print("\n--- VALIDACIÓN ---")
    try:
        c1.estabilidad = -10
    except ValueError as e:
        print("Error:", e)