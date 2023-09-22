def main_menu_display():
    print()
    print('=========================================  Main Menu Database Karyawan  ==========================================')
    print()
    print('1. Tampilkan data seluruh karyawan')
    print('2. Tampilkan data karyawan')
    print('3. Tambah Data Karyawan')
    print('4. Hapus Data Karyawan')
    print('5. Exit')
    print()
    print('Silahkan pilih menu yang ingin di akses(1 - 4):', end=' ')
    user_input=input()
    main_menu(user_input)

def main_menu(i:str):
    '''
    Memilih menu yang diinginkan
    '''
    if i == '1':
        show_database()
    elif i == '2':
        show_employee()
    elif i == '3':
        add_employee()
    elif i == '4':
        delete_menu()
    elif i == '5':
        print('Terima kasih telah mengakses database karyawan')
        print('---------------------------------------------  Have a good day  --------------------------------------------------')
        print()
        quit()
    else:
        print()
        print('Pilihan menu tidak tersedia!')
        print('Mohon pilih ulang menu yang yang tersedia')
        main_menu_display()

def show_database():
    print()
    print('======================================  Data Karyawan Divisi Data Science  =======================================')
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
    main_menu_display()

def show_employee():
    print()
    print('--------------------------------------  Data Karyawan Divisi Data Science  --------------------------------------')
    print()
    print('Masukkan nama karyawan:', end=' ')
    name_input = input().lower()
    name_input = name_input.title()
    print()

    print('--------------------------------------  Data Karyawan Divisi Data Science  --------------------------------------')
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
    print()
    
    print('Apakah anda ingin mengedit data karyawan ?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1 / 2):', end = ' ')
    user_input=input()
    
    while True:
        if user_input == '1':
            print()
            edit_data(name_input)
        elif user_input == '2':
            print()
            print('Kembali ke Main Menu')
            main_menu_display()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 / 2):', end = ' ')
            user_input=input()

def edit_data(keys:str):
    data_copy = {}
    data_copy['{}'.format(keys)] = employee_database[keys].copy()

    print('=========================================  Edit Menu Database Karyawan  ==========================================')
    print()
    print('Pilih data yang ingin diedit:')
    print('1. Nama\t\t\t5. Alamat')
    print('2. ID\t\t\t6. Golongan Darah')
    print('3. Tempat Lahir\t\t7. Agama')
    print('4. Tanggal lahir\t8. Status Perkawinan')
    print('Input (1 - 8):', end = ' ')
    user_input = input()
    print()

    edit_validation = True
    while edit_validation == True:
        if user_input == '1':
            edit_validation = False
            print('Masukkan data nama karyawan baru:', end = ' ')
            new_name_input = (input().lower()).title()
            data_temp = employee_database[keys]
            del employee_database[keys]
            employee_database[new_name_input] = data_temp
        elif user_input == '2':
            edit_validation = False
            print('Masukkan data ID karyawan baru:', end = ' ')
            new_id_input = input()
            employee_database[keys]['ID'] = new_id_input
        elif user_input == '3':
            edit_validation = False
            print('Masukkan data tempat lahir karyawan baru:', end = ' ')
            new_birthplace_input = (input().lower()).title()
            employee_database[keys]['Tempat Lahir'] = new_birthplace_input
        elif user_input == '4':
            edit_validation = False
            print('Masukkan data tanggal lahir karyawan baru:', end = ' ')
            new_birthday_input = (input().lower()).title()
            employee_database[keys]['Tanggal Lahir'] = new_birthday_input
        elif user_input == '5':
            edit_validation = False
            print('Masukkan data alamat karyawan baru:', end = ' ')
            new_address_input = (input().lower()).title()
            employee_database[keys]['Alamat'] = new_address_input
        elif user_input == '6':
            edit_validation = False
            print('Masukkan data golongan darah karyawan baru:', end = ' ')
            new_bloodtype_input = (input().lower()).title()
            employee_database[keys]['Golongan Darah'] = new_bloodtype_input
        elif user_input == '7':
            edit_validation = False
            print('Masukkan data agama karyawan baru:', end = ' ')
            new_religion_input = (input().lower()).title()
            employee_database[keys]['Agama'] = new_religion_input
        elif user_input == '8':
            edit_validation = False
            print('Masukkan data status perkawinan karyawan baru:', end = ' ')
            new_marriedstatus_input = (input().lower()).title()
            employee_database[keys]['Status Perkawinan'] = new_marriedstatus_input
        else:
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 - 8):', end = ' ')
            user_input=input()
        print()

    if user_input == 1:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(new_name_input,
                                                      employee_database[new_name_input]['ID'],
                                                      employee_database[new_name_input]['Tempat Lahir'],                                                   
                                                      employee_database[new_name_input]['Tanggal Lahir'],
                                                      employee_database[new_name_input]['Alamat'],
                                                      employee_database[new_name_input]['Golongan Darah'],
                                                      employee_database[new_name_input]['Agama'],
                                                      employee_database[new_name_input]['Status Perkawinan']
                                                     ))
    elif int(user_input) > 1 and int(user_input) < 8:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(keys,
                                                      employee_database[keys]['ID'],
                                                      employee_database[keys]['Tempat Lahir'],                                                   
                                                      employee_database[keys]['Tanggal Lahir'],
                                                      employee_database[keys]['Alamat'],
                                                      employee_database[keys]['Golongan Darah'],
                                                      employee_database[keys]['Agama'],
                                                      employee_database[keys]['Status Perkawinan']
                                                     ))
    print()

    print('Apakah data edit sudah benar?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1 / 2):', end = ' ')
    user_input=input()
    print()

    while True:
        if user_input == '1':
            print('Data edit diterima!')
            print('Kembali ke Main Menu Database')
            main_menu_display()
        elif user_input == '2':
            employee_database[keys] = data_copy[keys]
            edit_data(keys)
        else:
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 - 2):', end = ' ')
            user_input=input()
            print()

def add_employee():
    print()
    print('=========================================  Add Menu Database Karyawan  ==========================================')
    print()
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
    user_input=input('(1/2): ')

    # input_database = True
    while True:
        if user_input == '1':
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
        elif user_input == '2':
            add_employee()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 - 2):', end = ' ')
            user_input=int(input())
            print()

def delete_menu():
    print()
    print('Apakah anda ingin menghapus data?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1 / 2):', end = ' ')
    user_input = int(input())
    print()

    if user_input > 1:
        print('Perintah hapus dibatalkan')
        print('Kembali ke menu awal')
        main_menu_display()

    print('=================================================  Delete Menu  ==================================================')
    print()
    print('1. Hapus data karyawan')
    print('2. Hapus database')
    print('3. Kembali ke menu awal')
    print()
    print('Silahkan pilih perintah hapus')
    print('Input (1 - 3):', end = ' ')
    user_input = int(input())

    if  user_input == 1:
        delete_data()
    elif  user_input == 2:
        clear_data() 
    elif  user_input == 3:    
        print('Kembali ke menu awal')
        main_menu_display()
    else:
        print()
        print('Perintah tidak ditemukan!')
        print('Perintah delete dibatalkan')
        print('Kembali ke menu awal')
        main_menu_display()

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
            print('Input (1 / 2):', end = ' ')
            user_input = int(input())
            if user_input == 1:
                del employee_database[name_input]
                print('Data karyawan telah dihapus')
                print('Kembali ke menu awal')
                main_menu_display()
            elif user_input == 2:
                print('Perintah penghapusan dibatalkan')
                print('Kembali ke menu awal')
                main_menu_display()
            else:
                print()
                print('Perintah tidak ditemukan!')
                print('Mohon pilih ulang (1/2):', end = ' ')
                user_input=input()
        else:
            print('Data karyawan tidak ditemukan!')
            print('Perintah delete dibatalkan')
            print('Kembali ke menu awal')
            main_menu_display()

def clear_data():
    print()
    print('Apakah anda ingin menghapus seluruh data karyawan?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1 / 2):', end = ' ')
    user_input = int(input())
    print()

    if user_input == 1:
        print('Apakah anda yakin?')
        print('1. Ya')
        print('2. Tidak')
        print('Input (1 / 2):', end = ' ')
        user_input = int(input())
        print()
        
        if user_input == 1:
            employee_database.clear()
            print('Database telah dikosongkan')
            print('Kembali ke menu awal')
            main_menu_display()
        else:
            print('Perintah hapus dibatalkan')
            print('Kembali ke menu awal')
            main_menu_display()
    else:
            print('Perintah hapus dibatalkan')
            print('Kembali ke menu awal')
            main_menu_display()

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