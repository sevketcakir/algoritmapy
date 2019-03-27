from AlgoritmaParser import *
from AlgoritmaListener import AlgoritmaListener
from Siniflar import *


class AlgoritmaOlusturucu(AlgoritmaListener):

    def __init__(self) -> None:
        self.stack = []
        self.satirlar = {}

    def enterProg(self, ctx: AlgoritmaParser.ProgContext):
        super().enterProg(ctx)

    def exitProg(self, ctx: AlgoritmaParser.ProgContext):
        for s in reversed(ctx.children):
            if hasattr(s, 'symbol') and 'başla' in s.symbol.text:
                st = s.symbol.text
                sno = int(st.replace('başla', '').strip().replace('.', ''))
                self.satirlar[sno] = Satir(sno, Basla(sno))
            elif hasattr(s, 'symbol') and 'dur' in s.symbol.text:
                st = s.symbol.text
                sno = int(st.replace('dur', '').strip().replace('.', ''))
                self.satirlar[sno] = Satir(sno, Dur())
            else:
                sno = int(s.children[0].symbol.text.replace('.', ''))
                self.satirlar[sno] = Satir(sno, self.stack.pop())

    def enterDegisken(self, ctx: AlgoritmaParser.DegiskenContext):
        return Degisken(ctx.getText())

    def exitDegisken(self, ctx: AlgoritmaParser.DegiskenContext):
        self.stack.append(Degisken(ctx.getText()))

    def enterCarpBol(self, ctx: AlgoritmaParser.CarpBolContext):
        super().enterCarpBol(ctx)

    def exitCarpBol(self, ctx: AlgoritmaParser.CarpBolContext):
        sag = self.stack.pop()
        sol = self.stack.pop()
        if ctx.getChild(1).symbol.text == '*':
            self.stack.append(Carp(sol, sag))
        elif ctx.getChild(1).symbol.text == '/':
            self.stack.append(Bol(sol, sag))
        else:
            self.stack.append(Mod(sol, sag))

    def enterParantez(self, ctx: AlgoritmaParser.ParantezContext):
        super().enterParantez(ctx)

    def exitParantez(self, ctx: AlgoritmaParser.ParantezContext):
        super().exitParantez(ctx)

    def enterSayi(self, ctx: AlgoritmaParser.SayiContext):
        super().enterSayi(ctx)

    def exitSayi(self, ctx: AlgoritmaParser.SayiContext):
        self.stack.append(Sayi(ctx.getText()))

    def enterToplaCikar(self, ctx: AlgoritmaParser.ToplaCikarContext):
        super().enterToplaCikar(ctx)

    def exitToplaCikar(self, ctx: AlgoritmaParser.ToplaCikarContext):
        sag = self.stack.pop()
        sol = self.stack.pop()
        if ctx.getChild(1).symbol.text == '+':
            self.stack.append(Topla(sol, sag))
        else:
            self.stack.append(Cikar(sol, sag))


    def enterMetin(self, ctx: AlgoritmaParser.MetinContext):
        super().enterMetin(ctx)

    def exitMetin(self, ctx: AlgoritmaParser.MetinContext):
        i=0
        metin=""
        metin_liste=[]
        for child in ctx.getChildren():
            if(type(child) == AlgoritmaParser.Metin_iciContext):
                metin_liste.append(self.stack.pop())
                metin += "#{}"
            elif child.symbol.text != '"':
                metin += child.symbol.text
        self.stack.append(Metin(metin, metin_liste))
        super().exitMetin(ctx)

    def enterMetin_ici(self, ctx: AlgoritmaParser.Metin_iciContext):
        super().enterMetin_ici(ctx)

    def exitMetin_ici(self, ctx: AlgoritmaParser.Metin_iciContext):
        super().exitMetin_ici(ctx)

    def enterSatir(self, ctx: AlgoritmaParser.SatirContext):
        super().enterSatir(ctx)

    def exitSatir(self, ctx: AlgoritmaParser.SatirContext):
        super().exitSatir(ctx)

    def enterYaz(self, ctx: AlgoritmaParser.YazContext):
        super().enterYaz(ctx)

    def exitYaz(self, ctx: AlgoritmaParser.YazContext):
        self.stack.append(Yaz(self.stack.pop()))

    def enterGit(self, ctx: AlgoritmaParser.GitContext):
        super().enterGit(ctx)

    def exitGit(self, ctx: AlgoritmaParser.GitContext):
        self.stack.append(Git(ctx.getChild(1).symbol.text))

    def enterEger(self, ctx: AlgoritmaParser.EgerContext):
        super().enterEger(ctx)

    def exitEger(self, ctx: AlgoritmaParser.EgerContext):
        if ctx.getChildCount() == 4:
            dogruysa = self.stack.pop()
            kosul = self.stack.pop()
            self.stack.append(Eger(kosul, dogruysa, None))
        elif ctx.getChildCount() == 6:
            yanlissa = self.stack.pop()
            dogruysa = self.stack.pop()
            kosul = self.stack.pop()
            self.stack.append(Eger(kosul, dogruysa, yanlissa))

    def enterAtamalar(self, ctx: AlgoritmaParser.AtamalarContext):
        super().enterAtamalar(ctx)

    def exitAtamalar(self, ctx: AlgoritmaParser.AtamalarContext):
        atama_listesi = []
        for atama in ctx.children:
            if type(atama) == AlgoritmaParser.AtamaContext:
                atama_listesi.append(self.stack.pop())
        self.stack.append(Atamalar(atama_listesi))

    def enterGirdi(self, ctx: AlgoritmaParser.GirdiContext):
        super().enterGirdi(ctx)

    def exitGirdi(self, ctx: AlgoritmaParser.GirdiContext):
        girdi_listesi = []
        for child in ctx.getChildren():
            if child.symbol.text != ',' and child.symbol.text != 'al':
                girdi_listesi.append(child.symbol.text)
        self.stack.append(Girdi(girdi_listesi))

    def enterDegil(self, ctx: AlgoritmaParser.DegilContext):
        super().enterDegil(ctx)

    def exitDegil(self, ctx: AlgoritmaParser.DegilContext):
        super().exitDegil(ctx)

    def enterKarsilastir(self, ctx: AlgoritmaParser.KarsilastirContext):
        super().enterKarsilastir(ctx)

    def exitKarsilastir(self, ctx: AlgoritmaParser.KarsilastirContext):
        sag = self.stack.pop()
        sol = self.stack.pop()
        self.stack.append(Karsilastir(ctx.getChild(1).symbol.text, sol, sag))

    def enterParantezKosul(self, ctx: AlgoritmaParser.ParantezKosulContext):
        super().enterParantezKosul(ctx)

    def exitParantezKosul(self, ctx: AlgoritmaParser.ParantezKosulContext):
        super().exitParantezKosul(ctx)

    def enterVe(self, ctx: AlgoritmaParser.VeContext):
        super().enterVe(ctx)

    def exitVe(self, ctx: AlgoritmaParser.VeContext):
        sol = self.stack.pop()
        sag = self.stack.pop()
        self.stack.append(Ve(sol, sag))

    def enterVeya(self, ctx: AlgoritmaParser.VeyaContext):
        super().enterVeya(ctx)

    def exitVeya(self, ctx: AlgoritmaParser.VeyaContext):
        sol = self.stack.pop()
        sag = self.stack.pop()
        self.stack.append(Veya(sol, sag))

    def enterAtama(self, ctx: AlgoritmaParser.AtamaContext):
        super().enterAtama(ctx)

    def exitAtama(self, ctx: AlgoritmaParser.AtamaContext):
        self.stack.append(Atama(ctx.getChild(0).symbol.text,ctx.getChild(1).symbol.text,self.stack.pop()))