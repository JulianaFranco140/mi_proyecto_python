#!/usr/bin/env python3
"""
Script para probar el proyecto localmente antes de subirlo a GitHub.
Simula lo que hace GitHub Actions.
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Ejecuta un comando y muestra el resultado."""
    print(f"\n{'='*50}")
    print(f"🔄 {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print("✅ ÉXITO")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ ERROR")
        print(e.stdout)
        print(e.stderr)
        return False


def main():
    """Función principal para ejecutar todas las verificaciones."""
    print("🧪 SIMULANDO GITHUB ACTIONS LOCALMENTE")
    print("="*60)
    
    # Cambiar al directorio del proyecto
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    tests_passed = 0
    total_tests = 5
    
    # 1. Verificar que Python funciona
    if run_command("python --version", "Verificando versión de Python"):
        tests_passed += 1
    
    # 2. Instalar dependencias
    if run_command("pip install -r requirements-dev.txt", "Instalando dependencias"):
        tests_passed += 1
    
    # 3. Análisis de código con flake8
    if run_command("flake8 src/ --max-line-length=100", "Análisis de código con flake8"):
        tests_passed += 1
    
    # 4. Ejecutar pruebas
    if run_command("pytest tests/ -v --cov=src/", "Ejecutando pruebas unitarias"):
        tests_passed += 1
    
    # 5. Escaneo de seguridad
    if run_command("bandit -r src/", "Escaneo de seguridad con bandit"):
        tests_passed += 1
    
    # Resumen final
    print(f"\n{'='*60}")
    print(f"📊 RESUMEN FINAL")
    print(f"{'='*60}")
    print(f"Pruebas pasadas: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("🎉 ¡Todas las verificaciones pasaron!")
        print("✅ Tu proyecto está listo para GitHub Actions")
    else:
        print("⚠️  Algunas verificaciones fallaron")
        print("❌ Revisa los errores antes de subir a GitHub")
    
    return tests_passed == total_tests


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
