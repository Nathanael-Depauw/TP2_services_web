import json
import requests
import sys
from fastapi import FastAPI
url = 'http://127.0.0.1:8000/credit_demand'

arg = sys.argv[1]
demand = open(arg, 'r')

body = { "name": demand.readline().rstrip('''
''') , "price": float(demand.readline().rstrip('''
''')) , "adress": demand.readline().rstrip('''
''') , "description": demand.readline().rstrip('''
''') }

demand.close()

print(body)

ret = requests.put(url, json=body)
rep = ret.json()
