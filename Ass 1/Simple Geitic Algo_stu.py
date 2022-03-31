# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:39:16 2021

@author: ajitb
"""

MAX_GEN = 1000
IND_LEN = 20
POP_SIZE = 20
MUT_FLIP_PROB = 0.01

import random

def fitness(ind):
    return sum(ind)

def create_random_individual():
    return [random.randint(0,1) for _ in range(IND_LEN)]

def create_random_population():
    return [create_random_individual() for _ in range(POP_SIZE)]

def select(pop, fits):
    return random.choices(pop, fits, k=POP_SIZE)

def cross(p1, p2):
    point = random.randint(0, len(p1)-1)
    o1 = p1[:point] + p2[point:]
    o2 = p2[:point] + p1[point:]
    return o1, o2

def crossover(pop):
    offspring = []
    for p1, p2 in zip(pop[::2], pop[1::2]):
        o1, o2 = cross(p1, p2)
        offspring += [o1, o2]
    return offspring

def mutate(p):
    o = []
    for gene in p:
        if random.random() < MUT_FLIP_PROB:
            o.append(1-gene)
        else:
            o.append(gene)
    return o

def mutation(pop):
    return [mutate(ind) for ind in pop]

def mate(pop):
    o1 = crossover(pop)
    return mutation(o1)

def evolutionary_algorithm(fitness):
    pop = create_random_population()
    log = []
    for G in range(MAX_GEN):
        fits = [fitness(i) for i in pop]
        log.append((max(fits), sum(fits)/POP_SIZE))
        mating_pool = select(pop, fits)
        offspring = mate(mating_pool)
        pop = offspring[:] # + [max(pop, key=fitness)]
    return pop, log


if __name__ == '__main__':

    import pprint
    pop, log = evolutionary_algorithm(fitness)
    fits = [fitness(p) for p in pop]
    pprint.pprint(list(zip(pop, fits)))

    import matplotlib.pyplot as plt

    plt.plot([l[0] for l in log])
    plt.plot([l[1] for l in log])
    plt.show()