def edit_data(keys:str):
    
    print('Pilih data yang ingin diedit:')
    print('1. Nama\t\t\t5. Alamat')
    print('2. ID\t\t\t6. Golongan Darah')
    print('3. Tempat Lahir\t\t7. Agama')
    print('4. Tanggal lahir\t8. Status Perkawinan')
    print('(1-8):', end = ' ')
    user_input = int(input())
    print()

    if user_input == 1:
        pass
    elif user_input == 2:
        print('Masukkan data ID karyawan baru:', end = ' ')
        new_id_input = input()
        employee_database[keys]['ID'] = new_id_input
    elif user_input == 3:
        print('Masukkan data tempat lahir karyawan baru:', end = ' ')
        new_birthplace_input = (input().lower()).title()
        employee_database[keys]['Tempat Lahir'] = new_birthplace_input
    elif user_input == 4:
        print('Masukkan data tanggal lahir karyawan baru:', end = ' ')
        new_birthday_input = (input().lower()).title()
        employee_database[keys]['Tanggal Lahir'] = new_birthday_input
    elif user_input == 5:
        print('Masukkan data alamat karyawan baru:', end = ' ')
        new_address_input = (input().lower()).title()
        employee_database[keys]['Alamat'] = new_address_input
    elif user_input == 6:
        print('Masukkan data golongan darah karyawan baru:', end = ' ')
        new_bloodtype_input = (input().lower()).title()
        employee_database[keys]['Golongan Darah'] = new_bloodtype_input
    elif user_input == 7:
        print('Masukkan data agama karyawan baru:', end = ' ')
        new_religion_input = (input().lower()).title()
        employee_database[keys]['Agama'] = new_religion_input
    elif user_input == 8:
        print('Masukkan data status perkawinan karyawan baru:', end = ' ')
        new_marriedstatus_input = (input().lower()).title()
        employee_database[keys]['Status Perkawinan'] = new_marriedstatus_input
    else:
        pass
    print()

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
    print('Input (1/2):', end = ' ')
    user_input=(input())
    print()

    while True:
        if int(user_input) == 1:
            print('Data edit diterima!')
            print('Kembali ke Menu Database')
            print()
            # database_menu_display()
        elif int(user_input) == 2:
            edit_data(keys)
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1-2):', end = ' ')
            user_input=input()

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
        print()
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
            print()
            edit_data(name_input)
        elif user_input == 2:
            print()
            print('Kembali ke Menu Database')
            print()
            # database_menu_display()
        else:
            print()
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
        
show_employee()