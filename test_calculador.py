import pytest
from fastapi.testclient import TestClient
from calculator import app 

""" Se crea  un cliente de prueba para la API FastAPI"""
client = TestClient(app)

def test_calculator_tip_valid():
    """Test con valores válidos."""
    response = client.post("/calculator", json={"price": 999.99, "people": 4, "tip": 20.40})
    
    """Se verifica que el código de estado de la respuesta sea 200"""
    assert response.status_code == 200
    
    """ Se verifica que la respuesta JSON sea la esperada"""
    assert response.json() == {"precio_por_persona": 301.0} 


