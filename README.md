# Proyecto de Monitoreo de Temperatura IoT: Batch vs Streaming

Este proyecto implementa un sistema en Python para el procesamiento, análisis y visualización de lecturas de temperatura provenientes de dispositivos e instrumentos IoT. El sistema permite procesar datos bajo dos paradigmas clave del Big Data: **Procesamiento en Lote (Batch)** para volúmenes masivos de datos históricos y **Procesamiento en Tiempo Real (Streaming)** para la ingesta continua de eventos.

---

## Dataset

* **Nombre del dataset:** IoT Devices Temperature Readings
* **Fuente:** [Kaggle - IoT Devices Temperature Readings](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)
* **Descripción breve:** Contiene lecturas de temperatura registradas por dispositivos e sensores IoT instalados en entornos interiores y exteriores. Incluye identificadores de dispositivo, marcas de tiempo (*timestamps*) y los valores numéricos de temperatura en grados Celsius.

---

## Objetivo

El objetivo principal es comparar la eficiencia y el comportamiento del análisis de datos masivos mediante dos enfoques de procesamiento:
1. **Modo Batch:** Analizar eficientemente un gran volumen de datos históricos (más de 97,000 registros) calculando métricas globales (promedio, máximo, mínimo) y la evolución del promedio acumulado en un solo paso.
2. **Modo Streaming:** Evaluar el impacto de la llegada secuencial de datos en tiempo real, actualizando métricas descriptivas y visualizaciones gráficas de manera interactiva a medida que ocurren los eventos.

---

## Requisitos

* **Python:** Versión 3.10 o superior.
* **Dependencias:** Las librerías requeridas se encuentran detalladas en el archivo `requirements.txt`:
  * `matplotlib`

---

## Instalación

Clonar el repositorio:
```bash
git https://github.com/annadelahoz/proyecto-big-data
