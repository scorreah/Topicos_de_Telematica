import os,json 
class fortDB: 
    def __init__(self , location=".\\db"): 
        self.location = os.path.expanduser(location) 
        self.loaddb() 
    def loaddb(self): 
        self.db = json.load(open(self.location, "r")) if os.path.exists(self.location) else {} 
        self.savedb()
        return True 
    def savedb(self): 
        try: 
            json.dump(self.db , open(self.location, "w+")) 
            return True 
        except: 
            return False 
    def put(self, key, value): 
        try: 
            self.db[str(key)] = value 
            self.savedb() 
            return True 
        except Exception as e: 
            print("[X] Error Saving Values to Database : " + str(e)) 
            return False 
    def get(self , key): 
        try: 
            return self.db[key] 
        except KeyError: 
            print("No Value Can Be Found for " + str(key))  
            return False 
    def delete(self , key): 
        if not key in self.db: 
            return False 
        del self.db[key] 
        self.savedb() 
        return True 
    def resetdb(self): 
        self.db={} 
        self.savedb() 
        return True
    def ping(self):
        return "PONG"

# db1 = fortDB('caco')
#db1.put('Sa','ZA')
# db1.put('Santiago', 'Paola')
# print(db1.get('Santiago'))