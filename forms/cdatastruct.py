class opasData():
    def __init__(self, nStation):
        self.vol = [0 for _ in range(nStation)]
        self.info = ["" for _ in range(nStation)]
        self.ip = ["" for _ in range(nStation)]
        self.muted = [False for _ in range(nStation)]
        
    def map(self,sID,ip):
        self.ip[int(sID)-1] = ip
