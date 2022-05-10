#JSON returns dictionary

class Provider: 
    def __init__(self, dict):
        self.id = dict["id"]
        self.first_name = dict["first_name"]
        self.last_name = dict["last_name"]
        self.sex = dict["sex"]
        self.birth_date = dict["birth_date"]
        self.rating = dict["rating"]
        self.primary_skills = dict["primary_skills"]
        self.secondary_skill = dict["secondary_skill"]
        self.company = dict["company"]
        self.active = dict["active"]
        self.country = dict["country"]
        self.language = dict["language"]