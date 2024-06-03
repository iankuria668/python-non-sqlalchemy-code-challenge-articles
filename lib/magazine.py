class Magazine:
    def __init__(self,name,category):
        if not isinstance(name,str) or (2<=len(name) <= 0):
            raise ValueError('Name should be entered')
        self.name = name
        if not isinstance(category,str) or len(category) == 0:
            raise ValueError('Name should be entered')
        self.name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    