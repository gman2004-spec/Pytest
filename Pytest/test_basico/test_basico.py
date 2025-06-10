def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else: 
        return 'é impar'
    
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b        
  
def test_verica_se_numero_par():
    assert eh_par(7) == 'é impar'
    assert eh_par(10) ==  'é par' 
    
def verifica_soma_e_subtrair():
    assert somar(5,6) == 11
    assert subtrair(10,8) == 2      