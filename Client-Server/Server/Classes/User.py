import json


class User(object):
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.request = []
        self.card_UID = ""

    def add_friend(self, friend):
        self.friends.append(friend)
    
    def add_request(self, friend):
        self.request.append(friend)
        
    def remove_friend(self,friend):
        self.friends.remove(friend)
        
    def remove_request(self,friend):
        self.request.remove(friend)
        
    def get_friends(self):
        return [friend.username for friend in self.friends]

    def __str__(self):
        return f"User: {self.username}, Friends: {self.friends}"        
            
    def get_username(self):
        return self.username
    
    def get_requests(self):
        return self.request
    
    def set_UID(self,new_UID: str):
        self.card_UID=str
    
    def get_UID(self):
        return self.card_UID
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

