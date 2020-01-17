class Vehicle:

    def testattributes(self, vin, vtype, vlat, vlong, vstate):
        print("Working on it")

    def __init__(self, vin, vtype, vlat, vlong, vstate):

        self.vin = vin
        self.vtype = vtype
        self.vlat = vlat
        self.vlong = vlong
        self.vstate = vstate


    def changeposition(self, lat, long):
        self.vlat = lat
        self.vlong = long

    def changestate(self, state):
        self.vstate = state

