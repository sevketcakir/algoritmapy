import sys
from antlr4 import *
from AlgoritmaLexer import AlgoritmaLexer
from AlgoritmaParser import AlgoritmaParser
from AlgoritmaOlusturucu import *

class AlgoritmaYorumlayici:
    degiskenler = {}

    @classmethod
    def degisken_al(cls, degisken):
        # Kullanıcıdan değişken değeri al ve hafızaya ekle
        deger = float(input(f'{degisken} değerini girin: '))
        cls.degiskenler[degisken] = deger

    @classmethod
    def degisken_ata(cls, degisken, deger):
        # Değişkene değer ata
        cls.degiskenler[degisken] = deger

    @classmethod
    def deger_al(cls, degisken):
        # Değişkenin değerini hafızadan al
        return cls.degiskenler[degisken]

    @classmethod
    def degerlendir(cls, satirlar):
        satirno = min(satirlar.keys())
        sonuc = satirno
        while sonuc is not None:
            satir = satirlar[satirno]
            sonuc = satir.isle()
            if sonuc == -1:
                satirno += 1
            else:
                satirno = sonuc



def main(argv):
    input = FileStream(argv[1], encoding='utf8')
    lexer = AlgoritmaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AlgoritmaParser(stream)
    tree = parser.prog()
    alg = AlgoritmaOlusturucu()
    walker = ParseTreeWalker()
    walker.walk(alg, tree)
    AlgoritmaYorumlayici.degerlendir(alg.satirlar)


if __name__ == '__main__':
    main(sys.argv)