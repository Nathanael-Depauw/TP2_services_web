from fastapi import FastAPI
import json
from pydantic import BaseModel
import requests
import sys


url_bank_validation = 'http://127.0.0.1:8002/bank_valid'
url_visite = 'http://127.0.0.1:8001/visit'

app = FastAPI()

class Client(BaseModel):
	name: str

class House(BaseModel):
	adress: str

class Demand(BaseModel):
	name: str
	price: float
	adress: str
	description: str | None = None

class Visit(BaseModel):
	adress: str
	validation: bool
	reason: str

class bank_validation(BaseModel):
	name: str
	validation: bool
	reason: str

class bank_credit(BaseModel):
	name: str
	credit: float
	reason: str

def bank_validate(Client):
	body = {"name": Client.name}
	rep = requests.get(url_bank_validation, json=body)
	retj = rep.json()
	print(retj)
	ret = bank_validation(name = retj["name"], validation = retj["validation"], reason = retj["reason"])
	return ret;

def visit(House):
	body = {"adress": House.adress}
	rep = requests.get(url_visite, json=body)
	retj = rep.json()
	print(retj)
	ret = Visit(adress = retj["adress"], validation = retj["validation"], reason = retj["reason"])
	return ret;

@app.put("/credit_demand")
async def compute_demand(demand: Demand):
	print(demand.name + '''
''' + str(demand.price))
	client = Client(name = demand.name)
	house = House(adress = demand.adress)
	val = bank_validate(client)
	vis = visit(house)
	answer = open("Reponse.txt", 'w')
	a = '''Bonjour, ''' + demand.name + '''

Nous avons bien reçu votre demande de crédit immobilier pour l'achat de la propriété située au ''' + demand.adress + '''.'''
	if val.validation and vis.validation:
		a.append('''Nous avons accépté cetter demande''')
	else:
		a.append('''Nous n'avons pas pu accéder à votre demande car
''' + val.reason + 	'''
''' + vis.reason)
	a.append('''
Nous vous souhaitons une bonne continuation.''')
	answer.write(a)
	answer.close
	return 0

