class CountSquares:

    def __init__(self):
        self.ptscount=defaultdict(int)
        self.points=[]
        

    def add(self, point: List[int]) -> None:
        self.ptscount[tuple(point)]+=1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.points:
            if (abs(py-y)!=abs(px-x)) or px==x or y==py:
                continue
            res+=self.ptscount[(x,py)]*self.ptscount[(px,y)]
        return res
            
        
        
        
