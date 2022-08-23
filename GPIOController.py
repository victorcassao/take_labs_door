import RPi.GPIO as GPIO
import time
import warnings

GPIO.setwarnings(False)
warnings.filterwarnings('ignore')

BUZZER = 5
DOOR = 22

time_to_buzzer_on = 0.2
time_to_door_open = 5

def openDoor():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.setup(DOOR, GPIO.OUT)

    GPIO.output(DOOR, GPIO.HIGH)
    GPIO.setup(BUZZER, GPIO.HIGH)
    time.sleep(time_to_buzzer_on)
    GPIO.setup(BUZZER, GPIO.LOW)
    time.sleep(time_to_door_open)
    GPIO.output(DOOR, GPIO.LOW)


# class GPIOController:
    
#     def __init__(self):
        
        
        
#         self.BUZZER = 15
#         self.DOOR = 22
        
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.BUZZER, GPIO.OUT)
#         GPIO.setup(self.DOOR, GPIO.OUT)
            
#     def __unlock_door(self):
        
#         GPIO.output(self.DOOR, GPIO.HIGH)
    
#     def __lock_door(self):
        
#         GPIO.output(self.DOOR, GPIO.LOW)
        
#     def __set_buzzer_on(self):
        
#         GPIO.setup(self.BUZZER, GPIO.HIGH)
        
#     def __set_buzzer_off(self):
        
#         GPIO.setup(self.BUZZER, GPIO.LOW)
    
#     def open_door(self, 
#                   time_to_buzzer_on=0.1, 
#                   time_to_door_open=5):
        
#         self.__unlock_door()
#         self.__set_buzzer_on()
#         time.sleep(time_to_buzzer_on)
#         self.__set_buzzer_off()
#         time.sleep(time_to_door_open)
#         self.__lock_door()