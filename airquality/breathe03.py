#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://swapi.co/api/people/1/"

# imports always go at the top of your code
import requests
import argparse, socket

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("----------------")
    print(r.json())
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-a',  help='ME') 


# display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
#    for x in r.json():
#      if x.get()
main()
