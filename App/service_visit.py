from fastapi import FastAPI
import json
from pydantic import BaseModel
import requests
import sys

app = FastAPI()

class Visit(BaseModel):
	adress: str
	validation: bool
	reason: str

class House(BaseModel):
	adress: str

@app.get("/visit")
async def visit_house(house: House):
		v = True
		text = ""
		f = open( ("visit/data.json") , "r")
		data = json.load(f)
		if (house.adress in data):
			v = data[house.adresse]["valide"]
			text.append(data[house.adresse]["comment"])
		else:
			v = False
			text = "La propriété à cette adresse n'a pas été visitée"
	return {"adress" : house.adress, "validation": v, "reason" : text}
