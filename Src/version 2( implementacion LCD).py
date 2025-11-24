from machine import Pin, ADC, I2C
import dht
import time
from i2c_lcd import I2cLcd

# LCD I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x23, 2, 16)

# Sensores
mq = ADC(Pin(26))                 
dht_sensor = dht.DHT11(Pin(15))   

UMBRAL_1 = 25000
UMBRAL_2 = 35000

lcd.clear()
lcd.putstr("Iniciando...")
time.sleep(2)

while True:
    gas = mq.read_u16()
    dht_sensor.measure()	
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()

    if gas < UMBRAL_1:
        estado = "FRESCA"
    elif gas < UMBRAL_2:
        estado = "MADURA"
    else:
        estado = "DESCOMP."

    print("Gas:", gas)
    print("Temperatura:", temp, "°C")
    print("Humedad:", hum, "%")
    print("Estado:", estado)
    print("------------------------")

    lcd.clear()
    lcd.putstr("G:{} T:{}".format(gas, temp))
    lcd.move_to(0, 1)
    lcd.putstr("H:{}% {}".format(hum, estado))

    time.sleep(2)


