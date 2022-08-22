import RPi.GPIO as GPIO
import time
import warnings

class GPIOController:
    
    def __init__(self):
        
        GPIO.setwarnings(False)
        warnings.filterwarnings('ignore')
        
        self.BUZZER = 15
        self.DOOR = 22
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUZZER, GPIO.OUT)
        GPIO.setup(self.DOOR, GPIO.OUT)
            
    def __unlock_door(self):
        
        GPIO.output(self.DOOR, GPIO.HIGH)
    
    def __lock_door(self):
        
        GPIO.output(self.DOOR, GPIO.LOW)
        
    def __set_buzzer_on(self):
        
        GPIO.setup(self.BUZZER, GPIO.HIGH)
        
    def __set_buzzer_off(self):
        
        GPIO.setup(self.BUZZER, GPIO.LOW)
    
    def open_door(self, 
                  time_to_buzzer_on=0.1, 
                  time_to_door_open=5):
        
        self.__unlock_door()
        self.__set_buzzer_on()
        time.sleep(time_to_buzzer_on)
        self.__set_buzzer_off()
        time.sleep(time_to_door_open)
        self.__lock_door()