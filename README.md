# Calculadora Simple - Proyecto de Ejemplo para GitHub Actions

Un proyecto Python simple para demostrar cómo implementar y usar GitHub Actions para CI/CD.

## 🎯 Propósito

Este proyecto fue creado específicamente para:
- Aprender GitHub Actions de forma práctica
- Entender el flujo de CI/CD en Python
- Probar automatización de pruebas y análisis de código
- Servir como base para proyectos más complejos

## 🧮 Funcionalidades

La calculadora incluye las siguientes operaciones:
- ➕ Suma
- ➖ Resta  
- ✖️ Multiplicación
- ➗ División (con validación de división por cero)
- 🔢 Potencia
- 📊 Porcentaje

## 🏗️ Estructura del Proyecto

```
mi-proyecto-python/
├── .github/
│   └── workflows/
│       └── python-ci.yml      # Workflow de GitHub Actions
├── src/
│   ├── __init__.py
│   └── calculadora.py         # Código principal
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py    # Pruebas unitarias
├── requirements.txt           # Dependencias de producción
├── requirements-dev.txt       # Dependencias de desarrollo
├── .gitignore
└── README.md
```

## 🚀 Uso Local

### Prerequisitos
- Python 3.9+ instalado
- pip (incluido con Python)

### Instalación

```bash
# Clonar o descargar el proyecto
cd mi-proyecto-python

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

### Ejecutar el programa

```bash
python src/calculadora.py
```

### Ejecutar las pruebas

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con reporte de cobertura
pytest --cov=src/

# Ejecutar con reporte HTML
pytest --cov=src/ --cov-report=html
```

### Análisis de código

```bash
# Verificar estilo de código
flake8 src/

# Escaneo de seguridad
bandit -r src/

# Verificar dependencias
safety check
```

## 🔄 GitHub Actions

Este proyecto incluye un workflow completo que se ejecuta automáticamente en:
- Push a las ramas `main` o `develop`
- Pull requests hacia `main`

### Lo que hace el workflow:

1. **Pruebas en múltiples versiones de Python** (3.9, 3.10, 3.11)
2. **Análisis de código** con flake8
3. **Ejecución de pruebas** con pytest
4. **Reporte de cobertura** de código
5. **Escaneo de seguridad** con bandit y safety
6. **Generación de artefactos** con reportes

### Ver los resultados:

1. Ve a tu repositorio en GitHub
2. Pestaña **Actions**
3. Selecciona la ejecución más reciente
4. Revisa los logs y reportes generados

## 📊 Métricas de Calidad

El proyecto mantiene estos estándares:
- ✅ Cobertura de pruebas: >90%
- ✅ Sin vulnerabilidades de seguridad
- ✅ Código limpio según flake8
- ✅ Todas las pruebas pasan

## 🔧 Personalización

Para adaptar este proyecto a tus necesidades:

1. **Modificar el código**: Edita `src/calculadora.py`
2. **Agregar más pruebas**: Amplía `tests/test_calculadora.py`
3. **Cambiar dependencias**: Actualiza `requirements.txt`
4. **Ajustar el workflow**: Modifica `.github/workflows/python-ci.yml`

## 📝 Próximos Pasos

Ideas para expandir el proyecto:
- Agregar interfaz gráfica con tkinter
- Crear API REST con Flask/FastAPI
- Implementar operaciones matemáticas avanzadas
- Agregar logging y manejo de errores
- Crear documentación con Sphinx

## 🤝 Contribuciones

Este es un proyecto de aprendizaje. Siéntete libre de:
- Hacer fork del proyecto
- Crear nuevas funcionalidades
- Mejorar las pruebas
- Optimizar el workflow de GitHub Actions

---

**¡Feliz aprendizaje con GitHub Actions! 🎉**
