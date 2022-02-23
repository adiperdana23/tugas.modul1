def menu() :
    print('''
     =====DATA PASIEN RUMAH SAKIT=====
    List Menu
    1. Report Data Pasien
    2.Menambahkan Data Pasien
    3.Mengubah Data Pasien
    4.Menghapus Data Pasien
    5.Exit
    ''')


pasien = [
{'No Urut': 1 ,
    'Nama': 'Tonggo',
    'Usia': 40,
    'keluhan' :'Demam', 
    'Dokter': 'dr.Nia'
    }  ,   
    {'No Urut': 2 ,
    'Nama': 'Fredy',
    'Usia': 32,
    'keluhan' :'Pilek', 
    'Dokter': 'dr.Tubagus'
    },
    {'No Urut': 3 ,
    'Nama': 'Rangga',
    'Usia': '35',
    'keluhan' :'Diare', 
    'Dokter': 'dr.Wardoyo'
    }
]
menu ()
option = int(input(" Masukkan nomor menu yang dituju:"))
   


while option != 0 :
    if option == 1 :
        print('Report Data Pasien\n')
        for i , j in enumerate(pasien):
            print(j)
    elif option == 2 :
        Nourut = int (input('masukkan no urut :'))
        NamaPasien = input('masukkan nama pasien :')
        UmurPasien = int(input('masukkan Umur Pasien :'))
        Keluhan  = input('masukkan Keluhan :')
        Namadokter = input('nama dokter :')
        ceklagi = input('\n Apakah kamu yakin buat nambah data ini? (Y/N) : )').upper()
        if ceklagi == 'Y' :
           pasien.append ({
         'No Urut' : Nourut,
         'Nama'    : NamaPasien,
         'Usia'    : UmurPasien,
         'keluhan'  : Keluhan,
         'Dokter'   : Namadokter
         }) 
           print ('\n--- data  berhasil ditambahkan---')
        elif ceklagi == 'N' :
            print ('\n--- data tidak ditambahkan---')
        print('Report Data Pasien\n')
        for i , j in enumerate(pasien):
            print(j) 
        break
    elif option == 3 :
        updateNamaPasien = input('masukkan nama pasien baru :')
        updateUmurPasien = int(input('masukkan  umur pasienbaru :'))
        updateKeluhan  = input('masukkan Keluhan baru :')
        updateNamadokter = input('nama dokter baru:')
        pasien[
        'Nama'    : updateNamaPasien ,
        'Usia'    : updateUmurPasien,
        'keluhan'  : updateKeluhan,
        'Dokter'   : updateNamadokter  
        ]
        print('Daftar nama pasien\n')
        for i ,j in enumerate(pasien):
            print(j)
        break
    elif option == 4:
        print('Daftar Data Pasien\n')
        for i , j in enumerate(pasien):
            print(j)
        Nourutygdihapus = int (input('masukkan no urut pasien yang ingin dihapus :'))
        del pasien[Nourutygdihapus]
        print('Daftar Data Pasien\n')
        for i ,j in enumerate(pasien):
            print(j)
        break
    else :
        print('====MENU TIDAK TERDAFTAR=======') 
        break
print(' Terima kasih telah menggunakan menu ini')       
  