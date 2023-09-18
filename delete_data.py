def delete_menu():
    print()
    print('Apakah anda ingin menghapus data?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1/2):', end = ' ')
    user_input = int(input())

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
        pass 
    elif  user_input == 2:
        pass 
    elif  user_input == 3:
        pass
    else:
        pass