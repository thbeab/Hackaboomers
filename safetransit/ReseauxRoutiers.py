class Route(object):
    routeID = 0
    routeName = ''
    trips = []
    stops = []

    def __init__(self, routeID, routeName, trips, stops):
        self.routeID = routeID
        self.routeName = routeName
        self.trips = trips
        self.stops = stops
    def addTrip(self, trip):
        self.trips.append(trip)
    def addStop(self, stop):
        self.stops.append(stop)

class Trip(object):
    tripID = 0
    stopSequence = []



    def __init__(self, tripID):
        self.tripID = tripID

        #self.stopSequence.append(stopSequence)
    def addStopSequence(self, stopSequence):
        self.stopSequence.append(stopSequence)

class Stop(object):
    stopID = 0
    stopName = ''

    def __init__(self, stopID, stopName):
        self.stopID = stopID
        self.stopName = stopName

print(7)