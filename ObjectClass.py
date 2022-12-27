class Manager:
    id = ""
    name = ""
    username = ""
    password = ""
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

class Employee:
    id = ""
    name = ""
    status = ""
    dayoffs = 0

    def __init__(self, id, name, status, dayoffs):
        self.id = id
        self.name = name
        self.status = status
        self.dayoffs = dayoffs

