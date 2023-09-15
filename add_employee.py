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
print()

# print('Apakah anda ingin menambah data karyawan?')
# print('1. Ya')
# print('2. Tidak')
# print('Input (1-2):', end = ' ')

print('Masukkan data nama karyawan baru:', end = ' ')
new_name_input = (input().lower()).title()
print('Masukkan data ID karyawan baru:', end = ' ')
new_id_input = (input().lower()).title()
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

employee_database.update({new_name_input :{'ID' : new_id_input,
                                            'Tempat Lahir' : new_birthplace_input,
                                            'Tanggal Lahir' : new_birthday_input,
                                            'Alamat' : new_address_input,
                                            'Golongan Darah' : new_bloodtype_input,
                                            'Agama' : new_religion_input,
                                            'Status Perkawinan' : new_marriedstatus_input}
                                            })

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