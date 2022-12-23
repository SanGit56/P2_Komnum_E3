import matplotlib.pyplot as plt
import numpy as np

def fungsi(x):
    return 4*(x**2) + x + 6

def kartesian():
    x = np.linspace(-3,3,100)
    y = 4*(x**2) + x + 6
    
    plt.plot(x,y)
    plt.show()

def trapezcomp(fx, bwh, ats, klm):
    lbr_klm = (ats - bwh) / klm
    x = bwh

    integrasi = fx(bwh)
    for k in range(1, klm):
        x = x + lbr_klm
        integrasi += 2 * fx(x)

    return (integrasi + fx(ats)) * lbr_klm * 0.5

def romberg(fx, bwh, ats, klm):
    kartesian()
    iterasi = np.zeros((klm, klm))

    for k in range(0, klm):
        iterasi[k, 0] = trapezcomp(fx, bwh, ats, 2**k)

        for j in range(0, k):
            iterasi[k, j+1] = (4**(j+1) * iterasi[k, j] - iterasi[k-1, j]) / (4**(j+1) - 1)

        print(iterasi[k, 0:k+1])

    return iterasi

bawah = int(input("Batas bawah: "))
atas = int(input("Batas atas: "))
kolom = int(input("Jumlah kolom: "))

iterasi = romberg(fungsi, bawah, atas, kolom)
hasil = iterasi[kolom-1, kolom-1]
print(hasil)