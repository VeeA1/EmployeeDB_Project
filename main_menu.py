def main_menu_display():
    '''
    For displaying main menu of the program so the user can choose which 
    task that user need to do
    '''
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
    for choosing which menu that user want
    '''
    if i == '1':
        pass
        # show_database()
    elif i == '2':
        pass
        # show_employee()
    elif i == '3':
        pass
        # add_employee()
    elif i == '4':
        pass
        # delete_menu()
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