import pytest

@pytest.fixture
def lista_simples():
    return [1,2,3,4]


def test_somar_lista(lista_simples):
    assert sum(lista_simples) == 10

def test_tamanho_lista(lista_simples):
    assert len(lista_simples) == 4
    
def test_tipo_estrutura(lista_simples):
    assert type(lista_simples) == list 
    
def test_numero_maximo(lista_simples):
    assert max(lista_simples) == 4 
    
def test_numero_minimo(lista_simples):
    assert min(lista_simples) == 1   