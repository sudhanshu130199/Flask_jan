from app import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/ping')
    assert resp.status_code == 200

def test_aboutus(client):
    resp = client.get('/aboutus')
    assert resp.status_code == 200

def test_predict(client):
    test_data={'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2000000}
    resp=client.post('/prediction', json=test_data)
    assert resp.status_code == 500
    assert resp.json=={'loan_approval_status': 'Rejected'}

