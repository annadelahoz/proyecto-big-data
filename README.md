# Sistema de Monitoreo de Temperatura IoT: Batch vs Streaming

Este proyecto implementa un sistema desarrollado en Python para procesar, analizar y visualizad datos masivos de temperatura provenientes de dispositivos IoT. Se abordan dos modalidades fundamentales de procesamiento en Big Data: **Batch (Procesamiento en Lote)** para análisis histórico masivo y **Streaming (Procesamiento en Tiempo Real)** para la ingesta continua de eventos.

## Dataset

* **Nombre del dataset:** IoT Devices Temperature Readings
* **Fuente:** [Kaggle - IoT Devices Temperature Readings](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)
* **Descripción breve:** Contiene lecturas de temperatura recopiladas por sensores IoT ubicados en entornos interiores y exteriores, incluyendo marcas de tiempo (*timestamps*), identificadores de dispositivos y lecturas numéricas en grados Celsius (°C).

## Objetivo

Analizar y comparar la eficiencia entre el procesamiento de grandes volúmenes de datos históricos en lote (Batch) y la ingesta interactiva en tiempo real (Streaming), evaluando el impacto en el cálculo de métricas (promedio, máximos y mínimos) y la generación de visualizaciones dinámicas.

## Requisitos

Indica que se requiere Python 3.10 o superior y las dependencias incluidas en `requirements.txt`:
* `matplotlib`

## Instalación

Explica cómo clonar el repositorio:

```bash
git clone [https://github.com/annadelahoz/proyecto-big-data.git](https://github.com/annadelahoz/proyecto-big-data.git)
Entrar al proyecto:Bashcd proyecto-big-data
Crear el entorno:Bashpython -m venv .venv
Activarlo e instalar dependencias:PowerShell.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
EjecuciónIndica exactamente cómo ejecutar tu proyecto:Bashpython src/main.py
Análisis realizados
Análisis Batch: Procesamiento masivo  sobre más de 97,000 lecturas históricas almacenadas en data/IOT-temp.csv, calculando la temperatura promedio global, valores máximos y mínimos, junto con la tendencia del promedio acumulado mediante gráficos estadísticos de Matplotlib.Análisis en Streaming: Simulación de recepción de eventos uno a uno en tiempo real, recalculando dinámicamente las métricas de monitoreo y actualizando la gráfica en vivo con cada nueva lectura ingresada.
Resultados y conclusiones
Conclusiones individuales
Anamaria"El desarrollo del módulo Batch me permitió comprender la importancia crítica de la optimización algorítmica en Big Data. Inicialmente, el procesamiento iterativo provocaba una complejidad  que congelaba la aplicación; al refactorizar el código hacia un acumulador de complejidad, logramos procesar las 97,000 lecturas en menos de un segundo, demostrando que la eficiencia del código es tan vital como la capacidad de procesamiento del hardware."
Alejandra"Mediante la implementación del modo Streaming identifiqué las ventajas operativas de la ingesta de datos en tiempo real. A diferencia del enfoque por lotes, el streaming permite la detección inmediata de fluctuaciones críticas de temperatura en el instante en que suceden, siendo una solución indispensable para sistemas de monitoreo de infraestructura IoT donde la baja latencia es prioritaria."
Charbel"El proyecto facilitó una comparación práctica entre ambos paradigmas de procesamiento. Mientras que la modalidad Batch es ideal para auditorías pasadas, reportería y análisis descriptivo a largo plazo, el esquema de Streaming destaca en entornos reactivos que demandan alertas en vivo y toma de decisiones automatizada."
Conclusión general
En conclusión, este proyecto demostró que el procesamiento Batch y el procesamiento en Streaming son enfoques complementarios dentro de las arquitecturas de Big Data. La integración de ambos paradigmas permite combinar el análisis exhaustivo de volúmenes históricos de datos con la capacidad de respuesta inmediata ante eventos continuos en tiempo real, garantizando una solución integral para el monitoreo de dispositivos IoT.
