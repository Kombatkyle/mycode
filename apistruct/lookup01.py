#!/usr/bin/env python3
import requests

def main():
  mytoken = 'f243bb1486a4e247adff47ccbba5f1c62e82266a8c4b28a0'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?device=" + mytoken

  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi).json()

  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)

if __name__ == '__main__':
  main()
