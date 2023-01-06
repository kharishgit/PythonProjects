class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first_str = strs[0]
        last_strs = strs[-1]
        lcp=""
        for i,c in enumerate(first_str):
            print(i,c)
            if c == last_strs[i]:
                lcp+=c
            else:
                break
        return lcp

s=Solution()
res=s.longestCommonPrefix(["flower","flow","flight"])
print(res)