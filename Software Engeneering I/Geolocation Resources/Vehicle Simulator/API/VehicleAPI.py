import requests
import http.server
from http.server import BaseHTTPRequestHandler
import googlemaps
import Vehicle

destlat = 0.00
destlong = 0.00
vin = 0
vtype = 0
vlat = 0
vlong = 0
mapsapikey = "AIzaSyAnOrHGcWH9ya9lShrAskTIonJvp-GAfLE"

def receiveandassign(disptachinfo):
    print("Working on it")

def requestroute(key,destlat,destlong,vlat,vlong):
    httprequeststring = "https://maps.googleapis.com/maps/api/directions/json?origin=" + vlat + "," + vlong \
                        + "&destination=" + destlat + "," + destlong + "&key=" + key
    routerequest = requests.get(httprequeststring).json()
    print("Working on it")

def deploy(mapsresponse):
    print("Working on it")

def updateDispatch(simRecord):
    print("Working on it")






