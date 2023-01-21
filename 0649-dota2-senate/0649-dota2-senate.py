class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        hash={'R':'D','D':'R'}
        ans={'R':'Radiant','D':'Dire'}
        lst=list(senate)

        while len(lst)>1:
            try:
                lst.append(lst[0])
                lst=lst[1:]
                #print(lst)
                lst.remove(hash[lst[-1]])  
            except:
                return ans[lst[0]]
        return ans[lst[0]]