from graph import *
from ReseauxRoutiers import *
import copy

graph = Graph(["A","B","C"],[["B","C",12,["165","166","369"]],["A","B",12,["165","166","369"]]])
print(graph.calculate_penalty(["165"],["165"," 166"]))
print(graph.calculate_penalty(["165"],["166"]))
# graph.add_vertex("A")
# graph.add_vertex("B")
print(graph.vertices)
print(graph.adjacency_matrix)
print(graph.transitlines_matrix)
'''
stop1 = Stop(1, 'test')
trip1 = Trip(1, 'test', 1)
trip1.addStopSequence(2)
print(trip1)'''

#creation d'un vecteur de stops
stop2 = []
file0 = open("data/stops.txt", "r")
for x0 in file0:
   #stops = x.read()
    vectorStops = x0.split(",")
    stop2.append(Stop(vectorStops[0], vectorStops[2]))
    #test Stop
print(stop2[479].stopName)
#creation d'un vecteur de trips
trip2 = []
file1 = open("data/stop_times.txt", "r")
compteur = 0
for x1 in file1:
    vectorTrips1 = x1.split(",")
    trip2.append(Trip(vectorTrips1[0]))
    trip2[compteur].addStopSequence(vectorTrips1[4])
    compteur += 1
    #test Trip
print(trip2[30].tripID)

#Creation route
route = []
file3 = open("data/routes.txt", "r")
for x3 in file3:
   #stops = x.read()
    vectorRoute = x3.split(",")
    route.append(Route(vectorRoute[0], vectorRoute[3], trip2, stop2))
#Test Route
print(route[1].routeID)
