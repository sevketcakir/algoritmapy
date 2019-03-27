# Generated from /Users/cakir/code/antlr/Algoritma.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AlgoritmaParser import AlgoritmaParser
else:
    from AlgoritmaParser import AlgoritmaParser

# This class defines a complete generic visitor for a parse tree produced by AlgoritmaParser.

class AlgoritmaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmaParser#prog.
    def visitProg(self, ctx:AlgoritmaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Degisken.
    def visitDegisken(self, ctx:AlgoritmaParser.DegiskenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#CarpBol.
    def visitCarpBol(self, ctx:AlgoritmaParser.CarpBolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Parantez.
    def visitParantez(self, ctx:AlgoritmaParser.ParantezContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Sayi.
    def visitSayi(self, ctx:AlgoritmaParser.SayiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#ToplaCikar.
    def visitToplaCikar(self, ctx:AlgoritmaParser.ToplaCikarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#metin.
    def visitMetin(self, ctx:AlgoritmaParser.MetinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#metin_ici.
    def visitMetin_ici(self, ctx:AlgoritmaParser.Metin_iciContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#satir.
    def visitSatir(self, ctx:AlgoritmaParser.SatirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Yaz.
    def visitYaz(self, ctx:AlgoritmaParser.YazContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Git.
    def visitGit(self, ctx:AlgoritmaParser.GitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Eger.
    def visitEger(self, ctx:AlgoritmaParser.EgerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Atamalar.
    def visitAtamalar(self, ctx:AlgoritmaParser.AtamalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Girdi.
    def visitGirdi(self, ctx:AlgoritmaParser.GirdiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Degil.
    def visitDegil(self, ctx:AlgoritmaParser.DegilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Karsilastir.
    def visitKarsilastir(self, ctx:AlgoritmaParser.KarsilastirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#ParantezKosul.
    def visitParantezKosul(self, ctx:AlgoritmaParser.ParantezKosulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Ve.
    def visitVe(self, ctx:AlgoritmaParser.VeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#Veya.
    def visitVeya(self, ctx:AlgoritmaParser.VeyaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmaParser#atama.
    def visitAtama(self, ctx:AlgoritmaParser.AtamaContext):
        return self.visitChildren(ctx)



del AlgoritmaParser