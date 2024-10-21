from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class  Calculator(BaseModel):
   price : float
   people : int
   tip : float

@app.post("/calculator")
def calculator_tip(request: Calculator):
   quantity_propina = request.price * (request.tip / 100)
   total_to_pay = request.price + quantity_propina
   
   payment_per_person = total_to_pay / request.people

   return{"precio_por_persona": round(payment_per_person, 2)}
