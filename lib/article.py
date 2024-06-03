class Article:
    def __init__(self,title):
        if not isinstance(title,str) or not(5<=len<=50):
            raise ValueError('Name should be entered')
        self.title = title
    
    