""" si = 1
   moure disc ORIGEN -> DESTÍ
sino
   moure n-1 discos ORIGEN -> AUXILIAR
   moure disc ORIGEN -> DESTÍ
   moure n-1 discos AUXILIAR -> DESTÍ """

def hanoi(n,origen,destino,auxiliar):
    if n == 1:
        print(origen+" => " + destino)
    else:
        hanoi(n-1,origen,auxiliar,destino)
        print(origen+" => " + destino)
        hanoi(n-1,auxiliar,destino,origen)




hanoi(8,"torre1","torre3","torre2")