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

def send_biosino(sysOrder):
    arduino.write(str(sysOrder).encode())
    #sound_sys("send", "no")
    #print(sysOrder)
    with open(csv, "a") as log:
        temp = str(CPUTemperature().temperature)
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str("SEND "+sysOrder)))

try:
    arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)
    with open(csv, "a") as log:
        temp = str(CPUTemperature().temperature)
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str("CONECTADO CORRECTAMENTE")))
except:
    #print("ALERTA ALGO PASA CON LA VENTILACION")
    #sound_sys("bioAlert", "no")
    with open(csv, "a") as log:
        temp = str(CPUTemperature().temperature)
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str("Error 404 /dev/ttyUSB0")))

while True:
    with open(csv, "a") as log:
        temp = str(CPUTemperature().temperature)
        #print(temp)
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
    sleep(3)
    if CPUTemperature().temperature < 40:
        send_biosino("fanOff")
    
    if CPUTemperature().temperature > 45:
        send_biosino("fanOn")
    
    if CPUTemperature().temperature >= 60:
        sound_sys("temp","yes")
        sleep(60)
        sound_sys("temp", "yes")
    else:
        #print("cya in 120s")
        sleep(120)


