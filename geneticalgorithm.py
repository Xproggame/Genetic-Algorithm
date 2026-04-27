class GeneticAlgorithm:

    def __init__(self):
        self.survivors = {} # {~rank : [species, energy, chromosomes,]}

    def ranking(self, population:dict, nmb_survivors:int): # population{~species : [energy, chromosomes]}
        self.survivors = dict(sorted(population.items(), key=lambda item:item[1][0], reverse=True))