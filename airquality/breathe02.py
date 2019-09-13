#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-01-21&distance=25&API_KEY=2D0657E7-BCD0-4936-B9A2-10C1BDC05859" 

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the JSON we were returned as Pythonic datastructures
    print(r.json())

main()
