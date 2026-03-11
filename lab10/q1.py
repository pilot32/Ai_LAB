import itertools
dist={
    ('A','B'):3, ('B','A'):3,
    ('A','C'):2, ('C','A'):2,
    ('B','C'):1, ('C','B'):1
}
cities=['A','B','C']
def tourcost(tour):
    cost=0
    for i in range(len(cities)-1):
        cost+=dist[(tour[i],tour[i+1])]
    return cost
current=['A','B','C']
current_cost=tourcost(current)
neigbours=list(itertools.permutations(cities))
neigbours=[list(n) for n in neigbours if n[0]=='A']
for n in neigbours:
    cost=tourcost(n)
    if cost<current_cost:
        current=n
        current_cost=cost
print(f"{current[0]} [{dist[(current[0],current[1])]} km]-->"
      f"{current[1]} [{dist[(current[1],current[2])]} km]--> "
      f"{current[2]} [{current_cost} km] (most efficient)")