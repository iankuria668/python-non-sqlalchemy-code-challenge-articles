class Article:
    def __init__(self,title):
        if not isinstance(title,str) or not(5<=len<=50):
            raise ValueError('Name should be entered')
        self.title = title

        @property
        def author (self):
            return self._author
        
        @property
        def magazine(self):
            return  self._magazine
    
    