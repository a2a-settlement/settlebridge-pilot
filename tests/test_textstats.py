from pilot.textstats import average_word_length, word_count


def test_word_count_simple():
    assert word_count("hello world") == 2


def test_average_word_length_simple():
    assert average_word_length("ab abcd") == 3.0


def test_word_count_repeated_spaces():
    assert word_count("hello  world") == 2


def test_word_count_tabs_and_newlines():
    assert word_count("hello\tworld\nagain\n") == 3


def test_word_count_empty_and_whitespace_only():
    assert word_count("") == 0
    assert word_count("   \t\n") == 0


def test_average_word_length_empty():
    assert average_word_length("") == 0.0


def test_average_word_length_whitespace_only():
    assert average_word_length("   \t\n") == 0.0
