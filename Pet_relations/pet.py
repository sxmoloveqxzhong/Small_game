class pet_core:
    def __init__(self):
        self.__id=0
        self.__ablity=[]
        self.__currentskills=[]
    def get_id(self):
        return self.__id
    def get_ablity(self):
        import copy
        return copy.deepcopy(self.__ablity)
    def get_currentskills(self):
        import copy
        return copy.deepcopy(self.__currentskills)
    def get_all_information(self):
        import copy
        return {'id':self.__id,'ablity':self.__ablity,'currentskills':self.__currentskills}
    
    def set_information(pets_core): #pets_core: 3d dictionary
        if not type(pets_core) is dict:
            return -1
        if not len(pets_core)==3:
            retrun -1
        self.__id=pets_core['id']
        self.__ablity=pets_core['ablity']
        self.__currentskills=pets_core['currentskills']
        
    
