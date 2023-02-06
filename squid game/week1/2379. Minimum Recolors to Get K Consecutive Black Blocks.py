class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        i = 0
        j = 0
        ans = inf
        whites = 0
        while i < len(blocks):
            while j < len(blocks) and (j - i) < k:
                if blocks[j] == "W":
                    whites += 1
                j += 1
            
            ans = min(ans, whites)
            if j == len(blocks) and i == len(blocks) - k:
                break
            if blocks[i] == "W":
                whites -= 1
            i += 1
        return ans

