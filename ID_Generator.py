# CLASS RETURNS UNIQUE RANDOM INT ID FROM 1 to X
# built in module random;
import random

class UserIDGenerator:
    def __init__(self):
        self.used_ids = set()
    
    def generate_user_id(self, max):
        while True:
            user_id = random.randint(1, max)
            # check if a new id
            if user_id not in self.used_ids:
                self.used_ids.add(user_id)
                return user_id