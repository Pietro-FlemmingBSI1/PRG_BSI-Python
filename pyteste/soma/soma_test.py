"""Testando a Função"""
from soma import soma

def test_soma_lista_vazia():
    assert soma([]) == 0

def test_soma_unitaria():
    assert soma([0]) == 0
    assert soma([3]) == 3

def test_soma_varios_elementos():
    assert soma([1,2,3]) == 6
    assert soma([79,723,2]) == 804
