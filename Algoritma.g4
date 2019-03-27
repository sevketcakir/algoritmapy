grammar Algoritma;
prog:	BASLA (satir)* DUR;
ifade:	ifade ('*'|'/'|'%') ifade      # CarpBol
     |	ifade ('+'|'-') ifade          # ToplaCikar
     |	SAYI                           # Sayi
     |	DEGISKEN                       # Degisken
     |	'(' ifade ')'                  # Parantez
    ;

ACIKLAMA : '@' .*? '\r'? '\n' -> skip ;
SATIRNO : [0-9]+ '.';
SAYI    : [0-9]+ ('.' [0-9]+)?;
BASLA   : SATIRNO (' ')? 'başla' ;
DUR     : SATIRNO (' ')? 'dur' ;
metin   : '"' (metin_ici|.)*? '"' ;//metin tanımı pushmode popmode ile yapılmalı. şu an sorunlu...
metin_ici : '#{' ifade '}';
satir   : SATIRNO komut ACIKLAMA?;
komut   : 'yaz' (ifade|metin)                                 # Yaz
        | 'git' SATIRNO                                       # Git
        | 'eğer' kosul 'ise' komut ('yoksa' komut)?           # Eger
        | atama (',' atama)*                                  # Atamalar
        | DEGISKEN (',' DEGISKEN)* 'al'                       # Girdi
        ;
kosul   : kosul 've' kosul          # Ve
		| kosul 'veya' kosul        # Veya
        | kosul 'değil'             # Degil
		| ifade KARSOP ifade        # Karsilastir
		| '(' kosul ')'             # ParantezKosul
    ;
atama: DEGISKEN ATAMOP ifade;
WS  : [ \t\r\n]+ -> skip ;
DEGISKEN : [a-zA-Z] [a-zA-Z0-9_]*;
ARITOP: '*'|'/'|'%'|'+'|'-';
KARSOP: '<'|'>'|'=='|'!='|'<='|'>=';
ATAMOP: '='|'+='|'-='|'*='|'/='|'%=';
