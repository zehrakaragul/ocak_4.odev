# Kullanıcıdan 5 adet sayı alıp liste oluşturma ve gerekli işlemleri yapma
def sayi_islemleri():
    sayilar = []
    # Kullanıcıdan 5 sayı alıyoruz
    for i in range(5):
        sayi = float(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)
    
    # Listenin toplamı
    toplam = sum(sayilar)
    
    # Listenin ortalaması
    ortalama = toplam / len(sayilar)
    
    # En büyük ve en küçük eleman
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    
    # Sonuçları yazdırma
    print(f"Liste: {sayilar}")
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama}")
    print(f"En büyük eleman: {en_buyuk}")
    print(f"En küçük eleman: {en_kucuk}")

# Kullanıcıdan kelimeler alıp, listeye ekleyip ters sıralama
def kelime_tersten():
    kelimeler = []
    # Kullanıcıdan kelimeler alıyoruz
    print("\nKelime eklemek için 'bitir' yazın.")
    while True:
        kelime = input("Bir kelime girin: ")
        if kelime.lower() == 'bitir':
            break
        kelimeler.append(kelime)
    
    # Kelimeleri ters sıraya koyma
    kelimeler.sort(reverse=True)
    print(f"Ters sıralanmış kelimeler: {kelimeler}")

# Bir listeden tekrar eden elemanları kaldırma
def tekrarlananlari_kaldir():
    liste = []
    # Kullanıcıdan elemanları alıyoruz
    print("\nListeye eleman eklemek için 'bitir' yazın.")
    while True:
        eleman = input("Bir eleman girin: ")
        if eleman.lower() == 'bitir':
            break
        liste.append(eleman)
    
    # Tekrar eden elemanları kaldırma (set kullanarak)
    liste = list(set(liste))
    print(f"Tekrarlananlar kaldırıldı: {liste}")

# Ana program
def main():
    # 1. Görev: Kullanıcıdan 5 adet sayı alıp liste işlemleri yapma
    sayi_islemleri()

    # 2. Görev: Kullanıcıdan kelimeler alıp ters sıralama
    kelime_tersten()

    # 3. Görev: Bir listeden tekrar eden elemanları kaldırma
    tekrarlananlari_kaldir()

# Programı çalıştırma
main()
