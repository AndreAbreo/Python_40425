class Cliente:
    def __init__(self, nombre, apellido, cedula, saldo_puntos):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.saldo_puntos = saldo_puntos

    def gastar_puntos(self, puntos_gastados):
        if puntos_gastados <= self.saldo_puntos:
            self.saldo_puntos -= puntos_gastados
            return self.saldo_puntos
        else:
            return False

    def __str__(self):
        return f"Cliente: {self.nombre} con {self.saldo_puntos} puntos"


class ClienteVIP:
    def __init__(self, nombre, apellido, cedula, saldo_puntos, descuento):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.saldo_puntos = saldo_puntos
        self.descuento = descuento

    def gastar_puntos(self, puntos_gastados):
        puntos_restantes = self.saldo_puntos - puntos_gastados * (1 - self.descuento / 100)
        self.saldo_puntos = max(puntos_restantes, 0)
        return puntos_restantes

    def __str__(self):
        return f"Cliente VIP: {self.nombre} con {self.saldo_puntos} puntos y {self.descuento}% de descuento."
