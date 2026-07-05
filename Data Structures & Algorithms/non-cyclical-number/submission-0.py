class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.squareofsum(n)
            if n==1:
                return True
            
        return False
    def squareofsum(self,n:int)->bool:
        sum=0
        while n>0:
            digit=n%10
            digit=digit**2
            sum+=digit
            n=n//10
        return sum

        