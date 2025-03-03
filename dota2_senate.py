from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_voters = deque() 
        d_voters = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                r_voters.append(i)
            else:
                d_voters.append(i)

        n = len(senate)    
        while r_voters and d_voters:
            r = r_voters[0]
            d = d_voters[0]
            if r < d:
                d_voters.popleft()
                r_voters.append(n)
                n += 1
                r_voters.popleft() 
            else:
                r_voters.popleft() 
                d_voters.append(n)
                n += 1
                d_voters.popleft()
        
        return "Radiant" if len(r_voters) else "Dire"
