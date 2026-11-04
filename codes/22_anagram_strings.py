def is_anagram(first, second):
    s1 = first.replace(" ", "").lower()
    s2 = second.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)