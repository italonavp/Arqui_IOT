# 🍌 Sistema IoT de Monitoreo del Estado de Frutas ("nombre proyecto")
## 💻 Curso: Arquitectura del Computador
## 👩‍💻 Integrantes:

#### Italo Navarrete
#### Nahim Patiño



## 📆 Fecha

Noviembre 2025

## ✒ 1. Resumen del Proyecto

El sistema BananaSense permite monitorear el estado de madurez o descomposición del plátano mediante la medición de gases y temperatura.
Utiliza un sensor MQ-135 para detectar la concentración de gases (como CO₂ y compuestos orgánicos volátiles) y un DHT11 para registrar la temperatura ambiental.
Los datos se procesan en una Raspberry Pi Pico W, que compara los valores con dos umbrales de referencia para determinar el estado del fruto:

### 🟢 Estado 1: Por debajo de ambos umbrales → fruta fresca.

### 🟡 Estado 2: Supera el primer umbral → fruta madura.

### 🔴 Estado 3: Supera ambos umbrales → fruta en mal estado.

Si se detecta un estado de posible deterioro, el sistema envía los datos a la nube mediante ThingSpeak.

## 💿 2. Arquitectura del Sistema
### Flujo general:

-El sensor MQ-135 detecta la concentración de gases.
-El sensor DHT11 mide la temperatura.
-La Pico W procesa los datos y compara con los umbrales.
-Se determina el estado de la fruta.
-Si el valor supera los límites, se enciende el LED de alerta.
-Los datos se envían a la plataforma ThingSpeak para su monitoreo remoto.

📊 El diagrama de bloques se encuentra en /docs/arquitectura.png

## 🧠 3. Componentes Utilizados
Componente	Descripción	Imagen
Raspberry Pi Pico W	Microcontrolador principal con conectividad WiFi.	<img src="./docs/pico.jpg" width="180">
Sensor MQ-135	Mide gases relacionados con la madurez o descomposición de la fruta.	<img src="./docs/mq135.jpg" width="180">
Sensor DHT11	Mide temperatura y humedad ambiental.	<img src="./docs/dht11.jpg" width="180">
LED + resistencia 220Ω	Señal visual de alerta ante valores fuera de rango.	<img src="./docs/led.jpg" width="180">
## 💻 4. Código Fuente

📂 Ubicación: /src/main.py

🗒️ El código completo está disponible en el repositorio con comentarios detallados.

## 🧩 5. Diagrama de Flujo

-pendiente de subir imagen-
### Descripción:

Inicio

Lectura de sensores (MQ-135 y DHT11)

Comparación con umbrales

Determinación de estado

Activar LED / Enviar datos a ThingSpeak

Repetir

## 🔌 6. Diagrama de Conexiones (Fritzing)

Elemento	Pin Pico	Descripción
MQ-135	GP26 (ADC0)	Entrada analógica de gas
DHT11	GP16	Temperatura y humedad
LED	GP15	Indicador de estado
GND / VCC	–	Alimentación y referencia

## ☁️ 7. Conectividad IoT

Plataforma: nombre plat

Método: Envío HTTP GET mediante WiFi

Campos registrados: Gas (ppm), Temperatura (°C), Estado

Frecuencia: Cuando el valor cambia de estado

## 🧱 8. Diseño 3D del Case

📁 /3D/case.stl
Diseñado en... .

## 🎥 9. Video Demostrativo

🔗 Video en YouTube
 (pendiente de subir)
Duración: 5 min
Contenido: presentación, prototipo, funcionamiento y explicación técnica.

## 📊 10. Póster Técnico

📁 /poster/poster.pdf
Formato A2 – incluye metodología, resultados, arquitectura e impacto.

## 🗂️ 11. Gestión del Proyecto

Documento colaborativo de tareas, avances y fechas.
📎 Google Sheets – Gestión del Proyecto

## 🧾 12. Conclusiones

Se logró implementar un sistema funcional para detectar el estado de madurez del plátano usando sensores IoT.

El sistema puede escalarse para diferentes tipos de frutas y entornos.

Futuras mejoras: calibración del sensor MQ-135, conexión a una app móvil y almacenamiento histórico de datos.

## 🔗 13. Referencias

Raspberry Pi Pico W Documentation

MQ-135 Datasheet

DHT11 Datasheet
