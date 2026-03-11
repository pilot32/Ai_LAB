import random
import math
POP_SIZE = 30
GENERATIONS = 50
CHROM_LEN = 10
Pc = 0.8
Pm = 0.02
TOUR_SIZE = 3
def decode(chrom):
    decimal=int(chrom,2)
    return 10*decimal/(2**CHROM_LEN-1)
def fitness(x):
    return math.sin(x)+x
def init_population():
    return [''.join(random.choice('01') for i in range(CHROM_LEN)) for _ in range(POP_SIZE)]
def tournament(pop):
    selected=random.sample(pop,TOUR_SIZE)
    selected.sort(key=lambda c:fitness(decode(c)),reverse=True)
    return selected[0]
def crossover(p1,p2):
    if random.random() < Pc:
        point=random.randint(1,CHROM_LEN-1)
        c1=p1[:point]+p2[point:]
        c2=p2[:point]+p1[point:]
        return c1,c2
    return p1,p2
def mutate(chrom):
    new_chrom=''
    for bit in chrom:
        if random.random()<Pm:
            new_chrom+='1' if bit=='0' else '0'
        else:
            new_chrom+=bit
        return new_chrom
population=init_population()
for _ in range(GENERATIONS):
    new_pop=[]
    while len(new_pop)<POP_SIZE:
        p1=tournament(population)
        p2=tournament(population)
        c1,c2=crossover(p1,p2)
        new_pop.append(mutate(c1))
        new_pop.append(mutate(c2))
    population=new_pop[:POP_SIZE]
best=max(population,key=lambda c:fitness(decode(c)))
best_x=decode(best)
best_f=fitness(best_x)
print("Best x: ",best_x)
print("Maximum f(x): ",best_f)