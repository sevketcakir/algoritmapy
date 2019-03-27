from AlgoritmaYorumlayici import AlgoritmaYorumlayici
class Ifade:
    # ifade interface
    def deger(self):
        pass


class Kosul:
    def deger(self):
        pass

class Satir:
    # Satir interface
    def __init__(self, satirno, komut):
        self.satirno = satirno
        self.komut = komut

    def isle(self):
        return self.komut.isle()


class Komut:
    def isle(self):
        pass


class Basla(Komut):
    def __init__(self, satirno):
        self.satirno = satirno

    def isle(self):
        return -1


class Dur(Komut):
    def isle(self):
        return None


class Yaz(Komut):
    def __init__(self, yazilacak):
        self.yazilacak = yazilacak

    def isle(self):
        print(self.yazilacak.deger())
        return -1


class Git(Komut):
    def __init__(self, satirno):
        self.satirno = int(satirno.replace('.',''))

    def isle(self):
        return self.satirno


class Eger(Komut):
    def __init__(self, kosul, dogruysa, yanlissa):
        self.kosul = kosul
        self.dogruysa = dogruysa
        self.yanlissa = yanlissa

    def isle(self):
        if self.kosul.deger():
            return self.dogruysa.isle()
        elif self.yanlissa is not None:
            return self.yanlissa.isle()
        else:
            return -1 # yoksa kısmı boş, alt satıra geç...

class Atamalar(Komut):
    def __init__(self, atamalar):
        self.atamalar = atamalar

    def isle(self):
        for atama in self.atamalar:
            atama.isle()
        return -1

class Atama(Komut):
    def __init__(self, degisken, islec, ifade):
        self.degisken = degisken
        self.islec = islec
        self.ifade = ifade

    def isle(self):
        # bu kısım sınıflarla yapılacak new Bol(self.degisken, ...).deger() gibi
        ifade_degeri=self.ifade.deger()
        if self.islec == '=':
            AlgoritmaYorumlayici.degisken_ata(self.degisken, self.ifade.deger())
        elif self.islec == '+=':
            degisken_degeri = AlgoritmaYorumlayici.deger_al(self.degisken)
            AlgoritmaYorumlayici.degisken_ata(self.degisken, degisken_degeri+ifade_degeri)
        elif self.islec == '-=':
            degisken_degeri = AlgoritmaYorumlayici.deger_al(self.degisken)
            AlgoritmaYorumlayici.degisken_ata(self.degisken, degisken_degeri-ifade_degeri)
        elif self.islec == '*=':
            degisken_degeri = AlgoritmaYorumlayici.deger_al(self.degisken)
            AlgoritmaYorumlayici.degisken_ata(self.degisken, degisken_degeri*ifade_degeri)
        elif self.islec == '/=':
            degisken_degeri = AlgoritmaYorumlayici.deger_al(self.degisken)
            AlgoritmaYorumlayici.degisken_ata(self.degisken, degisken_degeri/ifade_degeri)
        elif self.islec == '%=':
            degisken_degeri = AlgoritmaYorumlayici.deger_al(self.degisken)
            AlgoritmaYorumlayici.degisken_ata(self.degisken, degisken_degeri%ifade_degeri)
        return -1


class Girdi(Komut):
    def __init__(self, degisken_listesi):
        self.degisken_listesi = degisken_listesi

    def isle(self):
        for degisken in self.degisken_listesi:
            AlgoritmaYorumlayici.degisken_al(degisken)
        return -1


class Ve(Kosul):
    def __init__(self, sol, sag):
        self.sol = sol
        self.sag = sag

    def deger(self):
        return self.sol.deger() and self.sag.deger()


class Veya(Kosul):
    def __init__(self, sol, sag):
        self.sol = sol
        self.sag = sag

    def deger(self):
        return self.sol.deger() or self.sag.deger()


class Degil(Kosul):
    def __init__(self, kosul):
        self.kosul = kosul

    def deger(self):
        return not self.kosul


class Karsilastir(Kosul):
    def __init__(self, islec, sol, sag):
        self.islec = islec
        self.sol =sol
        self.sag = sag

    def deger(self):
        if self.islec == '==':
            return self.sol.deger() == self.sag.deger()
        elif self.islec == '!=':
            return self.sol.deger() != self.sag.deger()
        elif self.islec == '<':
            return self.sol.deger() < self.sag.deger()
        elif self.islec == '>':
            return self.sol.deger() > self.sag.deger()
        elif self.islec == '<=':
            return self.sol.deger() <= self.sag.deger()
        elif self.islec == '>=':
            return self.sol.deger() >= self.sag.deger()

#TODO: Aritmetik işlem sınıfları...
class Infix(Ifade):
    def __init__(self, sol, sag):
        self.sol = sol
        self.sag = sag

    def deger(self):
        pass


class Carp(Infix):
    def deger(self):
        return self.sol.deger() * self.sag.deger()


class Bol(Infix):
    def deger(self):
        return self.sol.deger() * self.sag.deger()


class Mod(Infix):
    def deger(self):
        return self.sol.deger() % self.sag.deger()


class Topla(Infix):
    def deger(self):
        return self.sol.deger() + self.sag.deger()


class Cikar(Infix):
    def deger(self):
        return self.sol.deger() - self.sag.deger()


class Degisken(Ifade):
    def __init__(self, degisken):
        self.degisken = degisken

    def deger(self):
        return AlgoritmaYorumlayici.deger_al(self.degisken)


class Sayi(Ifade):
    def __init__(self, degeri):
        self.degeri = float(degeri)

    def deger(self):
        return self.degeri


class Metin():
    def __init__(self, metin, liste):
        self.metin = metin
        self.liste = liste

    def deger(self):
        # ayrilmis = self.metin.split('#{}')
        hesaplanmis = [x.deger() for x in reversed(self.liste)]
        m = self.metin
        for h in hesaplanmis:
            m = m.replace("#{}", str(h), 1)
        return m
