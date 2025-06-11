import pytest
import requests

@pytest.fixture
def consulta_cep():
    resposta = requests.get("https://viacep.com.br/ws/{cep}/json/")
    
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
    