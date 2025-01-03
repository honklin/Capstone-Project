#type: ignore
import time
import board
import digitalio 
import analogio

sensor1 = analogio.AnalogIn(board.A0)
sensor2 = analogio.AnalogIn(board.A1)
sensor3 = analogio.AnalogIn(board.A2)

with open("/data.csv", "w") as datalog:
    while True:
        print(sensor1.value)
        print(sensor2.value)
        print(sensor3.value)
        datalog.write(f"{sensor1.value, sensor2.value, sensor3.value}\n")
        datalog.flush()
        time.sleep(.5)
