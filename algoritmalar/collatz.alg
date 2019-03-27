@ Bu algoritma bir sayının Collatz serisine göre 1'e kaç adımda ulaştığını
@ gösterir
0. başla
1. yaz "collatz-sanisi"
2. sayi al
3. adim = 0
4. eğer sayi == 1 ise git 8.
5. eğer sayi%2==0 ise sayi/=2 yoksa sayi=sayi*3+1
6. adim += 1
7. git 4.
8. yaz "#{adim} adim"
9. dur
