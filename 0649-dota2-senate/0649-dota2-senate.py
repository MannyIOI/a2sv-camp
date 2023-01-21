class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banned = ""
        queue = deque([each for each in senate])
        vote_freq = Counter(senate)
        banned_count = 0
        
#         RRDDD
        """
        banned = ""
        banned_count = 0
        curr_vote = R
        counter_freq = {}
        
        RRDDD
        """
    
        while queue:
            curr_vote = queue.popleft()
            
            if vote_freq['D'] == 0:
                return 'Radiant'
            elif vote_freq['R'] == 0:
                return 'Dire'
            
            if banned_count > 0 and banned == curr_vote:
                banned_count -= 1
                vote_freq[banned] -= 1
                continue
            
            banned = "R" if curr_vote == "D" else "D"
            banned_count += 1
            
            queue.append(curr_vote)
            
            """
            RRDDD
            
            curr_vote           D
            vote_freq           {R: 1, D: 0}
            banned_count        0
            banned              D
            
            queue = [R
            """
            
            
            