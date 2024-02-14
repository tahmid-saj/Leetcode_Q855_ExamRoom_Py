class OrderedSet:
    def __init__(self, n):
        self.set = []
        self.n = n - 1
    
    def add(self):
        if len(self.set) == 0:
            self.set.append(0)
            return 0
        elif len(self.set) == 1:
            startDist = self.set[0]
            endDist = self.n - self.set[0]
            if endDist - startDist > 1:
                self.set.append(self.n)
                self.set.sort()
                return self.n
            else:
                self.set.append(0)
                self.set.sort()
                return 0

        i, j = self.getSpacing()
        seat = i + (j - i) // 2
        self.set.append(seat)
        self.set.sort()
        return seat

    def findByOrder(self, k):
        if k < 0 or k >= len(self.set): return None
        return self.set[k]
    
    def remove(self, k):
        self.set.remove(k)
    
    def getSpacing(self):
        l, r = 0, 0
        for i in range(len(self.set) - 1):
            if (self.set[i + 1] - self.set[i]) - (r - l) > 1: 
                l = self.set[i]
                r = self.set[i + 1]
        return l, r

class ExamRoom:

    def __init__(self, n: int):
        self.os = OrderedSet(n)

    def seat(self) -> int:
        return self.os.add()

    def leave(self, p: int) -> None:
        return self.os.remove(p)
