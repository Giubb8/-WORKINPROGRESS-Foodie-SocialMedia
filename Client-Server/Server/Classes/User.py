import json


class User(object):
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.request = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_friends(self):
        return [friend.username for friend in self.friends]

    def __str__(self):
        return f"User: {self.username}, Friends: {self.friends}"        
            
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

