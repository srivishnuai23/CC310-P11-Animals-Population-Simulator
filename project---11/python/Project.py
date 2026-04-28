import sys
import heapq

# Build Graph for Sim phase 1
def build_graph(filename):
    graph = {}
    with open(filename) as f:
        n = int(f.readline())
        organisms = [f.readline().strip() for _ in range(n)]
        
        for org in organisms:
            graph[org] = []
        
        e = int(f.readline())
        for _ in range(e):
            src, dest, weight = f.readline().split()
            graph[src].append((dest, float(weight)))
    
    return graph


# Build Tree for Sim Phase 2
def build_tree(filename):
    parent = {}
    children = {}
    
    with open(filename) as f:
        n = int(f.readline())
        
        for _ in range(n - 1):
            child, par = f.readline().split()
            parent[child] = par
            
            if par not in children:
                children[par] = []
            children[par].append(child)
    
    # find root
    root = None
    for node in children:
        if node not in parent:
            root = node
    
    return parent, children, root


# Build Queue for Sim Phase 3
def build_queue(filename):
    pq = []
    
    with open(filename) as f:
        n = int(f.readline())
        
        for _ in range(n):
            org, freq = f.readline().split()
            freq = int(freq)
            heapq.heappush(pq, (freq, org, freq))  # (next_day, org, frequency)
    
    return pq


# Define starting and final conditions
def build_population(filename):
    population = {}
    target = {}
    
    with open(filename) as f:
        n = int(f.readline())
        
        for _ in range(n):
            org, curr, targ = f.readline().split()
            population[org] = float(curr)
            target[org] = float(targ)
    
    return population, target


# Simulation Phase 1 - Update 
def update(population, graph):
    new_pop = {org: 0.0 for org in population}
    
    for src in graph:
        for dest, weight in graph[src]:
            new_pop[dest] += population[src] * weight
    
    return new_pop

# Simulation Phase 2 - Limit
def limit(population, parent, children, root):
    original = population.copy()
    
    def dfs(node):
        if node not in children:
            return
        
        parent_val = original[node]
        change = 0
        
        for child in children[node]:
            child_val = original[child]
            
            if child_val > 2 * parent_val:
                population[child] -= 20
                change += 20
            elif child_val < 0.5 * parent_val:
                population[child] += 20
                change -= 20
        
        population[node] += change
        
        for child in children[node]:
            dfs(child)
    
    dfs(root)

# Simulation phase 3 - Converse
def conserve(population, target, pq, day):
    while pq and pq[0][0] == day:
        _, org, freq = heapq.heappop(pq)
        
        if population[org] > 2 * target[org]:
            population[org] = population[org] / 2
        elif population[org] < 0.5 * target[org]:
            population[org] = population[org] * 3
        
        heapq.heappush(pq, (day + freq, org, freq))


# Main Function
def main(args):
    graph = build_graph(args[1])
    parent, children, root = build_tree(args[2])
    pq = build_queue(args[3])
    population, target = build_population(args[4])
    
    for day in range(3651):
        population = update(population, graph)
        limit(population, parent, children, root)
        conserve(population, target, pq, day)
    
    for org in population:
        print(f"{org} {population[org]:.4f}")


if __name__ == "__main__":
    main(sys.argv)