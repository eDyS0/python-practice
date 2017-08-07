class Allergies(object):
    scores = {
        'eggs' : 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }
    
    def __init__(self, score):
        self.score = score
        self.lst = list(allergy for allergy in self.scores if self.is_allergic_to(allergy))
        
    def is_allergic_to(self, allergy):
        return self.scores[allergy] & self.score
    
    