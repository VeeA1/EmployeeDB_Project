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
            # main_menu_display()
        elif user_input == '2':
            employee_database[keys] = data_copy[keys]
            edit_data(keys)
        else:
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 - 2):', end = ' ')
            user_input=input()
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