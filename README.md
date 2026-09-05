# 🚁 Motor de Simulación 3D de Telemetría

**Instituto Superior Tecnológico Cordillera**
**Carrera:** Desarrollo de Software (Primero A)
**Asignatura:** Matemática Aplicada
**Docente:** Ing. Andrés Cangui H.
**Integrantes:** Katherine Castillo, Sara [Apellido], Matías [Apellido]

---

## 🎯 Objetivo General
Desarrollar un motor de simulación 3D en Python que modele la trayectoria, la velocidad de cambio instantánea (derivadas), la optimización de vuelo y la acumulación total de transferencia de datos (integral definida) de un vehículo aéreo no tripulado (Dron), aplicando el Teorema Fundamental del Cálculo en tiempo real.

## 🧮 Modelos Matemáticos Utilizados

### 1. Velocidad Instantánea y Optimización (Primera Derivada)
La trayectoria de altitud del vuelo de prueba está dada por la función:
$$h(t) = -0.1t^4 + 1.6t^3 - 7.2t^2 + 10t + 5$$

Aplicando reglas de derivación, obtenemos la velocidad instantánea:
$$v(t) = h'(t) = -0.4t^3 + 4.8t^2 - 14.4t + 10$$

### 2. Antiderivada (Temperatura del Motor)
La tasa instantánea de calentamiento registrada por el sensor secundario es:
$$T'(t) = 0.6t^2 - 2t + 4$$

Integrando y resolviendo el problema de valor inicial para $T(0) = 22^\circ C$, la función de temperatura es:
$$T(t) = 0.2t^3 - t^2 + 4t + 22$$

### 3. Integral Definida (Acumulación de Datos de Cámara 4K)
El consumo de ancho de banda en MB/s está dado por:
$$D(t) = 3t^2 + 2t + 5$$

Aplicando el Teorema Fundamental del Cálculo para hallar los datos totales transferidos en el intervalo de $t=1$ a $t=4$ segundos:
$$\int_{1}^{4} (3t^2 + 2t + 5) dt = \left[ t^3 + t^2 + 5t \right]_{1}^{4} = 93 \text{ MB}$$

---

## 💻 Simulación 3D y Telemetría en Tiempo Real

El script principal `dron_simulation3d.py` fue desarrollado en Python utilizando `vpython`, `numpy` y `matplotlib`. 

### 1. Resultados Analíticos (Consola)
Cálculos exactos de velocidad, optimización de vuelo y acumulación de datos impresos por el programa:

![Resultados Analíticos](An%C3%A1lisis%20Anal%C3%ADtico.png)
> *Figura 1: Resultados matemáticos calculados por el motor.*

### 2. Interfaz 3D del Dron
Malla tridimensional siguiendo las coordenadas calculadas y el HUD de telemetría desplegando altitud, velocidad y datos acumulados:

![Recorrido del Dron](Recorrido%20del%20drom.png)
> *Figura 2: Entorno 3D renderizado con VPython.*

### 3. Análisis Estadístico (Gráficas)
Al finalizar el vuelo, el sistema genera las gráficas de comportamiento evaluando la posición, la tangente de velocidad y el área bajo la curva:

![Gráfica del Movimiento](Gr%C3%A1fica%20del%20movimiento%20del%20drom.png)
> *Figura 3: Resumen analítico generado con Matplotlib.*
