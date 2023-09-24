def show_database():
    print()
    print('======================================  Data Karyawan Divisi Data Science  =======================================')
    print()
    
    global employee_database
    employee_database = dict(sorted(employee_database.items()))
    
    for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))
    # main_menu_display()

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
            pass
            # edit_data(name_input)
        elif user_input == '2':
            print()
            print('Kembali ke Main Menu')
            pass
            # main_menu_display()
        else:
            print()
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1 / 2):', end = ' ')
            user_input=input()