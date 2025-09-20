import pytest

def test_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

def test_validate_luas_segitiga():
    alas = 10
    tinggi = 5
    luas = test_luas_segitiga(alas, tinggi)
    assert luas == 25
    


