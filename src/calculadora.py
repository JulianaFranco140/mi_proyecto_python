"""
Calculadora Simple - Proyecto de ejemplo para GitHub Actions
"""


class Calculadora:
    
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - a
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
    
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def potencia(self, base, exponente):
        return base ** exponente
    
    def porcentaje(self, cantidad, porcentaje):
        return (cantidad * porcentaje) / 100


def main():
    calc = Calculadora()
    
    print("Calculadora")
    print("=" * 30)
    
    # Ejemplos de uso
    print(f"Suma: 10 + 5 = {calc.sumar(10, 5)}")
    print(f"Resta: 10 - 5 = {calc.restar(10, 5)}")
    print(f"Multiplicación: 10 * 5 = {calc.multiplicar(10, 5)}")
    print(f"División: 10 / 5 = {calc.dividir(10, 5)}")
    print(f"Potencia: 2^3 = {calc.potencia(2, 3)}")
    print(f"Porcentaje: 20% de 100 = {calc.porcentaje(100, 20)}")


if __name__ == "__main__":
    main()
