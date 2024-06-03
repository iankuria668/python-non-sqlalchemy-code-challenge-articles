class Author:
    def __init__(self,name):
        if not isinstance(name,str) or len(name) == 0:
            raise ValueError('Name should be entered')
        self._name = name
    
    @property
    def name(self):
        return self._name
    
author1 = Author()