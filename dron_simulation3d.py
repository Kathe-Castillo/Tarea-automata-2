# Importa la librería numpy para generar y manejar arreglos numéricos (vectores de tiempo)
import numpy as np 
# Importa el módulo pyplot de matplotlib para renderizar las 3 gráficas estáticas al final
import matplotlib.pyplot as plt 
# Importa los elementos específicos de vpython para construir el entorno 3D y el renderizado en pantalla
from vpython import box, vector, rate, label, color, canvas 

# ==========================================
# 1. DEFINICIÓN DE FUNCIONES MATEMÁTICAS
# ==========================================

def h(t):
    # Retorna la altitud en metros evaluando el polinomio de trayectoria según el tiempo t
    return -0.1*t**4 + 1.6*t**3 - 7.2*t**2 + 10*t + 5

def v(t):
    # Retorna la velocidad instantánea en m/s; corresponde a la primera derivada h'(t)
    return -0.4*t**3 + 4.8*t**2 - 14.4*t + 10

def D(t):
    # Retorna la tasa instantánea de transferencia de datos de la cámara en MB/s
    return 3*t**2 + 2*t + 5

def data_accumulated(t):
    # Retorna el volumen total calculando la integral definida de D(t) de forma dinámica
    return (t**3 + t**2 + 5*t)


# ==========================================
# 2. CONFIGURACIÓN DE ESCENA 3D Y HUD (INTERFAZ)
# ==========================================

# Crea la ventana principal de la simulación con un título personalizado y dimensiones específicas
scene = canvas(title="Simulacion 3D Dron - Telemetria", width=800, height=600)

# Renderiza la malla 3D (un objeto tipo caja/cubo) que representa al dron
# Su posición inicial en Y está dada por la función h(0), y deja un rastro (trail) al moverse
dron = box(pos=vector(0, h(0), 0), size=vector(2,0.5,2), color=color.cyan, make_trail=True)

# Crea la etiqueta (HUD) para mostrar la altitud en tiempo real en la pantalla
hud_alt = label(pos=vector(10, 20, 0), text='Altitud: 0 m', box=False)

# Crea la etiqueta (HUD) para mostrar la velocidad instantánea (derivada) en tiempo real
hud_vel = label(pos=vector(10, 18, 0), text='Velocidad: 0 m/s', box=False)

# Crea la etiqueta (HUD) para mostrar la acumulación total de datos (integral) en tiempo real
hud_dat = label(pos=vector(10, 16, 0), text='Datos: 0 MB', box=False)


# ==========================================
# 3. BUCLE DE SIMULACIÓN EN TIEMPO REAL
# ==========================================

# Define el tiempo máximo de vuelo estipulado para la prueba
t_max = 10 
# Define el paso de tiempo (delta t) para actualizar los cuadros de la animación (cada 0.05s)
dt = 0.05 
# Inicializa la variable del tiempo actual en cero
t_current = 0 

# Inicia un ciclo que se ejecutará mientras el tiempo actual sea menor o igual al tiempo máximo estipulado
while t_current <= t_max:
    # Limita la velocidad del ciclo a 20 iteraciones (frames) por segundo para una animación fluida
    rate(20) 
    
    # Calcula la altitud actual evaluando la función matemática en el tiempo actual
    current_h = h(t_current)
    # Calcula la velocidad actual evaluando la función derivada en el tiempo actual
    current_v = v(t_current)
    
    # Actualiza las coordenadas 3D del dron; se desplaza en X para avanzar, y en Y según la altitud h(t)
    dron.pos = vector(t_current*2 - 10, current_h, 0) 
    
    # Actualiza el texto de la etiqueta HUD inyectando el valor de la altitud actual formateado a 2 decimales
    hud_alt.text = f'Altitud h(t): {current_h:.2f} m'
    # Actualiza el texto de la etiqueta HUD inyectando el valor de la velocidad actual
    hud_vel.text = f'Vel. v(t): {current_v:.2f} m/s'
    # Actualiza el texto de la etiqueta HUD con la integral evaluada dinámicamente
    hud_dat.text = f'Datos Totales: {data_accumulated(t_current):.2f} MB'
    
    # Suma el paso de tiempo (0.05) al tiempo actual para avanzar al siguiente cuadro lógico
    t_current += dt


# ==========================================
# 4. GRÁFICAS RESUMEN CON MATPLOTLIB (AL FINALIZAR)
# ==========================================

# Genera un vector con 200 puntos de tiempo espaciados uniformemente entre 0 y 10 segundos
t_arr = np.linspace(0, 10, 200)
# Evalúa la función de altitud para todos los puntos del vector de tiempo
h_arr = h(t_arr)
# Evalúa la función de velocidad para todos los puntos del vector de tiempo
v_arr = v(t_arr)
# Evalúa la función de transferencia de datos para todos los puntos del vector de tiempo
D_arr = D(t_arr)

# Crea una ventana de figura con 3 subplots (gráficas) alineados horizontalmente
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# --- Gráfica 1: Posición ---
# Dibuja la curva de posición/altitud h(t) en color azul ('b')
ax1.plot(t_arr, h_arr, 'b', label='h(t)')
ax1.set_title('Altitud del Dron') # Asigna el título de la gráfica
ax1.set_xlabel('Tiempo (s)')      # Etiqueta el eje X
ax1.set_ylabel('Altura (m)')      # Etiqueta el eje Y
ax1.grid(True)                    # Activa la cuadrícula de fondo

# --- Gráfica 2: Velocidad y Recta Tangente ---
# Almacena el valor del tiempo exacto donde se alcanza la altura máxima según los puntos críticos calculados
max_t = 7.79 
# Dibuja la curva de velocidad instantánea v(t) en color verde ('g')
ax2.plot(t_arr, v_arr, 'g', label="v(t) = h'(t)")
# Dibuja una línea horizontal punteada roja en y=0, que representa la tangente en los puntos críticos
ax2.axhline(0, color='r', linestyle='--', label='v=0 (Tangente en máx/mín)')
# Dibuja un punto rojo indicando exactamente el punto donde la velocidad es cero en el tiempo max_t
ax2.scatter(max_t, v(max_t), color='red')
ax2.set_title('Velocidad Instantánea') # Asigna el título
ax2.set_xlabel('Tiempo (s)')           # Etiqueta el eje X
ax2.grid(True)                         # Activa la cuadrícula
ax2.legend()                           # Muestra el cuadro de leyendas

# --- Gráfica 3: Transferencia de Datos y Área bajo la curva ---
# Dibuja la curva de la tasa de transferencia de datos D(t) en color negro ('k')
ax3.plot(t_arr, D_arr, 'k', label='D(t)')
# Crea un nuevo vector de tiempo estrictamente para el intervalo solicitado de t=1 a t=4
t_fill = np.linspace(1, 4, 100)
# Colorea el área bajo la curva D(t) en el intervalo definido para ilustrar la integral definida
ax3.fill_between(t_fill, D(t_fill), color='orange', alpha=0.5, label='Área = 93 MB')
ax3.set_title('Consumo de Datos') # Asigna el título
ax3.set_xlabel('Tiempo (s)')      # Etiqueta el eje X
ax3.set_ylabel('Tasa (MB/s)')     # Etiqueta el eje Y
ax3.grid(True)                    # Activa la cuadrícula
ax3.legend()                      # Muestra el cuadro de leyendas

# Ajusta el espaciado automático entre las gráficas para que no se superpongan
plt.tight_layout()

# ==========================================
# 5. IMPRESIÓN DE RESULTADOS EN CONSOLA
# ==========================================
print("========================================")
print(" RESULTADOS ANALÍTICOS")
print("========================================")
print(f"Velocidad en t=2: {v(2):.2f} m/s")
print(f"Velocidad en t=6: {v(6):.2f} m/s")
print("\nPuntos críticos:")
print(f"t1 = 1.0000 s")
print(f"h(t1) = {h(1):.4f} m")
print(f"t2 = 3.2087 s")
print(f"h(t2) = {h(3.2087):.4f} m")
print(f"t3 = 7.7913 s")
print(f"h(t3) = {h(7.7913):.4f} m")
print("\nTemperatura inicial:")
print("T(0) = 22.00 °C")
print("\nDatos transferidos entre t=1 y t=4:")
# Se calcula la diferencia exacta llamando a la función de la integral
print(f"{data_accumulated(4) - data_accumulated(1):.0f} MB")

# Abre y muestra la ventana final estática con las 3 gráficas renderizadas
plt.show()