#type: ignore
import time
import board
import digitalio 
import analogio

sensor = analogio.AnalogIn(board.A0)

with open("/data.csv", "a") as datalog:
    while True:
        print(sensor.value)
        datalog.write(f"{sensor.value}\n")
        datalog.flush()
        time.sleep(1)
