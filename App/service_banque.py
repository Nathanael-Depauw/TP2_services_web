from fastapi import FastAPI
import json
from pydantic import BaseModel
import requests
import sys

app = FastAPI()

class Client(BaseModel):
	name: str

class Bank_validation(BaseModel):
	name: str
	validation: bool
	reason: str

@app.get("/bank_valid")
async def validate(client: Client):
	
	v = True
	text = ""
	f_h = open("data/historique_database.json", "r")
	data_h = json.load(f_h)
	f_a = open("data/actuel_database.json", "r")
	data_a = json.load(f_a)
	if (client.name in data_h) and (client.name in data_a):
		if data_h[client.name]['faillite'] > 0 :
			v = False
			text.append("- vous avez été en faillite")
		if data_h[client.name]['nbPaymentRetard'] > 0 :
			v = False
			text.append("- vous avez été eu des payements en retard")
		if data_h[client.name]['credit'] > (data_a[client.name]['revenus_mens'] - data_a[client.name]['depenses_mens']) :
			v = False
			text.append("- vous n'avez pas assez de revenus")
	else:
		v = False
		text = client.name + " n'est pas enregistré"
	
	return {"name": client.name, "validation": v, "reason" : text}
