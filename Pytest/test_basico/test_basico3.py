def validar_senha(senha):
    caractere = '@#$%&*'
    if len(senha) > 8 and \
        any(c.isdigit() for c in senha) and \
        any(c.isupper() for c in senha) and \
        any(c in caractere for c in senha):
        return 'Senha cadastrada'
    else:
        return 'Senha não contem elementos obrigatórios'

def test_validar_senha():
    assert validar_senha('Helo@12345') == 'Senha cadastrada'
    assert validar_senha('12345') == 'Senha não contem elementos obrigatórios'    