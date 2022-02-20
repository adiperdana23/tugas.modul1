# menu utama
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
cart = []
   


while True :
    pilihanMenu = input ('''
    =====DATA PASIEN RUMAH SAKIT=====
    List Menu
    1. Report Data Pasien
    2.Menambahkan Data Pasien
    3.Mengubah Data Pasien
    4.Menghapus Data Pasien
    5.Exit
    Masukkan Angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        print('Report Data Pasien\n')
        print('No Urut \t|Nama \t|Usia\t|keluhan\t|Dokter\t')
        for i in range(len(pasien)) :
            print ('{} \t|{}\t|{}\t|{}\t|{}\t'.format(pasien[i]['No Urut'],pasien[i]['Nama'],pasien[i]['Usia'],pasien[i]['keluhan'],pasien[i]['Dokter']))
    elif (pilihanMenu == '2') :
        Nourut = int (input('masukkan no urut :'))
        NamaPasien = input('masukkan nama pasien :')
        UmurPasien = int(input('masukkan Umur Pasien :'))
        Keluhan  = input('masukkan Keluhan :')
        Namadokter = input('nama dokter :')
        pasien.append ({
        'No Urut' : Nourut,
        'Nama'    : NamaPasien,
        'Usia'    : UmurPasien,
        'keluhan'  : Keluhan,
        'Dokter'   : Namadokter
        })
        print('Report Data Pasien\n')
        print('No Urut \t|Nama \t|Usia\t|keluhan\t|Dokter\t')
        for i in range(len(pasien)) :
            print ('{} \t|{}\t|{}\t|{}\t|{}\t'.format(pasien[i]['No Urut'],pasien[i]['Nama'],pasien[i]['Usia'],pasien[i]['keluhan'],pasien[i]['Dokter']))
    elif (pilihanMenu == '4') :
        print('Daftar Data Pasien\n')
        print('No Urut \t|Nama \t|Usia\t|keluhan\t|Dokter\t')
        for i in range(len(pasien)) :
            print ('{} \t|{}\t|{}\t|{}\t|{}\t'.format(pasien[i]['No Urut'],pasien[i]['Nama'],pasien[i]['Usia'],pasien[i]['keluhan'],pasien[i]['Dokter']))
        Nourutygdihapus = int (input('masukkan no urut pasien yang ingin dihapus :'))
        del pasien[Nourutygdihapus]
        print('Daftar Data Pasien\n')
        print('No Urut \t|Nama \t|Usia\t|keluhan\t|Dokter\t')
        for i in range(len(pasien)) :
            print ('{} \t|{}\t|{}\t|{}\t|{}\t'.format(pasien[i]['No Urut'],pasien[i]['Nama'],pasien[i]['Usia'],pasien[i]['keluhan'],pasien[i]['Dokter']))
    else :
        print('====MENU TIDAK TERDAFTAR=======')  
        
  