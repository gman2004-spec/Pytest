import pytest
import requests

@pytest.fixture
def consulta_cep():
    resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
    
    if resposta.status_code != 200:
        return 'Cep não encontrado'
    
    else:
        resposta.status_code = 200
        resposta.json()
        
        return resposta
global resposta

def test_cep_nao_encontrado(consulta_cep):
    resposta = consulta_cep
    
    assert not resposta == 'Cep não encontrado' 
    
def test_encontrar_numero_de_cep(consulta_cep):
    resposta = consulta_cep
    
    #cep = resposta.json()
    #assert cep["cep"] ==  "01001-000"
    assert resposta.json() == {
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "unidade": "",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "estado": "São Paulo",
  "regiao": "Sudeste",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}   
