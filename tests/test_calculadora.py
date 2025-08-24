"""
Pruebas unitarias para la calculadora simple.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import Calculadora


class TestCalculadora:
    """Clase de pruebas para la calculadora."""
    
    def setup_method(self):
        """Configuración antes de cada prueba."""
        self.calc = Calculadora()
    
    def test_sumar(self):
        """Prueba la función de suma."""
        assert self.calc.sumar(2, 3) == 5
        assert self.calc.sumar(-1, 1) == 0
        assert self.calc.sumar(0, 0) == 0
        assert self.calc.sumar(-5, -3) == -8
        assert self.calc.sumar(1.5, 2.5) == 4.0
    
    def test_restar(self):
        """Prueba la función de resta."""
        assert self.calc.restar(5, 3) == 2
        assert self.calc.restar(1, 1) == 0
        assert self.calc.restar(-1, -1) == 0
        assert self.calc.restar(10, 15) == -5
        assert self.calc.restar(7.5, 2.5) == 5.0
    
    def test_multiplicar(self):
        """Prueba la función de multiplicación."""
        assert self.calc.multiplicar(3, 4) == 12
        assert self.calc.multiplicar(-2, 3) == -6
        assert self.calc.multiplicar(0, 100) == 0
        assert self.calc.multiplicar(-5, -2) == 10
        assert self.calc.multiplicar(2.5, 4) == 10.0
    
    def test_dividir(self):
        """Prueba la función de división."""
        assert self.calc.dividir(10, 2) == 5
        assert self.calc.dividir(-6, 3) == -2
        assert self.calc.dividir(0, 5) == 0
        assert self.calc.dividir(-8, -2) == 4
        assert self.calc.dividir(7.5, 2.5) == 3.0
    
    def test_dividir_por_cero(self):
        """Prueba que la división por cero lance una excepción."""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.dividir(10, 0)
        
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.dividir(-5, 0)
    
    def test_potencia(self):
        """Prueba la función de potencia."""
        assert self.calc.potencia(2, 3) == 8
        assert self.calc.potencia(5, 0) == 1
        assert self.calc.potencia(3, 2) == 9
        assert self.calc.potencia(-2, 2) == 4
        assert self.calc.potencia(2, -1) == 0.5
    
    def test_porcentaje(self):
        """Prueba la función de porcentaje."""
        assert self.calc.porcentaje(100, 20) == 20
        assert self.calc.porcentaje(50, 10) == 5
        assert self.calc.porcentaje(200, 15) == 30
        assert self.calc.porcentaje(0, 50) == 0
        assert self.calc.porcentaje(80, 25) == 20


class TestCalculadoraIntegracion:
    """Pruebas de integración para la calculadora."""
    
    def setup_method(self):
        """Configuración antes de cada prueba."""
        self.calc = Calculadora()
    
    def test_operaciones_combinadas(self):
        """Prueba operaciones matemáticas combinadas."""
        resultado = self.calc.multiplicar(self.calc.sumar(2, 3), 4)
        assert resultado == 20
        
        resultado = self.calc.dividir(self.calc.restar(10, 5), 2)
        assert resultado == 2.5
        
        # 2^3 + 10% de 50 = 8 + 5 = 13
        potencia = self.calc.potencia(2, 3)
        porcentaje = self.calc.porcentaje(50, 10)
        resultado = self.calc.sumar(potencia, porcentaje)
        assert resultado == 13
    
    def test_casos_borde(self):
        """Prueba casos borde y extremos."""
        assert self.calc.sumar(999999, 1) == 1000000
        
        resultado = self.calc.sumar(0.1, 0.2)
        assert abs(resultado - 0.3) < 0.0001  # Debido a precisión de punto flotante
        
        assert self.calc.multiplicar(1000, 0) == 0
        assert self.calc.sumar(0, 0) == 0
