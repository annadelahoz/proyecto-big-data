import os
import sys
import csv
import matplotlib.pyplot as plt

# FUNCIONES DE VALIDACIÓN Y PROCESAMIENTO

def validar_temperatura(valor_str):
    """Valida y convierte el valor numérico de temperatura."""
    val = float(str(valor_str).strip())
    if val < -50.0 or val > 100.0:
        raise ValueError("Temperatura fuera de rango operativo (-50°C a 100°C).")
    return val


def obtener_lecturas_batch():
    """Solicita al usuario una lista por comas, la ruta de un CSV/TXT real o usa datos de prueba."""
    print("\n   [1] Ingresar datos manuales separados por coma")
    print("   [2] Cargar datos desde la ruta de un archivo (.csv o .txt)")
    print("   [Presiona Enter para usar datos de prueba automáticos]")
    
    opcion = input("\nSelecciona método de ingreso (1, 2 o Enter) > ").strip()
    lecturas = []

    # Opción 1: Lista manual separada por comas
    if opcion == '1':
        cadena = input("\nIngresa las temperaturas separadas por comas (ej. 22.4, 23.5, 25.1): ").strip()
        elementos = cadena.split(',')
        for item in elementos:
            if item.strip():
                try:
                    val = validar_temperatura(item)
                    lecturas.append(val)
                except ValueError as e:
                    print(f"   [!] Dato ignorado '{item.strip()}': {e}")

    # Opción 2: Ruta de archivo CSV o TXT real
    elif opcion == '2':
        ruta_archivo = input("\nIngresa la ruta del archivo (.csv o .txt): ").strip()
        if os.path.exists(ruta_archivo):
            try:
                print("   [i] Leyendo y procesando archivo, por favor espera...")
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    lector_dict = csv.DictReader(f)
                    
                    columna_temp = None
                    posibles_nombres = ['temp', 'temperature', 'temperatura']
                    for h in lector_dict.fieldnames or []:
                        if h.lower() in posibles_nombres:
                            columna_temp = h
                            break

                    if columna_temp:
                        print(f"   [i] Columna detectada automáticamente: '{columna_temp}'")
                        for fila in lector_dict:
                            try:
                                val = validar_temperatura(fila[columna_temp])
                                lecturas.append(val)
                            except (ValueError, KeyError):
                                continue
                    else:
                        f.seek(0)
                        for linea in f:
                            subelementos = linea.strip().split(',')
                            for item in subelementos:
                                if item.strip():
                                    try:
                                        val = validar_temperatura(item)
                                        lecturas.append(val)
                                    except ValueError:
                                        continue
            except Exception as e:
                print(f"   [!] Error al leer el archivo: {e}")
        else:
            print(f"   [!] La ruta '{ruta_archivo}' no existe.")

    # Opción por defecto
    if not lecturas:
        print("\n[i] Cargando lote de prueba predeterminado...")
        lecturas = [22.4, 23.1, 25.0, 24.8, 26.2, 21.5, 23.9, 27.1, 24.0]

    return lecturas


def modo_batch():
    """Modo Batch: Procesa el lote completo de lecturas y genera estadísticas finales de forma ultra rápida O(N)."""
    print("\n           MODO BATCH (PROCESAMIENTO EN LOTE)")
    
    lecturas = obtener_lecturas_batch()

    if not lecturas:
        print("\n[!] No hay lecturas válidas para procesar.")
        return

    total_registros = len(lecturas)
    promedio_global = sum(lecturas) / total_registros
    maximo_global = max(lecturas)
    minimo_global = min(lecturas)

    # OPTIMIZACIÓN O(N): Cálculo de promedios acumulados continuo súper rápido
    suma_acumulada = 0.0
    promedios_acumulados = []
    for idx, val in enumerate(lecturas, 1):
        suma_acumulada += val
        promedios_acumulados.append(suma_acumulada / idx)

    eje_x = list(range(1, total_registros + 1))

    print("\n" + "="*50)
    print("      RESULTADOS DEL PROCESAMIENTO EN BATCH")
    print("="*50)
    print(f"   Total de registros procesados : {total_registros}")
    print(f"   Temperatura Promedio          : {promedio_global:.2f} °C")
    print(f"   Temperatura Máxima            : {maximo_global:.2f} °C")
    print(f"   Temperatura Mínima            : {minimo_global:.2f} °C")
    print("-"*50 + "\n")

    plt.ioff()
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Dibujar líneas de datos
    ax.plot(eje_x, lecturas, color='#2980b9', linewidth=1, alpha=0.7, label='Lecturas Batch (°C)')
    ax.plot(eje_x, promedios_acumulados, color='#e67e22', linestyle='--', linewidth=2, label=f'Promedio acumulado final ({promedio_global:.2f} °C)')
    
    ax.axhline(maximo_global, color='#c0392b', linestyle=':', linewidth=1.5, label=f'Máx ({maximo_global:.2f} °C)')
    ax.axhline(minimo_global, color='#27ae60', linestyle=':', linewidth=1.5, label=f'Mín ({minimo_global:.2f} °C)')

    ax.set_title(f"Procesamiento Batch: Análisis de {total_registros:,} Muestras", fontsize=12, fontweight='bold')
    ax.set_xlabel("Índice de Muestra")
    ax.set_ylabel("Temperatura (°C)")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    print("[i] Abriendo gráfica... Cierra la ventana emergente para regresar al menú principal.")
    plt.show()


def modo_streaming():
    """Modo Streaming: Recibe eventos uno a uno y actualiza métricas y gráfica en tiempo real."""
    print("\n        MODO STREAMING (TIEMPO REAL EN TERMINAL)")
    print("Escribe un valor numérico de temperatura y presiona Enter.")
    print("Escribe 'r' para reiniciar el flujo o 'q' para volver al menú principal.\n")

    streaming_data = {
        'count': 0, 'suma': 0.0,
        'maximo': float('-inf'), 'minimo': float('inf'),
        'recorridos_x': [], 'lecturas_y': [], 'promedios_y': []
    }

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 4))

    while True:
        try:
            entrada = input("Temp (°C) > ").strip()
            
            if entrada.lower() == 'q':
                plt.close(fig)
                print("[i] Finalizando sesión de streaming...\n")
                break
            elif entrada.lower() == 'r':
                streaming_data = {
                    'count': 0, 'suma': 0.0, 'maximo': float('-inf'),
                    'minimo': float('inf'), 'recorridos_x': [], 'lecturas_y': [], 'promedios_y': []
                }
                ax.clear()
                plt.draw()
                print("[i] Flujo reiniciado. Ingresa nuevos registros.\n")
                continue

            valor = validar_temperatura(entrada)

            s = streaming_data
            s['count'] += 1
            s['suma'] += valor
            if valor > s['maximo']: s['maximo'] = valor
            if valor < s['minimo']: s['minimo'] = valor
            promedio = s['suma'] / s['count']

            s['recorridos_x'].append(s['count'])
            s['lecturas_y'].append(valor)
            s['promedios_y'].append(promedio)

            print(f"  └─► [EVENTO #{s['count']:02d}] Registrado: {valor:.2f} °C")
            print(f"      [Métricas] Promedio: {promedio:.2f} °C | Máx: {s['maximo']:.2f} °C | Mín: {s['minimo']:.2f} °C\n")

            ax.clear()
            ax.plot(s['recorridos_x'], s['lecturas_y'], marker='o', color='#27ae60', linewidth=2, label='Lectura actual (°C)')
            ax.plot(s['recorridos_x'], s['promedios_y'], color='#e67e22', linestyle='--', label=f'Promedio ({promedio:.2f} °C)')
            ax.scatter([s['count']], [valor], color='red', s=100, zorder=5, label='Último evento')

            ax.set_xticks(s['recorridos_x'])
            if s['count'] == 1:
                ax.set_xlim(0.5, 1.5)
            else:
                ax.set_xlim(0.8, s['count'] + 0.2)

            ax.set_title(f"Streaming en Tiempo Real: Muestra #{s['count']}", fontsize=12, fontweight='bold')
            ax.set_xlabel("Secuencia de Eventos (Llegada)")
            ax.set_ylabel("Temperatura (°C)")
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc='upper left')
            
            plt.tight_layout()
            plt.draw()
            plt.pause(0.1)

        except ValueError as e:
            print(f"[!] Error: {e}\n")
        except Exception as e:
            print(f"[!] Error inesperado: {e}\n")

# MENÚ PRINCIPAL DE NAVEGACIÓN

def main():
    while True:
        print("\n==========================================================")
        print("    SISTEMA DE MONITOREO DE TEMPERATURA: BATCH VS STREAMING    ")
        print("==========================================================")
        print(" Selecciona la modalidad de procesamiento:")
        print("  [1] Procesamiento en Batch (Lote completo de datos)")
        print("  [2] Procesamiento en Streaming (Entrada en tiempo real)")
        print("  [3] Salir")

        opcion = input("\nOpción (1-3) > ").strip()

        if opcion == '1':
            modo_batch()
        elif opcion == '2':
            modo_streaming()
        elif opcion == '3':
            print("\nSaliendo del sistema...")
            sys.exit(0)
        else:
            print("\n[!] Opción no válida. Por favor ingresa 1, 2 o 3.")

if __name__ == "__main__":
    main()