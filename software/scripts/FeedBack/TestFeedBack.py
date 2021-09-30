import dac, time
import Adafruit_BBIO.ADC as ADC

ADC.setup()

dac.on(28)
dac.config(28)

while(1):
    for voltage in [3.3, 5, 7.7, 8, -3, -5, -8]:
        dac.writeVolts(voltage) #int(raw_input("Digite o valor: ")))
        time.sleep(1)
        print("Valor escrito: %s\n")
        time.sleep(2)
        raw_input("continue")

