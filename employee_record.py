def database_menu_display():
    print()
    print('=============  Database Karyawan  =============')
    print()
    print('1. Tampilkan data seluruh karyawan')
    print('2. Tampilkan data karyawan')
    print('3. Kembali ke menu utama')
    print()
    print('Silahkan pilih menu yang ingin di akses (1-3):', end=' ')
    user_input = int(input())
    database_menu(user_input)

def database_menu(i:int):
    '''
    Memilih menu yang diinginkan
    '''
    if i == 1:
        show_database()
    elif i == 2:
        show_employee()
    elif i == 3:
        print('Kembali ke Menu Utama')
        print()
        # main_menu_display()
    else:
        print('Pilihan menu tidak tersedia')
        print('Mohon pilih ulang menu yang yang tersedia')
        print()
        database_menu_display()

def show_database():
    print()
    for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],
                                               employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))
    print()

def show_employee():
    print()
    print('Masukkan nama lengkap karyawan:', end=' ')
    name_input = input().lower()
    name_input = name_input.title()
    print()

    if name_input in employee_database.keys():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(name_input,
                                                      employee_database[name_input]['ID'],
                                                      employee_database[name_input]['Tempat Lahir'],                                                   
                                                      employee_database[name_input]['Tanggal Lahir'],
                                                      employee_database[name_input]['Alamat'],
                                                      employee_database[name_input]['Golongan Darah'],
                                                      employee_database[name_input]['Agama'],
                                                      employee_database[name_input]['Status Perkawinan']
                                                      ))
    else:
        print('Data karyawan tidak ditemukan!')
        print('Masukkan ulang nama karyawan')
        print()
        show_employee()
    
    print('Apakah anda ingin mengedit data karyawan?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1/2):', end = ' ')
    user_input=int(input())
    
    edit_database = True
    while edit_database == True:
        if user_input == 1:
            pass
        elif user_input == 2:
            print('Kembali ke Menu Database')
            database_menu_display()
        else:
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1-2):', end = ' ')
            user_input=int(input())


employee_database={
    'Viky':{
        'ID' : 'DS150798',
        'Tempat Lahir' : 'Surabaya',
        'Tanggal Lahir' : '15 Juli 1998',
        'Alamat' : 'Gayungsari Barat 2 no. 23',
        'Golongan Darah' : 'A',
        'Agama' : 'Islam',
        'Status Perkawinan' : 'Belum Kawin'
        },
    'Aldo':{
        'ID' : 'DS081097',
        'Tempat Lahir' : 'Surabaya',
        'Tanggal Lahir' : '8 Oktober 1997',
        'Alamat' : 'Kebonagung Blok 2A no. 14',
        'Golongan Darah' : 'B',
        'Agama' : 'Islam',
        'Status Perkawinan' : 'Belum Kawin'
        }
}

database_menu_display()