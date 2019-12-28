class Entity():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def callClassName():
        print('Entity')
    def getName(self):
        return self.name
Entity.callClassName()
 
class People(Entity):
    def __init__(self, is_alive, age, name):
        self.is_alive = is_alive
        self.age = age
        self.name = name
    def getName(self):
        return self.is_alive
 
if __name__ == "__main__":
    entity = Entity("John", 25)
    Entity.callClassName()
    print(entity.getName())
    p = People(True, 25, "Martin")
    p.callClassName()
    print(p.getName())
