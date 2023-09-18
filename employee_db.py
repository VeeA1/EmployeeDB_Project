def main_menu_display():
    print()
    print('=============  Data Karyawan Divisi Data Science  =============')
    print()
    print('1. List Daftar Karyawan')
    print('2. Menambahkan Data Karyawan Baru')
    print('3. Mengubah Data Karyawan')
    print('4. Menghapus Data Karyawan')
    print('5. Exit')
    print()
    print('Silahkan pilih menu yang ingin di akses(1 - 5):', end=' ')
    user_input=int(input())
    print()
    main_menu(user_input)

def main_menu(i:int):
    '''
    Memilih menu yang diinginkan
    '''
    if i == 1:
        database_menu_display()
    elif i == 2:
        add_employee()
    elif i == 3:
        pass
    elif i == 4:
        pass
    elif i == 5:
        print('Terima kasih telah mengakses daftar karyawan')
        print('-----------  Have a good day  --------------')
        print()
        quit()
    else:
        print('Pilihan menu yang dipilih tidak tersedia')
        print('Mohon pilih ulang menu yang yang tersedia')
        main_menu_display()

def database_menu_display():
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
        main_menu_display()
    else:
        print()
        print('Pilihan menu tidak tersedia')
        print('Mohon pilih ulang menu yang yang tersedia')
        print()
        database_menu_display()

def show_database():
    print()
    for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))
    print()
    database_menu_display()

def show_employee():
    print()
    print('Masukkan nama karyawan:', end=' ')
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
        show_employee()
    
    print('Apakah anda ingin mengedit data karyawan?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1/2):', end = ' ')
    user_input=int(input())
    
    while True:
        if user_input == 1:
            pass
        elif user_input == 2:
            print()
            print('Kembali ke Menu Database')
            print()
            database_menu_display()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1-2):', end = ' ')
            user_input=int(input())

def add_employee():

    print('Masukkan data nama karyawan baru:', end = ' ')
    new_name_input = (input().lower()).title()
    print('Masukkan data ID karyawan baru:', end = ' ')
    new_id_input = input()
    print('Masukkan data tempat lahir karyawan baru:', end = ' ')
    new_birthplace_input = (input().lower()).title()
    print('Masukkan data tanggal lahir karyawan baru:', end = ' ')
    new_birthday_input = (input().lower()).title()
    print('Masukkan data alamat karyawan baru:', end = ' ')
    new_address_input = (input().lower()).title()
    print('Masukkan data golongan darah karyawan baru:', end = ' ')
    new_bloodtype_input = (input().lower()).title()
    print('Masukkan data agama karyawan baru:', end = ' ')
    new_religion_input = (input().lower()).title()
    print('Masukkan data status perkawinan karyawan baru:', end = ' ')
    new_marriedstatus_input = (input().lower()).title()
    print()

    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(new_name_input, 
                                            new_id_input,
                                            new_birthplace_input,
                                            new_birthday_input,
                                            new_address_input,
                                            new_bloodtype_input,
                                            new_religion_input,
                                            new_marriedstatus_input
                                            ))

    print()
    print('Apakah data karyawan yang diinput sudah benar?')
    print('1. Ya')
    print('2. Tidak')
    user_input=int(input(('(1/2): ')))

    # input_database = True
    while True:
        if user_input == 1:
            employee_database.update({new_name_input :{'ID' : new_id_input,
                                                        'Tempat Lahir' : new_birthplace_input,
                                                        'Tanggal Lahir' : new_birthday_input,
                                                        'Alamat' : new_address_input,
                                                        'Golongan Darah' : new_bloodtype_input,
                                                        'Agama' : new_religion_input,
                                                        'Status Perkawinan' : new_marriedstatus_input}
                                                        })
            # input_database = False
            print('Data karyawan baru telah diterima')
            main_menu_display()
        elif user_input == 2:
            print()
            add_employee()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1-2):', end = ' ')
            user_input=int(input())
            print()

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

main_menu_display()