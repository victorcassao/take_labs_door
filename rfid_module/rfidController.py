from mfrc522 import SimpleMFRC522

PATH_CARDS_DB = "rfid_module/cards.txt"

class RFIDController:
    
    def __init__(self):
        
        self.reader = SimpleMFRC522()
        
    
    def hasAccess(self, id):
        
        authorized_id = self.__getAuthorizedIds()
        
        if id in authorized_id:
            return True
        else:
            return False
        
    def __getAuthorizedIds(self):
        
        ids = []
        
        with open(PATH_CARDS_DB, 'r') as cards:
            
            for card_id in cards.read():
                
                ids.append(str(card_id))
                
        return ids
    
    def read(self):
        
        id, text = self.reader.read()
        
        return id, text
        