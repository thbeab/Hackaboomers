class Route(object):
    routeID = 0
    routeName = ''
    trips = []
    stops = []

    def __init__(self, routeID, routeName, trip, stop):
        self.routeID = routeID
        self.routeName = routeName
        self.trips.append(trip)
        self.stops.append(stop)

class Trip(object):
    tripID = 0
    tripName = ''
    stopSequence = []

    def __init__(self, tripID, tripName, stopSequence):
        self.tripID = tripID
        self.tripName = tripName
        self.stopSequence.append(stopSequence)

class Stop(object):
    stopID = 0
    stopName = ''

    def __init__(self, stopID, stopName):
        self.stopID = stopID
        self.stopName = stopName

