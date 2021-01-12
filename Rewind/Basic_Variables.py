
saatlikgirdi = int(input("Kac saat calistiginizi giriniz  "))
oran_girdisi = int(input("oran giriniz"))
maas = hesaplayici(saatlik_girdi,oran_girdisi)


def hesaplayici(saatlik_girdi,oran_girdisi):
    if saatlik_girdi > 40:
        maas = (saatlik_girdi - 40)*oran_girdisi*1.5 +(40 * oran_girdisi)
    else:
        (saatlik_girdi*oran_girdisi)
    return maas
    
print("Toplam Maas",maas)