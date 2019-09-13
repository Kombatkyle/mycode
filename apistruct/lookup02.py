#!/usr/bin/env python3
import requests
import argparse

def main():
  mytoken = 'f243bb1486a4e247adff47ccbba5f1c62e82266a8c4b28a0'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken

  ## ask user for a brand to search on
#  brand = input("What brand of device are you searching for?")
#  brand = "&brand=" + brand

  ## translate our JSON response to a series of Python lists and dictionaries

  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--brand', help='Brand to search for') 
    args = parser.parse_args()
    myjson = requests.get(mybuiltapi + args.b).json()
    main()
