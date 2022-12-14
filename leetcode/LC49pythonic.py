from collections import defaultdict


def groupAnagrams(strs):
    res=defaultdict(list)
    for s in strs:
        res[tuple(sorted(s))].append(s)
    return list(res.values())

a= groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)