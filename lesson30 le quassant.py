class akun:
    def __init__(self, saldo):
        self._saldo = saldo 

a = akun(100_000)
print(a._saldo)

class Profil:
    def __init__(self, nama):
        self._nama = nama 

    @property
    def nama(self):
        return self.nama 
    
p = Profil("dara")
print(p.nama)

class dompet:
    def __init__(self, saldo=0):
        self._saldo = 0; self.saldo = saldo

    @property 
    def saldo(self): return self._saldo
    @saldo.setter
    def saldo(self, v):
        assert v >= 0, "saldo tidak boleh negatip"
        self._saldo = v

    def topup(self, n):
        assert n > 0, "Topup harus > 0"
        self._saldo += n

    def bayar(self, n):
        assert 0 < n <= self.saldo, "Pembayaran tidak valid"
        self._saldo -= n



