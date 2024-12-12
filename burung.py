from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi ):
        super() .__init__( nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super() .cetak()
        print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')    
    
print('---- cetak burung ----')
print('---- objek pertama ----')

beo = Burung('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'saya lucu')
beo.cetak_burung()

#object kedua
print('\n---- objek kedua---')

merpati = Burung('Burung merpati', 'biji-bijian', 'udara', 'bertelur', 'blue and black', 'kamu lucu')
merpati.cetak_burung()
