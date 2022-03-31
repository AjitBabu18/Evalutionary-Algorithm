# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 00:42:15 2021

@author: ajitb
"""

import random


MAX_GEN = 100
POP_SIZE = 50
DIMENSION = 25

def create_ind():
    return [random.randint(0,1) for _ in range(DIMENSION)]
def create_random_population():
    return[create_ind() for _ in range(POP_SIZE)]

def onemax(ind): #OneMax returnes number of 1s in vector.
     return sum(ind)

def select(pop, fits): # p_i = f_i/sum(fits)
    return random.choices(pop, fits, k=POP_SIZE)

def cross(p1, p2):
    point = random.randint(0, DIMENSION-1)
    o1 = p1[:point] + p2[point:]
    o2 = p2[:point] + p1[point:]
    return o1, o2

def mutate(ind):
    o=[]
    for bit in ind:
        if random.random() < 0.01:
            o.append(1-bit)
        else:
             o.append(bit) 
    return o
def mutation(pop):
    return[mutate(ind) for ind in pop]

def crossover(pop):
    offspring = []
    for p1, p2 in zip(pop[::4], pop[2::4]):
        o1, o2 = cross(p1, p2)
        offspring.append(o1)
        offspring.append(o2)
    return offspring

def mate(pop):
    pop1 = crossover(pop)
    return mutation(pop1)

def evolutionary_algorithm(fitness):
    pop = create_random_population()
    log = []
    for G in range(MAX_GEN):
        fits = list(map(fitness, pop)) #fitness function.
        log.append((max(fits), sum(fits)/POP_SIZE))
        mating_pool = select(pop, fits)
        offspring = mate(mating_pool)
        pop = offspring[:]

    return pop, log
import pprint
pop = create_random_population()
fits = list(map(onemax, pop))
pprint.pprint(list(zip(pop, fits)))
print('='*80)
result, log = evolutionary_algorithm(onemax)
res_fits = list(map(onemax, result))
#pprint.pprint(list(zip(result, res_fits)))



import matplotlib.pyplot as plt
avg = [l[1] for l in log]
best = [l[0] for l in log]
plt.plot(best, label = 'Best')
plt.plot(avg, label = 'Avg')
plt.legend()
plt.show()
