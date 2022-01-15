def vytvoreni_klicu(vstup_klic):
    t1=[57,49,41,33,25,17,9, 1,58,50,42,34,26,18, 10,2,59,51,43,35,27, 19,11,3,60,52,44,36, 63,55,47,39,31,23,15, 7,62,54,46,38,30,22, 14,6,61,53,45,37,29, 21,13,5,28,20,12,4]
    t2=[14,17,11,24,1,5, 3,28,15,6,21,10, 23,19,12,4,26,8, 16,7,27,20,13,2, 41,52,31,37,47,55, 30,40,51,45,33,48, 44,49,39,56,34,53, 46,42,50,36,29,32]
    shift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    Kp=[]; L = []; R = []; Vk = []; Vpk = [];

    for num in t1:
        Kp.append(vstup_klic[num-1])

    Kp = ''.join(Kp)
#    print(Kp)

    C0 = Kp[:28]
    D0 = Kp[28:]

#    print(str(C0))
#    print(str(D0))
#    print('C0= '+ str(C0))
#    print('D0= '+ str(D0))

        #Shift levych klicu
    for i in range(0,16):
        k = shift[i]
        if i == 0:
            L.append(C0[k::] + C0[:k])
        else:
            L.append(L[i-1][k::] + L[i-1][:k])
#        print(str(i+1)+". levy klic: "+L[i])

        #Shift pravych klicu
    for i in range(0,16):
        k = shift[i]
        if i == 0:
            R.append(D0[k::] + D0[:k])
        else:
            R.append(R[i-1][k::] + R[i-1][:k])
#        print(str(i+1)+". pravy klic: "+R[i])

        #Spojeni pravych a levych stran klicu
    for i in range(0,16):
        Vk.append(L[i]+R[i])
#        print(str(i+1)+". vysledny klic: "+Vk[i])

        #Permutace klicu do vyslednych klicu
    for i in range(0,16):
        pom_pole = []
        pom = Vk[i]
        for num in t2:
            pom_pole.append(pom[num-1])
        pom = ''.join(pom_pole)
        Vpk.append(pom)
#        print(str(i)+". vysledne klice, zpermutovane: "+Vpk[i])
    return Vpk