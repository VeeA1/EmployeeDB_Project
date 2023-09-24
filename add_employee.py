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
            # main_menu_display()
        elif user_input == '2':
            add_employee()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 - 2):', end = ' ')
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