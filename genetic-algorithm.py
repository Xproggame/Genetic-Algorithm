class GeneticAlgorithm:

    def __init__(self):
        self.survivors = {} # {~rank : [species, energy, chromosomes, family]}

    def ranking(self, population:dict, nmb_survivors:int): # population{~species : [energy, chromosomes, family]}

        for species in population.keys():
            indexed = False

            for rank in self.survivors.keys():

                if not indexed:

                    if population.get(species)[0] > self.survivors.get(rank)[1]:

                        retrograde = self.survivors.get(rank)
                        self.survivors[rank + 1] = s

                        self.survivors[rank] = [
                            species,
                            population.get(species)[0],
                            population.get(species)[1],
                            population.get(species)[2]
                        ]