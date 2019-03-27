# Algoritma Yorumlayıcı
Algoritma yorumlayıcı sıralı satırlarda bulunan komutları işleyerek sonuçlar verir. Satırlarda bir yönlendirme 
komutu yoksa komutlar çalıştırıldıktan sonra bir sonraki satırdan itibaren çalışmaya devam eder.

Uygulamayı çalıştırabilmek için Python 3 gereklidir. Gereksinimler için aşağıdakilerden birisi çalıştırılabilir.
```bash
pip install antlr4-python3-runtime
# veya
pip install -r requirements.txt
# Kaynak kodu yorumlamak için
python AlgoritmaYorumlayici.py algoritma.alg
```

## Aritmetik Operatörler
| Operatör | İşlev            |
|----------|------------------|
| +        | Toplama          |
| -        | Çıkarma          |
| *        | Çarpma           |
| /        | Bölme            |
| %        | Mod              |

## Karşılaştırma Operatörleri
| Operatör |
|----------|
| ve       |
| veya     |
| değil    |

## Atama Operatörleri
| Operatör | İşlev            |
|----------|------------------|
| =        | Atama            |
| +=       | Artırarak atama  |
| -=       | Azaltarak atama  |
| *=       | Çarparak atama   |
| /=       | Bölerek atama    |
| %=       | Mod alarak atama |

## Komutlar
| Komut | Kullanım                         |
|-------|----------------------------------|
| başla | başla                            |
| dur   | dur                              |
| Girdi | d1,d2,... al                     |
| yaz   | yaz d1                           |
|       | yaz "metin"                      |
|       | yaz "a+b=#{a+b}"                 |
| Atama | x=5, t=12, k=1,...               |
|       | y=(x+5)*4                        |
|       | z *= 2                           |
| Koşul | x>5                              |
| Eğer  | eğer koşul ise komut             |
|       | eğer koşul ise komut yoksa komut |
| Git   | git 1.                           |

## Örnek Asal Sayı Algoritması
```
@Bu algoritma kullanıcının girdiği n sayısından küçük
@asal sayıları yazdırır
1. başla
2. n al @ n sayısını kullanıcıdan al
3. sayi=2 @ ilk asal sayı
4. eğer sayi>=n ise git 13.
5. i=2
6. eğer i>=sayi ise git 10. @ buraya gelmişse tam böleni yok
7. eğer sayi%i==0 ise git 11. @tam böleni varsa sonraki sayıya git
8. i =i+1
9. git 6. @döngü devam
10. yaz sayi @ asaldır, yazdır.
11. sayi=sayi+1
12. git 4. @dıştaki döngü devam
13. dur
```

## Hatalar/Buglar/Eksiklikler
- Sayılar sadece float türünde
- Metin tanımlamasında problem var. pushMode ve popMode kullanılarak yapılmalı
- Yorumlayıcı sadece dosyadan alıyor, standart input kullanmıyor
- Gramer içindeki operatörler için kısa adlar kullanılabilir(op='+'|'-' gibi).
- Metinler ifadelere dahil edilebilir.
- Açıklama için @ yerine # kullanılabilir. Şu an gramerde kullanılmadığı için @ kullanılıyor
- Şu an satır numaraları ardışık olmak zorunda. 10. satır 1 20. satır 2... şeklinde olabilir
