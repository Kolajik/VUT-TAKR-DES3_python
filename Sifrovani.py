from Hirs_klice import *
from Kolaja_SBOX_PBOX import *
from Jelinek_IP_EF_FP_XOR import *
from string_2_bits_and_reverse import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def DES_encrypt(klice = [], s = ""):
    if (s[0] == '0' or s[0] == '1'):
        b = s
    else:
        b = string2bits(s)
        b = ''.join(b)
    pp = b
    o = []
    while pp:
        o.append(pp[:64])
        pp = pp[64:]
    if len(o[len(o)-1]) != 64:                                     #Padding nul k poslednímu prvku pole
        last_item_length = len(o[len(o)-1])
        adding = '0'*(64-last_item_length)
        o[len(o)-1] = o[len(o)-1]+adding
                                                                   #Iniciální permutace
    inic_permutovane = []
    for i in range(0,len(o)):
        inic_permutovane.append(InitialPermutation(o[i]))
                                                                   #Rozdìlení do 32-bit blokù (pravé a levé pùlky)
    L_half = []
    R_half = []
    for i in range(0,len(inic_permutovane)):
        moo = inic_permutovane[i]
        L_half.append(moo[:32])
        R_half.append(moo[32:])
#        print("L0: "+L_half[i])
#        print("R0: "+R_half[i])
                                                                   #RUNDY

    vysledek_DES = []
    for j in range(0,len(inic_permutovane)):
        L_round = [R_half[j],]
        R_round = []

        for i in range(0,16):
            if i == 0:
                expan = ExpansionFunction(R_half[j])
            else:
                expan = ExpansionFunction(R_round[i-1])
#                print("Expanze R0: "+expan)
            xoring = XOR_Key(int(expan,2),int(klice[i],2))
            xoring = bin(xoring)[2:].zfill(48)
#            print("Xorovane: "+xoring)
            subs = s_box_a_p_box(xoring)
#            print("Zpermutovane: "+subs)
            if i == 0:
                R_round.append(int(L_half[j],2) ^ int(subs,2))
                R_round[i] = bin(R_round[i])[2:].zfill(32)
            else:
                L_round.append(R_round[i-1])
                R_round.append(int(L_round[i-1],2) ^ int(subs,2))
                R_round[i] = bin(R_round[i])[2:].zfill(32)
#                print(bin(R_round[0])[2:])
        R16L16 = R_round[15]+L_round[15]
        fin_per = FinalPermutation(R16L16)
        vysledek_DES.append(fin_per)
#        print(fin_per)
#    print(len(vysledek_DES))
    vys_bit = ''.join(vysledek_DES)
#    print(vys_bit)
#    pb = vys_bit
#    pomoc_rozdel = []
#    while pb:
#        pomoc_rozdel.append(pb[:8])
#        pb = pb[8:]
                                                                   #Pøevedení sifry na hex (binarne)
#    pomoc_vysledku = []
#    for bajt in pomoc_rozdel:
#        pomoc_vysledku.append(hex((int(bajt,16)))[2:].zfill(8))

#    print(pomoc_vysledku)
#    total_out = ''.join(pomoc_rozdel)
    return vys_bit