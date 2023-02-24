from funciones import encontrar_menor

def test_encontrar_menor():
    assert encontrar_menor([1, 2, 3, 4, 5, 6]) == 1
    assert encontrar_menor([0, 4, 10, 4, 5, 6]) == 0
    assert encontrar_menor([7, 9, 3, 4, 5, 6]) == 3
    assert encontrar_menor([10, 2.4, 3, 40, 6]) == 2.4
    
    


