from machine import Pin, ADC
import dht
import time

# Sensores
mq = ADC(Pin(26))         # MQ-135 en GP26 (ADC0)
dht_sensor = dht.DHT11(Pin(15))  # DHT11 en GP15

# Umbrales simples de ejemplo
UMBRAL_1 = 25000
UMBRAL_2 = 35000

while True:

    # Lectura MQ-135
    gas = mq.read_u16()

    # Lectura DHT11
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()

    # Determinar estado
    if gas < UMBRAL_1:
        estado = "FRESCA"
    elif gas < UMBRAL_2:
        estado = "MADURA"
    else:
        estado = "DESCOMPOSICION"

    # Mostrar valores
    print("Gas:", gas)
    print("Temperatura:", temp, "°C")
    print("Humedad:", hum, "%")
    print("Estado:", estado)
    print("------------------------")

    time.sleep(2)
