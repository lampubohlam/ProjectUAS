# ProjectUAS
![Screenshot (225)](https://user-images.githubusercontent.com/116137169/211908755-d907d578-9b88-465e-8c7a-79a6acab602e.png)
> buka aplikasi phycharm dan buat project terlebih dahulu seperti gambar berikut
  
  
  ![Screenshot (226)](https://user-images.githubusercontent.com/116137169/211909508-57106895-a521-47e1-ad33-09434c9b036f.png)

> lalu klik kanan dan pilih new pada project kalian dan buat package seperti gambar berikut
  
  
  ![Screenshot (227)](https://user-images.githubusercontent.com/116137169/211910364-697c0e5b-98b4-4cd2-ae0b-f8e2effd2350.png)


> buat python package dengan nama "MODEL"

> lalu pada package klik kanan dan new pilih python file dan masukan daftar_nilai seperti gambar berikut

 
 ![Screenshot (228)](https://user-images.githubusercontent.com/116137169/211911328-b93a6b01-dbaf-4beb-8d87-98fd331d7f4f.png)

> setelah itu bualah package lagi dengan nama view_nilai untuk hasil tabel yang akan ditampilkan
  
  
  ![Screenshot (229)](https://user-images.githubusercontent.com/116137169/211912022-2adc3a47-05ba-42f0-875a-f8220eb811bb.png)

> masukan codingan seperti berikut


![image](https://user-images.githubusercontent.com/116137169/211912542-af1f9ac3-362f-43b8-a36e-729a136c9e95.png)

# penjelasan daftar_nilai

1) pertama deklarasikan dulu menggunakan class daftar nilai untuk memasukan tambah data menggunakan fungsi "Def" dengan ketentuan data[tambah_nama] = tambah_nim, tambah_tugas, tambah_uts, tambah_uas, tambah_akhir

2) Gunanya untuk mengubah data mahasiswa dari nama mahasiswa itu sendiri dan, menggunakan logika "if ubah_nama in data.keys():" bertujuan untuk mengubah  data dengan memasukan inputan baru
 
3) (Jika)Jika mahasiswa tersebut ada maka data mahasiswa tersebut akan di ubah
(Else) Jika nama mahasiswa tersebut tidak ada maka datanya tidak akan ditemukan

> kemudian masuk ke package view dan masuk ke input nilai dengan menggunakan fungsi "Def" juga seperti gambar berikut
  
  ![Screenshot (231)](https://user-images.githubusercontent.com/116137169/211917365-eccc4ade-2f4e-43a1-867c-67d98783db79.png)

# penjelasan input_nilai

1) pertama masukan fyngsi "Def" dengan mamasukan inputan Nama, Nim, tugas, uts, uas, akhir
2) gunakan pada keterengan penjelasan dengan memasukan "\t" ini berfungsi untuk memasukan pada Tab berikut ketentuan rumusnnya :
   ![Screenshot (232)](https://user-images.githubusercontent.com/116137169/211918493-09007e65-2e8a-47ac-9e02-64fbc715486e.png)
3) pada setiap tahap data input masukan fungsi return agar tidak terjadi error pada program

> lalu masuk ketahap selanjutnya yaitu view_nilai yang berfungsi untuk menampilkan hasil inputan berupa tabel

  ![Screenshot (233)](https://user-images.githubusercontent.com/116137169/211920087-3d705840-eaef-481a-988c-6c93cc66a214.png)
![Screenshot (234)](https://user-images.githubusercontent.com/116137169/211920348-cfe80ea9-5d75-453c-a014-15979b1e6acb.png)

# Penjelasan view_nilai

Fungsinya sama saja dengan yang ada dibagian Input_Nilai

1) Disini tabel untuk menampilkan data - data dan nama - nama mahasiswa didalam (Jika)Jika terdapat data maka data dan nama mahasiswa tersebut akan muncul

2) lalu gunakan for untuk melakukan perulangan nomor urut(Else)Jika kita belum menginputkan data sama sekali maka akan muncul tulisan "tidak ada data" Def mencari data

>langkah selanjutnya masuk ke python file main.py disini berfungsi untuk melakukan run dari file-file diatas menjadi 1 berikut gambarnya  
![Screenshot (235)](https://user-images.githubusercontent.com/116137169/211922114-81a15fa8-e1e3-4bd0-8cb2-6947fee85f4d.png)


# penjelasan main
1) gunakan print untuk membuat pilihan menunya lalu buat inputan untuk memilih menu nanti ketika program dijalankan
2) gunakan fungsi "If dan Elif" karena akan membuat cabang pilihan yang banyak
3) dibawahnya tambahkan fungsi - fungsi yang sudah dibuat tadi
4) Pada perintah terakhir gunakan fungsi "break" untuk keluar dari program yang di jalankan
(Else)Jika tidak memilih salah satu menu tersebut maka akan muncul peringatan "pilih menu yang tersedia diatas"

3) sama seperti diatas tadi pada print Input_Nilai dengan membuat inputan dengan format nama untuk mencari data dari mahasiswa yang sedang kita cari

4) (If)Jika data mahasiswa yang dicari ada didalam hasil innput maka data baik Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS akan muncul
(Else)Jika data mahasiswa yang dicari tidak ada didalam kamus maka akan muncul tulisan "datanya tidak ada"

# hasil run

![Screenshot (236)](https://user-images.githubusercontent.com/116137169/211924887-8bcb0210-7915-4104-bde5-ad9f5c526a5f.png)
![Screenshot (237)](https://user-images.githubusercontent.com/116137169/211924900-feb8f236-7e96-47f5-9dc9-012eca8069cc.png)
![Screenshot (238)](https://user-images.githubusercontent.com/116137169/211924922-a6c5aff8-1356-4883-a181-b041bee1dc5e.png)
![Screenshot (239)](https://user-images.githubusercontent.com/116137169/211924953-76654f2a-d89a-48c7-9f01-1c4c55340cd2.png)



