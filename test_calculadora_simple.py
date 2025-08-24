"""
Script de pruebas simple para la calculadora
Prueba de escritorio
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from calculadora import Calculadora


def probar_calculadora():
    """
    Función principal que ejecuta todas las pruebas de la calculadora
    de manera sencilla y básica
    """
    print("\n")
    print("PRUEBAS DE LA CALCULADORA")

    
    calc = Calculadora()
    
    pruebas_totales = 0
    pruebas_exitosas = 0
    
    print("\n1. Probando SUMA...")
    pruebas_totales += 1
    resultado = calc.sumar(10, 5)
    esperado = 15
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 10 + 5 = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 10 + 5 = {resultado}, se esperaba {esperado}")
    
    print("\n2. Probando RESTA...")
    pruebas_totales += 1
    resultado = calc.restar(10, 3)
    esperado = 7
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 10 - 3 = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 10 - 3 = {resultado}, se esperaba {esperado}")
    
    print("\n3. Probando MULTIPLICACIÓN...")
    pruebas_totales += 1
    resultado = calc.multiplicar(4, 6)
    esperado = 24
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 4 × 6 = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 4 × 6 = {resultado}, se esperaba {esperado}")
    
    print("\n4. Probando DIVISIÓN...")
    pruebas_totales += 1
    resultado = calc.dividir(15, 3)
    esperado = 5.0
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 15 ÷ 3 = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 15 ÷ 3 = {resultado}, se esperaba {esperado}")
    
    print("\n5. Probando DIVISIÓN POR CERO...")
    pruebas_totales += 1
    try:
        calc.dividir(10, 0)
        print("   ✗ ERROR: Debería haber lanzado una excepción al dividir por cero")
    except ValueError as e:
        print(f"   ✓ CORRECTO: División por cero manejada correctamente - {e}")
        pruebas_exitosas += 1
    except Exception as e:
        print(f"   ✗ ERROR: Excepción inesperada - {e}")
    
    print("\n6. Probando POTENCIA...")
    pruebas_totales += 1
    resultado = calc.potencia(2, 3)
    esperado = 8
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 2³ = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 2³ = {resultado}, se esperaba {esperado}")
    
    print("\n7. Probando PORCENTAJE...")
    pruebas_totales += 1
    resultado = calc.porcentaje(200, 15)
    esperado = 30.0
    if resultado == esperado:
        print(f"   ✓ CORRECTO: 15% de 200 = {resultado}")
        pruebas_exitosas += 1
    else:
        print(f"   ✗ ERROR: 15% de 200 = {resultado}, se esperaba {esperado}")
    
    print("\n")
    print("RESUMEN DE PRUEBAS")

    print(f"Pruebas ejecutadas: {pruebas_totales}")
    print(f"Pruebas exitosas: {pruebas_exitosas}")
    print(f"Pruebas fallidas: {pruebas_totales - pruebas_exitosas}")
    
    if pruebas_exitosas == pruebas_totales:
        print("\n Todas las pruebas pasaron. La calculadora funciona correctamente.")
        return True
    else:
        print(f"\n {pruebas_totales - pruebas_exitosas} prueba(s) fallaron. Revisar la implementación.")
        return False


def pruebas_adicionales():
    """
    Pruebas adicionales con casos más variados
    """
    print("\n")
    print("PRUEBAS ADICIONALES")
 
    
    calc = Calculadora()
    
    print("\n• Probando números negativos...")
    resultado = calc.sumar(-5, 3)
    print(f"  -5 + 3 = {resultado} (esperado: -2)")
    
    print("\n• Probando números decimales...")
    resultado = calc.multiplicar(2.5, 4)
    print(f"  2.5 × 4 = {resultado} (esperado: 10.0)")
    
    print("\n• Probando potencia con exponente 0...")
    resultado = calc.potencia(5, 0)
    print(f"  5⁰ = {resultado} (esperado: 1)")
    
    print("\n• Probando porcentaje de 0...")
    resultado = calc.porcentaje(0, 50)
    print(f"  50% de 0 = {resultado} (esperado: 0.0)")


if __name__ == "__main__":
    print("Iniciando pruebas de la calculadora...")
    
    exito = probar_calculadora()
    
    pruebas_adicionales()
    
    print("\n")
    if exito:
        print(" PRUEBAS COMPLETADAS EXITOSAMENTE")
    else:
        print("ALGUNAS PRUEBAS FALLARON")
   
