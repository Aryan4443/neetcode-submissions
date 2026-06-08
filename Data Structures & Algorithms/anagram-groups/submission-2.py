class Solution:
    def groupAnagrams(self, strs):
        hashmap =defaultdict(list) # python lib creates list inside dictionary

        for word in strs:
            count = [0] * 26 # because constraint says only small letters
            for char in word:
                count[ord(char)- ord('a')] += 1 #gives index ACSII
            hashmap[tuple(count)].append(word)
        return list(hashmap.values())