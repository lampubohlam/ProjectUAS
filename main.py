from model.daftar_nilai import daftarnilai
from view.view_nilai import mencari
while True:
    b = daftarnilai()
    c = mencari()
    print('tambah\t(t)\nubah\t(u)\ncari\t(c)\nhapus\t(h)\nlihat\t(l)')
    a = input('Masukkan pilihan > ')
    if (a=="t"):
        b.tambah_data()
    elif (a=="u"):
        b.ubah_data()
    elif (a=="c"):
        c.cetak_hasil_pencarian()
    elif (a=="h"):
        b.hapus_data()
    elif (a=="l"):
        c.cetak_daftar_nilai()
    else :
        keluar()
        break