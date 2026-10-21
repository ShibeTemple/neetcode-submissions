from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strings: strs
        # group all anagrams together.
        # returned output can be in any order
        """sorted_strs = []
        output = defaultdict(list)

        explored = set()

        sorted_strs = ["".join(sorted(value)) for value in strs]

        num_strs = len(sorted_strs)
        for i in range(0,num_strs):
            if i in explored:
                continue
            current = sorted_strs[i]
            lonely = True
            for j in range(0,num_strs):
                considering = sorted_strs[j]
                if i != j and j not in explored:
                    if considering == current:
                        lonely = False
                        explored.add(j)
                        output[strs[i]].append(strs[j])
            if lonely:
                explored.add(i)
                output[strs[i]]

        return [[key] + value for key,value in output.items()]"""

        dict = defaultdict(list)
        for word in strs:
            dict["".join(sorted(word))].append(word)
        return list(dict.values())
            