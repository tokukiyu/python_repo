class Solution(object):
    def __init__(self):
        self.radiant = 0
        self.dire = 0
    
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = str(senate)
        if senate[0] != senate[-1]:
            senate = senate.replace(senate[-1], senate[0])
            if senate[0] == "R":
                self.radiant += 1
            else:
                self.dire += 1
        else:
            senate = senate[:-1]
            senate = senate.replace(senate[-1], senate[0])
            if senate[0] == "R":
                self.radiant -= 1
                senate = senate[1:]
            else:
                self.dire -= 1
                senate = senate[1:]
        
        if self.radiant <= 0:
            return "Dire"
        elif self.dire <= 0:
            return "Radiant"
        else:
            return self.predictPartyVictory(senate)

s = Solution()
print(s.predictPartyVictory("rdd"))
