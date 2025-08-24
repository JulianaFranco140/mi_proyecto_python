# Archivo __init__.py para hacer que src sea un paquete Python
"""
Paquete de calculadora simple para demostrar GitHub Actions.
"""

from .calculadora import Calculadora

__version__ = "1.0.0"
__author__ = "Tu Nombre"

__all__ = ["Calculadora"]
