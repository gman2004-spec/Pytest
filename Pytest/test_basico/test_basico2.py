def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email Válido'
    else:
        return 'email incorreto'

def test_verifica_o_email():
    assert verifica_email('godzilla@gmail.com') == 'email Válido'
    assert verifica_email('godzilla@gmail') == 'email incorreto'
