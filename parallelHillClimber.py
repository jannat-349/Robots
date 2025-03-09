from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Spawn(self):
        self.children = {}
        for i in range(c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(c.populationSize):
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
            
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        for i in range(c.populationSize):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
    
    def Print(self):
        for parent in self.parents:
            print("parent fitness: ", self.parents[parent].fitness)
        for child in self.children:
            print("child fitness: ", self.children[child].fitness)


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print()
        self.Print()
        print()
        self.Select()

    def Show_Best(self):
        lowest_fitness_parent = min(self.parents, key=lambda parent: self.parents[parent].fitness)
        self.parents[lowest_fitness_parent].Start_Simulation("GUI")
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for _ in range (c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
