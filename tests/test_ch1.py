import sys


def vowel_count(string):
    count = 0
    string = string.lower()
    for c in string:
        if c == 'a' or c == 'i' or c == 'e' or c == 'o' or c == 'u':
            count += 1
    return count


def short_long(string):
    short = sys.maxsize
    short_str = ""
    long = -sys.maxsize
    long_str = ""
    for str in string.split():
        if len(str) < short:
            short = len(str)
            short_str = str
        if len(str) > long:
            long = len(str)
            long_str = str

    ans = short_str + " " + long_str
    return short_str, long_str


def test_short_long_1():
    assert short_long("A cow jUmped Over the Moon") == ('A', 'jUmped')


def test_short_long_2():
    assert short_long(" cow jUmped Over the Moon") == ('cow', 'jUmped')


def test_short_long_3():
    assert short_long("cow are thr you") == ('cow', 'cow')


def test_vowel_count_1():
    assert vowel_count('aaaaaaa') == 7


def test_vowel_count_2():
    assert vowel_count('bbbbba') == 1


def test_vowel_count_3():
    assert vowel_count('iaoue') == 5


def test_vowel_count_4():
    assert vowel_count('AIOUE') == 5


def test_vowel_count_5():
    assert vowel_count('') == 0
