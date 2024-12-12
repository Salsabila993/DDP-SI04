from animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular ):
        super() .__init__( nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular
        
    def cetak_ular(self):
        super(). cetak()
        print(f'Hewan ini berwarna {self.warna} dan hewan ini jenis {self.jenis}')
        
Taipan = Ular('ular Taipan', 'tikus', 'darat', 'bertelur', 'coklat tua', 'berbisa')
Taipan.cetak_ular()
