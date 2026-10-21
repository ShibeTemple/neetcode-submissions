class Solution:

    def encode(self, strs: List[str]) -> str:
        master_string = str(len(strs)) + "---"

        for string in strs:
            master_string += string + "|...|wow!|...|"

        print(master_string)
        return master_string

    def decode(self, s: str) -> List[str]:
        data = s.split("---")
        count = int(data[0])
        if count == 0:
            return []
        split = data[1].removesuffix("|...|wow!|...|").split("|...|wow!|...|")
        return split
