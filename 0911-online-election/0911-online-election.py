class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tally = {persons[0]: 1}

        leader = [persons[0]]
        
        for i in range(1, len(persons)):
            person = persons[i]
            tally[person] = tally.get(person, 0) + 1
            if tally[leader[-1]] <= tally[person]:
                leader.append(person)
            else:
                leader.append(leader[-1])
        
        self.leaderArray = leader
        self.times = times
        

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if t > self.times[mid]:
                left = mid + 1
            elif t < self.times[mid]:
                right = mid - 1
            else:
                right = mid
                break
        
        return self.leaderArray[right]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)