from machine import Pin, ADC, I2C
import dht
import time
import urequests
import network
from i2c_lcd import I2cLcd

# LCD I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x23, 2, 16)
lcd.clear()

# Sensores
mq = ADC(Pin(26))
dht_sensor = dht.DHT11(Pin(15))

UMBRAL_1 = 7000
UMBRAL_2 = 10000

# Credenciales WiFi
WIFI_SSID = "Xiaomi de Cielo"
WIFI_PASSWORD = "Solvalle18?"

# Ubidots
UBIDOTS_TOKEN = "BBUS-1RVDMlCwHd0mLejxYj61aicC8GuoIo"
DEVICE_LABEL = "raspberry"
VARIABLE_LABEL = "regis-pico"

# ---- FUNCIONES ----

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    print("Conectando a WiFi...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)

    print("\nWiFi conectado!")
    print("IP:", wlan.ifconfig()[0])


def enviar_a_ubidots(gas, temp, hum):
    url = f"https://stem.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "gas": gas,
        "temperatura": temp,
        "humedad": hum,
    }

    print("Enviando a Ubidots:", payload)
    try:
        urequests.post(url, json=payload, headers=headers).close()
        print("OK enviado\n")
    except:
        print("Error al enviar a Ubidots\n")


# ---- PROGRAMA PRINCIPAL ----

lcd.clear()
lcd.putstr("Iniciando...")
time.sleep(2)

# Conectar WiFi al inicio
conectar_wifi()

while True:
    gas = mq.read_u16()
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()

    # Determinar estado
    if gas < UMBRAL_1:
        estado = "FRESCA"
    elif gas < UMBRAL_2:
        estado = "MADURA"
    else:
        estado = "DESCOMPUESTA"
        enviar_a_ubidots(gas, temp, hum)

    # Mostrar SIEMPRE en LCD
    lcd.clear()
    lcd.putstr(f"G:{gas} T:{temp}")
    lcd.move_to(0, 1)
    lcd.putstr(f"H:{hum}% {estado}")

    # Mostrar también en consola
    print("Gas:", gas)
    print("Temp:", temp, "°C")
    print("Humedad:", hum, "%")
    print("Estado:", estado)
    print("------------------------")

    time.sleep(2)
