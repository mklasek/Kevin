class FixedSizeQueue:
    queue = []
    length = 0

    def __init__(self, length):
        self.queue = [None] * length
        self.length = length

    def push(self, member):
        j = 0
        while self.queue[j] == None:
            j = j + 1
            if j > self.length - 1:
                break

        if j == 0:
            self.out()
            self.push(member)
            return 1

        self.queue[j - 1] = member
        return 1

    def out(self):                                   # doesnt work properly
        outtage = self.queue[self.length - 1]

        for j in reversed(range(self.length)):
            if j > 0:
                self.queue[j] = self.queue[j - 1]
            else:
                self.queue[0] = None

        return outtage

    def print(self):
        print(self.queue)


