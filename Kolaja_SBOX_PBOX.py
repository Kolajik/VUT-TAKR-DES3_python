sub_box = [
        
        # S1
		[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		# S2
		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		# S3
		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		# S4
		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		# S5
		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		# S6
		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		# S7
		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		# S8
		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]
    
p_box = [
		16, 7, 20, 21, 29, 12,
		28, 17, 1, 15, 23, 26,
		5, 18, 31, 10, 2, 8,
		24, 14, 32, 27, 3, 9,
		19, 13, 30, 6, 22, 11,
		4, 25
	    ]

def s_box_a_p_box(v):
    p = []
    vys_sub = []
    while v:
        p.append(v[:6])
        v = v[6:]
    
#    print(p)

                                                                                                  #Funkce substitucnich tabulek
    for i in range(0,8):
        vyt = p[i]
        row_s = (vyt[0]+vyt[5]).zfill(4)                                                          #Vytvoreni cisla radku substitucni tabulky z prvniho a posledniho bitu 6ti bitoviho cisla
        col_s = (vyt[1]+vyt[2]+vyt[3]+vyt[4]).zfill(4)                                            #Vytvoreni cisla sloupce substitucni tabulky z 2.,3.,4. a 5. bitu 6ti bitoveho cisla
#        print("Sifrovani:\n")
#        print("Radek: "+str(row_s)+", decimalne: "+str(int(row_s,2)))
#        print("Sloupec: "+str(col_s)+", decimalne: "+str(int(col_s,2)))
        #print(sub_box[ktera_sub_tabulka][int(row_s,2)][int(col_s,2)])
        vys_sub.append(bin(sub_box[i][int(row_s,2)][int(col_s,2)])[2:].zfill(4))                  #Prirazeni vysledneho cisla ze substitucni tabulky do pole
        #vys_sub.append(bin(sub_box[ktera_sub_tabulka][row_s][col_s])[2:].zfill(4))
#    print(str(vys_sub))
#    for i in range(0,8):
#        vys_sub[i] = bin(vys_sub[i])[2:].zfill(4)
    vys_sub = ''.join(vys_sub)
#    print("Substituovane: "+vys_sub)

                                                                                                  # Permutace
    vys_per = []
    for i in range(0,len(p_box)):
        x = p_box[i]
        vys_per.append(vys_sub[x-1])
#        if vys_per[i] != vys_sub[x-1]:                                                            # just checking...
#            print("Tento bit: "+str(i)+" se nerovna!")
#            break
    vys_per = ''.join(vys_per)
#    print(vys_per)
    return vys_per