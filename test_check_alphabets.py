import alphabets

def test_check_english():
    assert alphabets.check_alphabets("hello world")["english"] == True
    assert alphabets.check_alphabets("hello world")["greek"] == False
    assert alphabets.check_alphabets("hello world")["cyrillic"] == False
    assert alphabets.check_alphabets("hello world")["punctuation"] == False

def test_check_greek():
    assert alphabets.check_alphabets("καλημέρα")["english"] == False
    assert alphabets.check_alphabets("καλημέρα")["greek"] == True
    assert alphabets.check_alphabets("καλημέρα")["cyrillic"] == False
    assert alphabets.check_alphabets("καλημέρα")["punctuation"] == False

def test_check_cyrillic():
    assert alphabets.check_alphabets("д")["english"] == False
    assert alphabets.check_alphabets("д")["greek"] == False
    assert alphabets.check_alphabets("д")["cyrillic"] == True
    assert alphabets.check_alphabets("д")["punctuation"] == False

def test_check_punctuation():
    assert alphabets.check_alphabets(".")["english"] == False
    assert alphabets.check_alphabets(".")["greek"] == False
    assert alphabets.check_alphabets(".")["cyrillic"] == False
    assert alphabets.check_alphabets(".")["punctuation"] == True

def test_check_multiple_alphabets():
    assert alphabets.check_alphabets("hello world.")["english"] == True
    assert alphabets.check_alphabets("hello world.")["greek"] == False
    assert alphabets.check_alphabets("hello world.")["cyrillic"] == False
    assert alphabets.check_alphabets("hello world.")["punctuation"] == True
    
    assert alphabets.check_alphabets("καλημέρα world.")["english"] == True
    assert alphabets.check_alphabets("καλημέρα world.")["greek"] == True
    assert alphabets.check_alphabets("καλημέρα world.")["cyrillic"] == False
    assert alphabets.check_alphabets("καλημέρα world.")["punctuation"] == True

def test_check_capitals():
    assert alphabets.check_alphabets("Hello World")["english"] == True
    assert alphabets.check_alphabets("Hello World")["greek"] == False
    assert alphabets.check_alphabets("Hello World")["cyrillic"] == False
    assert alphabets.check_alphabets("Hello World")["punctuation"] == False

def test_check_tonos():
    assert alphabets.check_alphabets("έ")["greek"] == True