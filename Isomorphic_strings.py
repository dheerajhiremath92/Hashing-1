class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict={}
        t_dict={}
        for i in range(0,len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]]=t[i]
            else:
                if(s_dict[s[i]]!=t[i]):
                    return False
            if(t[i] not in t_dict):
                t_dict[t[i]]=s[i]
            else:
                if(t_dict[t[i]]!=s[i]):
                    return False
        return True