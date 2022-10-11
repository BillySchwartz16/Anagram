def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    maps = {}
    mapt = {}
    for i in s:
        maps[i] = maps.get(i, 0) + 1
    for i in t:
        mapt[i] = mapt.get(i, 0) + 1
    return maps == mapt

print(is_anagram("billy", "yibl"))