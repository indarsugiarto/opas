""" Kelas opasData berisi struktur data untuk menyimpan
    parameter-parameter program terkait station ketika dijalankan.
    """
    
class opasData():
    def __init__(self, nStation):
        self.vol = [0 for _ in range(nStation)]
        self.info = ["" for _ in range(nStation)]
        self.ip = ["" for _ in range(nStation)]
        self.muted = [False for _ in range(nStation)]
        
    def map(self,sID,ip):
        """ Note: sID adalah station-ID yang dimulai dari 1 """
        self.ip[int(sID)-1] = ip
