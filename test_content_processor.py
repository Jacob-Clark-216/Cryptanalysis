import content_processor as cp

def test_seperators():
    msg = "hello world\nhow are you world"
    assert cp.get_lines(msg) == ["hello world", "how are you world"]
    assert cp.get_words(msg) == ["hello", "world", "how", "are", "you", "world"]
    assert cp.get_characters(msg) == ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d", " ", "h", "o", "w", " ", "a", "r", "e", " ", "y", "o", "u", " ", "w", "o", "r", "l", "d"]

def test_unique_method():
    msg = "hello world\nhow are you world"
    assert len(cp.unique(cp.get_lines(msg))) == 2
    for i in cp.unique(cp.get_lines(msg)):
        assert cp.unique(cp.get_lines(msg)).count(i) == 1
    assert len(cp.unique(cp.get_words(msg))) == 5
    for i in cp.unique(cp.get_words(msg)):
        assert cp.unique(cp.get_words(msg)).count(i) == 1
    assert len(cp.unique(cp.get_characters(msg))) == 11
    for i in cp.unique(cp.get_characters(msg)):
        assert cp.unique(cp.get_characters(msg)).count(i) == 1

def test_count_method():
    msg = "hello world\nhow are you world"
    assert cp.count(cp.get_lines(msg)) == {"how are you world": 1, "hello world": 1}
    assert cp.count(cp.get_words(msg)) == {"hello": 1, "world": 2, "how": 1, "are": 1, "you": 1}
    assert cp.count(cp.get_characters(msg)) == {"h": 2, "e": 2, "l": 4, "o": 5, " ": 5, "w": 3, "r": 3, "d": 2, "a": 1, "y": 1, "u": 1}