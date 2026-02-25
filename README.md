# 🩺 Doctor Python: Sistema de Agendamiento Médico

Este es un sistema de gestión de citas médicas desarrollado en **Python** como Actividad de Evaluación del módulo 3 del Bootcamp "Desarrollo de aplicaciones Full Stack Python Trainee v2.0". 
Permite administrar el ciclo completo de una atención (CRUD), asegurando la integridad de los datos mediante validaciones avanzadas de formatos chilenos y estándares internacionales.

## 🚀 Características Principales

- **Validación de RUT:** Algoritmo de módulo 11 integrado para verificar RUTs chilenos reales.
- **Formateo Automático:** Estandarización de RUT (XXXXXXX-X) y nombres (Capitalización).
- **Validaciones en Tiempo Real:**
  - Correo electrónico con formato `@dominio.com`.
  - Edad restringida a rangos lógicos (0-120 años).
  - Fechas y horas reales mediante el módulo `datetime`.
- **Gestión Inteligente:**
  - Prevención de duplicados por RUT.
  - Opción de modificar cita existente si se detecta un reingreso.
  - Ordenamiento cronológico automático de la agenda.

## 🛠️ Requisitos

- Python 3.x
- Librerías estándar (no requiere instalaciones externas):
  - `datetime`

## 📋 Uso del Sistema

1. Clona el repositorio o descarga el archivo `.py`.
2. Ejecuta el programa:
   ```bash
   python nombre_de_tu_archivo.py
