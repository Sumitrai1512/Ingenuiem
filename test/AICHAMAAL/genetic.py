import random
import math
# So we use the Cities as Points on a graph and the distance between them shall be calculated using their Euclidean Distances
cities = {'A': (0, 0), 'B': (5, 2), 'C': (6, 3), 'D': (3, 4), 'E': (2, 5)}

#The total Number Iterations the algo will run for & in each Iteration how many routes can be stored
num_of_iterations=100
pop_size = 50

def calculate_distance(city1,city2):
    x1,y1=city1
    x2,y2=city2
    distance = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) )
    return distance

def calculate_route_distance(route):
    total_distance=0
    for i in range(len(route)-1):
        total_distance+=calculate_distance(cities[route[i]],cities[route[i+1]])
    return total_distance

population = [random.sample(list(cities.keys()),len(cities)) for _ in range(pop_size)]
# In here the random.sample(list(cities.keys()),len(cities)) will first 
# Create a list of the cities-> keys
# Then that method will use this list and a limiter -> len(cities) to generate a sub list of that list containing the max number of elements = lens(cities)
count=0
for _ in range(num_of_iterations):
    parent1,parent2=random.sample(population,2)
    # print(parent1)
    # print(parent2)

    start,end=sorted(random.sample(range(len(cities)),2))
    # print(start,end)
    #so this line basically first gets the subset of cities (child) from parent 1 and then appends the cities from parent 2 which haven't been yet appended in child
    child = parent1[start:end]+[city for city in parent2 if city not in parent1[start:end]]
    

    #MUTATION STEP
    if random.random()<0.05:
        count+=1
        print("Mutation Happened , ",count)
        position1,position2=random.sample(range(len(cities)),2)
        child[position1],child[position2]=child[position2],child[position1]

    worst_route=max(population,key=calculate_route_distance)
    population.remove(worst_route)
    # print("Removed Route: ",worst_route)
    # print("Distance: ",calculate_route_distance(worst_route))
    # Check for the route with the highest route calculate_distance
    # print("Child Appended: ",child)
    population.append(child)


best_route=min(population,key=calculate_route_distance)

print("Best Route: ", best_route)
print("Distance Required: ",calculate_route_distance(best_route))



