import serial
from time import sleep, strftime, time
from gpiozero import CPUTemperature
import pygame

csv_path = "" # Custom file path here /home/scripts
csv_name = "" # Your csv name here "something.csv"
csv = csv_path+csv_name

def sound_sys(sound, infinite):
    pygame.mixer.init()
    if sound == "send":
        pygame.mixer.music.load('biosino-send.wav')
    if sound == "bioAlert":
        pygame.mixer.music.load('biosino-send.wav')
    if sound == "temp":
        pygame.mixer.music.load('temp.wav')
    if infinite == "yes":
        pygame.mixer.music.play(-1)
    else :
        pygame.mixer.music.play(1)

def write_log(order,text):
    
    with open(csv, "a") as log:
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(order),str(text)))

def send_biosino(sysOrder):
    
    arduino.write(str(sysOrder).encode())
    write_log("STATUS",sysOrder)
    
try:
    arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)
    write_log("STATUS","CONECTED")
    ardu_con = "ok"
except:
    write_log("STATUS","ERROR /dev/ttyUSB0")
    ardu_con = "no"

while True:
    print("Obteniendo temperatura")
    temp = str(CPUTemperature().temperature)
    print(temp)
    write_log("TEMP",temp)
    print("Arduino conectado ["+ardu_con+"]")
    sleep(3)

    if ardu_con == "ok":
        if CPUTemperature().temperature < 40:
            send_biosino("fanOff")
        else:
            if CPUTemperature().temperature > 45:
                send_biosino("fanOn")
    
        if CPUTemperature().temperature >= 60:
            sound_sys("temp","yes")
            sleep(60)
        else:
            sleep(120)
    else:
        print("esperando para la siguiente lectura")
        sleep(120)