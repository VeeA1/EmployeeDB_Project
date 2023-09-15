def main_menu(i:int):
    '''
    Memilih menu yang diinginkan
    '''
    if i == 1:
        pass
    elif i == 2:
        pass
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

def main_menu_display():
    print()
    print('=============  Data Karyawan Divisi Data Science  =============')
    print()
    print('1. List Daftar Karyawan')
    print('2. Menambahkan Data Karyawan')
    print('3. Mengubah Data Karyawan')
    print('4. Menghapus Data Karyawan')
    print('5. Exit')
    print()
    print('Silahkan pilih menu yang ingin di akses(1 - 5):', end=' ')
    user_input=int(input())
    print()
    main_menu(user_input)

# main_menu(user_input)
main_menu_display()