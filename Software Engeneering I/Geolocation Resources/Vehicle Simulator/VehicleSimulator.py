import requests
from Vehicle import Vehicle
import http.server
from http.server import BaseHTTPRequestHandler

scrawnynag = Vehicle(0, "type", 0.00, 0.00, "Available")

def startengine(vehiclesend):
   print("Working on it")

def travelroute(legpos,legtime):
    print("Working on it")

def updatevapi(vlat,vlong,vstate):
    print("Working on it")

def startenginedemo(vin,vlat,vlong,vtype,destlat,destlong):
    scrawnynag.vin = vin
    scrawnynag.vtype = vtype

    scrawnynag.changeposition(vlat,vlong)
    scrawnynag.changestate("Deployed")

    print(scrawnynag.vstate)
    print(scrawnynag.vlat)
    print(scrawnynag.vlong)

    travelroutedemo(destlat,destlong)

def travelroutedemo(destlat,destlong):
    scrawnynag.changeposition(destlat,destlong)
    scrawnynag.changestate("Available")
    updatevapi(scrawnynag.vlat,scrawnynag.vlong,scrawnynag.vstate)

def main():
    startenginedemo(101,45.667,77.445,"Pizza",100.08,86.44)
    print(scrawnynag.vstate)
    print(scrawnynag.vlat)
    print(scrawnynag.vlong)

main()