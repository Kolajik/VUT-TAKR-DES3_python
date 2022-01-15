from Hirs_klice import *
from Kolaja_SBOX_PBOX import *
from Jelinek_IP_EF_FP_XOR import *
from Sifrovani import *
from Desifrovani import *
from string_2_bits_and_reverse import *
import tkinter as tk
import time
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

spravnost = True
while(spravnost):
#Vytvoření klíčů z uživatelova hesla
    uz_heslo = input("Zadej osmimistny klic: \n")
    uz_heslo = string2bits(uz_heslo)
    uz_heslo = ''.join(uz_heslo)
    if len(uz_heslo) == 64:
        klice = vytvoreni_klicu(uz_heslo)
        spravnost = False
    else:
        print("Sorry, spatna delka klice :(")

uz_vstup = ''
hehe = 0
while uz_vstup != 'Q':
    print("Sifrovat text ze souboru....E")
    print("Desifrovat soubor...........D")
    print("Sifruj pomoci 3-DES.........TE")
    print("Desifruj pomoci 3-DES.......TD")
    print("Zavrit aplikaci.............Q\n")
    uz_vstup = input("Vyber funkci DES: ")
    uz_vstup = uz_vstup.upper()
    if uz_vstup == 'E':                                                         #SIFROVANI
        print("Zadej cestu ke vstupnimu souboru: ")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        fo = open(file_path, "r+")
        s = fo.read()
        
        encrypted = DES_encrypt(klice, s)

        print("Zadej cestu vystupniho souboru (do nej se ti ulozi sifra v binarnich cislech): ")
        f = asksaveasfilename()
        output_file_e = open(f,"wb")
        output_file_e.write(bytes(encrypted, 'UTF-8'))
        output_file_e.close()
                                                                                #DESIFROVANI
    elif uz_vstup == 'D':
        print("Zadej cestu ke vstupnimu souboru: ")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        fo = open(file_path, "r+")
        s = fo.read()
        
        decrypted = DES_decrypt(klice, s)
        o = []
        pp = decrypted
        while pp:
            o.append(pp[:8])
            pp = pp[8:]
        pb = bits2string(o)

        print("Zadej cestu vystupniho souboru (do nej se ti ulozi desifrovany text): ")
        f = asksaveasfilename()
        output_file_d = open(f,"wb")
        output_file_d.write(bytes(pb, 'UTF-8'))
        output_file_d.close()
                                                                                #SIFROVANI TRIPLE DES 
    elif uz_vstup == 'TE':
        klice2 = []
        uz_heslo = input("Zadej druhy, osmimistny klic, potrebny k Triple DES: \n")
        uz_heslo = string2bits(uz_heslo)
        uz_heslo = ''.join(uz_heslo)
        if len(uz_heslo) == 64:
            klice2 = vytvoreni_klicu(uz_heslo)
            spravnost = False
        else:
            print("Sorry, spatna delka klice :(")
        print("Zadej cestu ke vstupnimu souboru: ")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        fo = open(file_path, "r+")
        s = fo.read()
        
        encrypted_first = DES_encrypt(klice, s)
        decrypted_second = DES_decrypt(klice2,encrypted_first)
        encrypted_third = DES_encrypt(klice, decrypted_second)

        print("Zadej cestu vystupniho souboru (do nej se ti ulozi desifrovany text): ")
        f = asksaveasfilename()
        output_file_tdes_e = open(f,"wb")
        output_file_tdes_e.write(bytes(encrypted_third, 'UTF-8'))
        output_file_tdes_e.close()
                                                                                #DESIFROVANI TRIPLE DES
    elif uz_vstup == 'TD':
        klice2 = []
        uz_heslo = input("Zadej druhy, osmimistny klic, potrebny k Triple DES: \n")
        uz_heslo = string2bits(uz_heslo)
        uz_heslo = ''.join(uz_heslo)
        if len(uz_heslo) == 64:
            klice2 = vytvoreni_klicu(uz_heslo)
            spravnost = False
        else:
            print("Sorry, spatna delka klice :(")
        print("Zadej cestu ke vstupnimu souboru: ")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        fo = open(file_path, "r+")
        s = fo.read()
        
        decrypted_first = DES_decrypt(klice, s)
        encrypted_second = DES_encrypt(klice2, decrypted_first)
        decrypted_third = DES_decrypt(klice, encrypted_second)

        o = []
        pp = decrypted_third
        while pp:
            o.append(pp[:8])
            pp = pp[8:]
        pb = bits2string(o)
        
        print("Zadej cestu vystupniho souboru (do nej se ti ulozi desifrovany text): ")
        f = asksaveasfilename()
        output_file_tdes_d = open(f,"wb")
        output_file_tdes_d.write(bytes(pb, 'UTF-8'))
        output_file_tdes_d.close()
    elif uz_vstup == 'Q':
        quit()
    else:
        if hehe == 0:
            print("Vsak tam mas menu, tak si vyber nekterou z moznosti v nabidce a nemackej mi nic jinyho ;)\n")
        if hehe == 1:
            print("Neboj se, mam to osetrene..\n")
        if hehe == 2:
            print("Ty se proste musis ujistovat, ze?\n")
        if hehe == 3:
            print("Je docela pozde, asi by jsi mel jit spat :)\n")
        if hehe == 4:
            print("Uz to, prosim, nezkousej..\n")
        if hehe == 5:
            print("No nic, na to nemam sily... Ukoncuji se za 10 vterin.")
            dejvtubyl = True
            i = 10
            while dejvtubyl:
                print(i)
                i -= 1
                time.sleep(1)
                if i == 0:
                    dejvtubyl = False
            quit()
        hehe += 1