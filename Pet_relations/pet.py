class pet_core:
    def __init__(self):
        self.__id=0
        self.__ability=[]
        self.__currentskills=[]
    def get_id(self):
        return self.__id
    def get_ability(self):
        import copy
        return copy.deepcopy(self.__ability)
    def get_currentskills(self):
        import copy
        return copy.deepcopy(self.__currentskills)
    def get_all_information(self):
        import copy
        return {'id':self.__id,'ability':self.__ability,'currentskills':self.__currentskills}
    
    def set_information(self,pets_infromation): #pets_information: 3d dictionary
        if not type(pets_infromation) is dict:
            return -1
        if not len(pets_infromation)==3:
            retrun -1
        self.__id=pets_infromation['id']
        self.__ability=pets_infromation['ability']
        self.__currentskills=pets_infromation['currentskills']
        
class ability_core:
    def __init__(self):
        self.__attack=0
        self.__defence=0
        self.__magicattack=0
        self.__magicdefence=0
        self.__speed=0
        self.__hp=0
    def get_attack(self):
        return self.__attack
    def get_defence(self):
        return self.__defence
    def get_magicattack(self):
        return self.__magicattack
    def get_magicdefence(self):
        return self.__magicdefence
    def get_speed(self):
        return self.__speed
    def get_hp(self):
        return self.__hp
    def get_ability(self):
        return {'attack':self.__attack,'defence':self.__defence,'magicattack':self.__magicattack,
        'magicdefence':self.__magicdefence,'speed':self.__speed,'hp':self.__hp}
    
    def set_ability(self,pets_ability): #pets_ability: 6d dictionary
        if not type(pets_ability) is dict:
            return -1
        if not len(pets_ability)==6:
            retrun -1
        self.__attack=pets_ability['attack']
        self.__defence=pets_ability['defence']
        self.__magicattack=pets_ability['magicattack']
        self.__magicdefence=pets_ability['magicdefence']
        self.__speed=pets_ability['speed']
        self.__hp=pets_ability['hp']
