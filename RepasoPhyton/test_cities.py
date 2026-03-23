from city_functions import city_country

def test_city_country():
    resultado = city_country('santiago', 'chile')
    assert resultado == 'Santiago, Chile'