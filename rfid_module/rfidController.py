from mfrc522 import SimpleMFRC522

PATH_CARDS_DB = "/home/pi/take_labs_door/rfid_module/cards.txt"

class RFIDController:
    
    def __init__(self):
        
        self.reader = SimpleMFRC522()
        
    
    def hasAccess(self, id):
        
        authorized_id = self.__getAuthorizedIds(id)
        
        if authorized_id:
            return True
        else:
            return False
        
    def __getAuthorizedIds(self, id):
        
        # ids = []
        
        with open(PATH_CARDS_DB, 'r') as cards:
            
            for card_id in cards:
                if str(id) in card_id:
                    return True
                        
        return False
    
    def read(self):
        
        id = self.reader.read_id()
        
        return id
        