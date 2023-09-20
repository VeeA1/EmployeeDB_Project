def delete_menu():
    print()
    print('Apakah anda ingin menghapus data?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1/2):', end = ' ')
    user_input = int(input())
    print()

    if user_input > 1:
        print('Perintah hapus dibatalkan')
        print('Kembali ke menu awal')
        # main_menu_display()

    print('=============  Delete Menu  =============')
    print('1. Hapus data karyawan')
    print('2. Hapus database')
    print('3. Kembali ke menu awal')
    print('Silahkan pilih perintah hapus')
    print('Input (1-3):', end = ' ')
    user_input = int(input())

    if  user_input == 1:
        delete_data()
    elif  user_input == 2:
        clear_data() 
    elif  user_input == 3:    
        print('Kembali ke menu awal')
        # main_menu_display()
    else:
        print('Perintah tidak ditemukan!')
        print('Perintah delete dibatalkan')
        print('Kembali ke menu awal')
        # main_menu_display()

def delete_data():
        print()
        print('Masukkan nama lengkap karyawan:', end = ' ')
        name_input = (input().lower()).title()

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
            print()
            print('Apakah anda ingin menghapus data karyawan " {} "'.format(name_input))
            print('1. Ya')
            print('2. Tidak')
            print('Input (1/2):', end = ' ')
            user_input = int(input())

            if user_input == 1:
                del employee_database[name_input]
                print('Data karyawan telah dihapus')
                print('Kembali ke menu awal')
                # main_menu_display()
            elif user_input == 2:
                print('Perintah penghapusan dibatalkan')
                print('Kembali ke menu awal')
                # main_menu_display()
            else:
                print()
                print('Perintah tidak ditemukan!')
                print('Mohon pilih ulang (1/2):', end = ' ')
                user_input=input()

        else:
            print('Data karyawan tidak ditemukan!')
            print('Perintah delete dibatalkan')
            print('Kembali ke menu awal')
            # main_menu_display()

def clear_data():
    print()
    print('Apakah anda ingin menghapus seluruh data karyawan?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1/2):', end = ' ')
    user_input = int(input())
    print()

    if user_input == 1:
        print('Apakah anda yakin?')
        print('1. Ya')
        print('2. Tidak')
        print('Input (1/2):', end = ' ')
        user_input = int(input())
        print()
        
        if user_input == 1:
            employee_database.clear()
            print('Database telah dikosongkan')
            print('Kembali ke menu awal')
            # main_menu_display()
        else:
            print('Perintah hapus dibatalkan')
            print('Kembali ke menu awal')
            # main_menu_display()
    else:
            print('Perintah hapus dibatalkan')
            print('Kembali ke menu awal')
            # main_menu_display()
    
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

for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))
delete_menu()

for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))