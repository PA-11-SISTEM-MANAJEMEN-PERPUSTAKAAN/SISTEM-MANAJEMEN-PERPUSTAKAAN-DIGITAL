import json
import os
from prettytable import PrettyTable
import time
from datetime import date
from pwinput import pwinput

data_buku = "Data_Buku.json"
data_user = "Data_user.json"
data_barang = "Data_Barang.json"  

def registrasi ():
    with open(data_user, "r") as f :
        user = json.load(f)
    while True:
        try: 
            input_username = input("Buat username anda: ")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")
        if input_username not in user[0]:
            if input_username.isalnum():
                try:
                    input_password = pwinput("Buat Password (contoh : 1234): ","*")
                except EOFError:
                    print(" Jgn Klik CTRL+Z ")
                except KeyboardInterrupt:
                        print(" Jgn Klik CTRL+C ")
                user[0][input_username] = {"password": input_password, "role": "user", "poin" : 0, "pinjam" : []}
                print(f"Registrasi Berhasil sebagai {input_username}, Mohon Tunggu...")

                with open(data_user, 'w') as f:
                    json.dump(user, f, indent=4)
                time.sleep(3)
                break
            else:
                print("simbol dan spasi tidak di perbolehkan, Mohon Tunggu...")
                time.sleep(2)
        else:
            print("Username tidak tersedia (sudah terpakai), Mohon Tunggu...")
            time.sleep(2)

def login ():
    with open(data_user, "r") as f :
        user = json.load(f)
        dic_user = user[0]

    kesempatan = 3
    while kesempatan > 0 :
        os.system('cls')

        try:
            input_username = input("Masukkan username anda: ")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")

        try:
            input_password = pwinput("Masukkan password anda (contoh : 1234): ","*")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")

        if input_username in dic_user and dic_user[input_username]["password"] == input_password: 
            os.system('cls')
            print(f"anda berhasil login sebagai {input_username}, LOADING... ")
            time.sleep(2)
            return input_username
            
        else : 
            kesempatan -= 1
            print(f"Login Gagal, silahkan input username dan password lagi")
            print("Mohon Tunggu...")
            time.sleep(3)
            if kesempatan == 0 :
                print("Kesempatan Anda Habis, Login Gagal") 
                exit()


def tambah():
    with open(data_buku, "r") as f:
        buku = json.load(f)
        dic_buku = buku[0]

    #Input Judul
    while True:
        try:
            tambah_judul = input("Ketikkan Judul Buku : ")
            if tambah_judul not in dic_buku :
                if "".join(tambah_judul.split()).isalpha():
                    break
                else:
                    print("Inputan tidak boleh mengandung simbol")
            else : 
                print(f"Buku '{tambah_judul}' sudah ada di dalam database")

        except EOFError:
            print("Jgn Klik CTRL+Z")
            continue
        except KeyboardInterrupt:
            print("Jgn Klik CTRL+C")
            return
    
    #Input Genre
    while True:
        try:
            tambah_genre = input("Genre (contoh: aksi): ")
            if tambah_genre == "" :
                print("Genre tidak boleh kosong")
                if tambah_genre.isalpha():
                    break
                else:
                    print("Genre hanya boleh berupa huruf")
                    continue
            else: 
                break
        except EOFError:
            print("Jgn Klik CTRL+Z")
            continue
        except KeyboardInterrupt:
            print("Jgn Klik CTRL+C")
            return
    
    #Input Tahun terbit
    while True:
        try:
            tambah_terbit = input("Tahun Terbit (contoh: 2004): ")
                
            tahun = int(tambah_terbit)
            if tahun < 1000 or tahun > 2025:
                print("Tolong masukkan tahun terbit yang valid")
            break
        except ValueError:
            print("Tahun terbit hanya boleh berupa angka")
        except EOFError:
            print("Jgn Klik CTRL+Z")
            continue
        except KeyboardInterrupt:
            print("\nJgn Klik CTRL+C")
            return
    
    # Input Jumlah Buku
    while True:
        try:
            jumlah_buku = int(input("Jumlah Buku (contoh: 10): "))
            if jumlah_buku > 0:
                break
            else:
                print("Jumlah yang di input harus lebih dari 0")
                continue
        except ValueError:
            print("Inputan harus berupa angka")
            continue
        except EOFError:
            print("Jgn Klik CTRL+Z")
            continue
        except KeyboardInterrupt:
            print("Jgn Klik CTRL+C")
            return
    print(f"Buku Berjudul {tambah_judul} berhasil di tambah kedalam database")
            

    dic_buku[tambah_judul] = {"genre": tambah_genre, "terbit": tambah_terbit, "jumlah": jumlah_buku, "jumlah_fix": jumlah_buku}

    with open(data_buku, 'w') as f:
        json.dump(buku, f, indent=4)
        
    print(f"{tambah_judul} berhasil di tambah ke database!")

def hapus():
    daftar_buku()
    with open(data_buku, "r") as f:
        buku = json.load(f)
    dic_buku = buku[0]   
    daftar_judul = list(dic_buku.keys())

    try:
        hapus_buku = int(input("Judul Buku yang ingin dihapus : "))
    except ValueError:
        print("Input harus berupa Angka")
    except EOFError:
        print(" Jgn Klik CTRL+Z ")
    except KeyboardInterrupt:
        print(" Jgn Klik CTRL+C ")

    if hapus_buku < 1 or hapus_buku > len(daftar_judul):
            print(" Nomor tidak valid!")
    else:
        hapus_buku = daftar_judul[hapus_buku - 1]

        del dic_buku[hapus_buku]

        with open(data_buku, 'w') as f:
            json.dump(buku, f, indent=4)

def edit():
    while True:
        daftar_buku()
        with open(data_buku, "r") as f:
            buku = json.load(f)
        dic_buku = buku[0]      
        daftar_judul = list(dic_buku.keys())
        
        try:
            nomor_buku = int(input("Pilih nomor buku yang akan di edit (0 untuk kembali): "))
        except ValueError:
            print("perintah harus berupa angka")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")
        
        if nomor_buku == 0:
            print("Kembali ke Menu Admin, LOADING...")
            time.sleep(2)
            break
        
        elif nomor_buku <= -1 or nomor_buku > len(daftar_judul):
            print(" Nomor tidak valid!")
            break
        
        else:
            buku_lama = daftar_judul[nomor_buku - 1]
            print(f"Buku yang dipilih: {buku_lama}")

            # Menu edit
            print("+=== MENU EDIT ===+")
            print("| 1. Judul        |")
            print("| 2. Genre        |")
            print("| 3. Tahun Terbit |")
            print("| 4. Jumlah Buku  |")
            print("| 5. Kembali      |")
            print("+=================+")

            try:
                pilihan = input("\nApa yang ingin di edit?: ")
            
                if pilihan == "1":
                    buku_baru = input("Ketikan judul buku baru: ")
                    if buku_baru.isalnum():
                        dic_buku[buku_baru] = dic_buku.pop(buku_lama)
                        print(f" Judul buku berhasil diubah menjadi '{buku_baru}'")
                    else:
                        print("Simbol tidak diperbolehkan")
                
                elif pilihan == "2":
                    try:
                        genre_baru = input("Ketikan genre baru: ")
                        if genre_baru.isalnum():
                            dic_buku[buku_lama].update({"genre": genre_baru})
                            print(f" Genre buku '{buku_lama}' berhasil diubah menjadi '{genre_baru}'")
                        else:
                            print("Simbol tidak diperbolehkan")
                    except ValueError:
                        print(" Input harus berupa Angka ")
                    except EOFError:
                        print(" Jgn Klik CTRL+Z ")
                    except KeyboardInterrupt:
                        print(" Jgn Klik CTRL+C ")

                elif pilihan == "3":
                    try:
                        terbit_baru = input("Ketikan tahun terbit baru: ")
                        if terbit_baru.isdigit() and len(terbit_baru) == 4:
                            dic_buku[buku_lama].update({"terbit": terbit_baru})
                            print(f" Tahun terbit buku '{buku_lama}' berhasil diubah menjadi '{terbit_baru}'")
                        else:
                            print(" Tahun harus berupa 4 digit angka (contoh: 2025)")
                    except ValueError:
                        print("Tahun harus berupa 4 digit angka (contoh: 2025)")
                    except EOFError:
                        print(" Jgn Klik CTRL+Z ")
                    except KeyboardInterrupt:
                        print(" Jgn Klik CTRL+C ")

                elif pilihan == "4":
                    try :
                        jumlah_baru = int(input("Ketikan jumlah buku yang ingin di tambah (beri tanda '-' jika ingin mengurangi): "))
                        if jumlah_baru != 0:
                            jumlah_lama = dic_buku[buku_lama]["jumlah"]
                            jumlah_lama_fix = dic_buku[buku_lama]["jumlah_fix"]

                            total_jumlah = jumlah_lama + jumlah_baru 
                            total_jumlah_fix = jumlah_lama_fix + jumlah_baru
                            
                            dic_buku[buku_lama].update({"jumlah": total_jumlah})
                            dic_buku[buku_lama].update({"jumlah_fix": total_jumlah_fix})
                            
                            print(f" Jumlah buku '{buku_lama}' berhasil diubah. Jumlah sekarang: {total_jumlah}")
                        else:
                            print(" Jumlah yang di input tidak valid")
                    except ValueError:
                        print(" Input harus berupa Angka ")
                    except EOFError:
                        print(" Jgn Klik CTRL+Z ")
                    except KeyboardInterrupt:
                        print(" Jgn Klik CTRL+C ")
                        
                elif pilihan == "5":
                    print("Edit dibatalkan")
                    continue
                else:
                    print(" Perintah tidak valid")
                    continue
            except EOFError:
                print(" Jgn Klik CTRL+Z ")
            except KeyboardInterrupt:
                print(" Jgn Klik CTRL+C ")
            
            with open(data_buku, "w") as f:
                json.dump(buku, f, indent=4)

def daftar_buku():
    os.system('cls')
    with open(data_buku, "r") as f:
        buku = json.load(f)
    dic_buku = buku[0]
    print("="*61)
    print("                      DAFTAR BUKU")
    table = PrettyTable()
    table.field_names = ["No", "Judul", "Genre", "Tahun Terbit", "Jumlah"]

    i = 1
    for judul, info in dic_buku.items():
        table.add_row([i,judul,info["genre"],info["terbit"],info["jumlah"]])
        i += 1
    print(table)

def daftar_anggota():
    os.system('cls')
    with open(data_user, "r") as f:
        user = json.load(f)
    dic_user = user[0]

    table = PrettyTable()
    table.field_names = ["No", "Username", "Role","Poin"]

    i = 1
    for username, keterangan in dic_user.items() :
        table.add_row([i,username,keterangan["role"],keterangan["poin"]])
        i += 1
    print(table)

def tambah_barang():
    while True:
        with open(data_barang, 'r') as f:
            barang = json.load(f)
            dic_barang = barang[0]

            try:
                barang_baru = input("Nama barang : ")
                jumlah_barang = int(input("Jumlah barang : "))
                harga_barang = int(input("Harga penukaran Poin : "))
            except ValueError :
                ("Tolong Masukkan angka")
            except EOFError:
                print(" Jgn Klik CTRL+Z ")
            except KeyboardInterrupt:
                print(" Jgn Klik CTRL+C ")

            dic_barang[barang_baru] = {"jumlah": jumlah_barang, "poin": harga_barang }
            print(f"{barang_baru} sejumlah {jumlah_barang} berhasil ditambahkan")

        with open(data_barang, 'w') as f:
            json.dump(barang, f, indent=4)
        break

def menu_admin ():
    os.system('cls')
    while True :
        tabel = PrettyTable()       

        print("="*100)
        print("                                            MENU ADMIN")
        tabel.field_names = ["No","Fitur","Keterangan"]
        tabel.add_row(["1","Tambah Buku","Menambahkan buku baru ke daftar buku perpustakan"])
        tabel.add_row(["2","Hapus Buku","Menghapus buku dari daftar buku perpustakaan"])
        tabel.add_row(["3","Edit buku","Mengedit informasi buku"])
        tabel.add_row(["4","Daftar Buku","Melihat daftar buku"])
        tabel.add_row(["5","Lihat Anggota Perpustakaan","Melihat daftar anggota yang telah registrasi pada perpustakaan"])
        tabel.add_row(["6","Tambah Barang","Tambah Merchandise Perpustakaan"])
        tabel.add_row(["7","Keluar","Keluar dari program dan log out dari akun admin"])
        print(tabel)
        
        try:
            perintah = input("Pilih Perintah : ")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")

        if perintah == "1":
            tambah()
        elif perintah == "2":
            hapus()
        elif perintah == "3":
            edit()
        elif perintah == "4":
            daftar_buku()
        elif perintah == "5":
            daftar_anggota()
        elif perintah == "6":
            tambah_barang()
        elif perintah == "7":
            print("Log Out dari akun Admin")
            print("LOADING...")
            time.sleep(3)
            break
        else:
            print("Perintah tidak Valid, Mohon Tunggu...")
            time.sleep(1)

def pinjam (username):
    daftar_buku()
    with open(data_buku, "r") as f:
        buku = json.load(f)
    with open(data_user, "r") as f:
        user = json.load(f)
    
    dic_user = user[0]
    dic_buku = buku[0]

    daftar_judul = list(dic_buku.keys())

    try:
        nomor_buku = int(input("Nomor Buku yang ingin dipinjam (0 untuk kembali): "))
    except ValueError:
        print("Input harus berupa Angka")
    except EOFError:
        print(" Jgn Klik CTRL+Z ")
    except KeyboardInterrupt:
        print(" Jgn Klik CTRL+C ")
    
    if nomor_buku == 0:
        print("Kembali ke Menu Users, LOADING...")
        time.sleep(2)
    
    elif nomor_buku < 1 or nomor_buku > len(daftar_judul):
        print(" Nomor tidak valid!")

    else:
        pinjam_buku = daftar_judul[nomor_buku - 1]
        if dic_buku[pinjam_buku]["jumlah"] > 0 :
            dic_buku[pinjam_buku]["jumlah"] -= 1
            dic_user[username]["pinjam"].append(pinjam_buku)
            print(f" Buku Berjudul {pinjam_buku} berhasil di pinjam")
            print(f" Mendapat Bonus +10 Poin ")    
            dic_user[username]["poin"] += 10

            with open(data_buku, "w") as f:
                json.dump(buku, f, indent=4)
            with open(data_user, "w") as f:
                json.dump(user, f, indent=4)
        else: 
            print(" Stok Buku Habis")

def kembalikan (username) :
    with open(data_buku, "r") as f:
        buku = json.load(f)
    with open(data_user, "r") as f:
        user = json.load(f)

    dic_user = user[0]
    dic_buku = buku[0]
    daftar_buku = dic_user[username]["pinjam"]

    print("                      DAFTAR BUKU YANG DIPINJAM")
    table = PrettyTable()
    table.field_names = ["No", "Judul"]

    i = 1
    for judul in daftar_buku:
        table.add_row([i,judul])
        i += 1
    print(table)
    
    try:
        nomor_buku = int(input("Nomor Buku yang ingin dikembalikan (0 untuk kembali): "))
    except ValueError:
        print("Input harus berupa Angka")
    except EOFError:
        print(" Jgn Klik CTRL+Z ")
    except KeyboardInterrupt:
        print(" Jgn Klik CTRL+C ")
    
    if nomor_buku == 0:
        print("Kembali ke Menu Users, LOADING...")
        time.sleep(2)
    
    elif nomor_buku < 1 or nomor_buku > len(daftar_buku):
        print(" Nomor tidak valid!")

    else:
        balik_buku = daftar_buku[nomor_buku - 1]
        if dic_buku[balik_buku]["jumlah"] < dic_buku[balik_buku]["jumlah_fix"] :
            dic_buku[balik_buku]["jumlah"] += 1
            dic_user[username]["pinjam"].remove(balik_buku)

            print(f" Buku Berjudul {balik_buku} berhasil dikembalikan")

            print(f" Mendapat Bonus +10 Poin ")    
            dic_user[username]["poin"] += 10

            with open(data_user, "w") as f:
                json.dump(user, f, indent=4)

            with open(data_buku, "w") as f:
                json.dump(buku, f, indent=4)
        else: 
            print(" Stok Buku tidak valid")


def topup_poin(username): 
    while True: 
        with open(data_user, "r") as f:
            user = json.load(f)
            dic_user = user[0]
        os.system('cls')
        print("Selamat Datang :", username)
        print("Poin anda adalah:", dic_user[username]["poin"])
        
        try:
            beli = int(input("Ingin top up berapa: Rp"))
        except ValueError:
            print("Tolong masukkan angka, moho")
            time.sleep(2)
            continue
        except KeyboardInterrupt:
            print("Jangan tekan Ctrl+C")
            continue
        except EOFError:
            print("Jangan Tekan Ctrl+Z")
            continue
        if beli >= 10000 and beli <= 500000:
        
            dic_user[username]["poin"] += beli // 1000
            print("Memproses Transaksi, Mohon Tunggu...")
            time.sleep(2)
            os.system('cls')
            print("+=======================================================+")
            print("|              STRUK TRANSAKSI TOP-UP POIN              |")
            print("+=======================================================+")
            print(f"|Nama Pelanggan: {username}                                  |")
            print(f"|Tanggal       : {date.today()}                             |")
            print("+-------------------------------------------------------+")
            print("|      Jenis Pembelian       |          Jumlah          |")
            print("+-------------------------------------------------------+")
            print(f"|Poin                        |                    {beli//1000:>6}|")
            print(f"|Total                       |               Rp {beli:>8}|")
            print("+-------------------------------------------------------+")
            print("| 'Perpustakaan Digital Samarendah - Jl.  project asik' |")
            print("|                       TERIMAKASIH                     |")
            print("+-------------------------------------------------------+")


            with open(data_user, "w") as f:
                json.dump([dic_user], f, indent=4) 

            pilihan = input("Apakah kamu ingin top up lagi? (ya / tidak): ")

            if pilihan == "ya":
                print("Silakan top up Kembali")
                continue  
            elif pilihan == "tidak":
                print("Anda sudah kembali. Terima kasih!")
                break
            else:
                print("Perintah Tidak Tersedia")
                continue
        else:
            print("Maaf, Minimal Top Up Rp10.000, Mohon Tunggu...")
            time.sleep(2)
            continue

def tukar_poin(username):
    while True:
        os.system('cls')
        with open(data_barang, "r") as f:
            barang = json.load(f)
            dic_barang = barang[0]
        with open(data_user, "r") as f:
                user = json.load(f)
                dic_user = user[0]

        #buat list barang
        daftar_barang = list(dic_barang.keys())
        
        #Menampilkan daftar merchandise
        print("          DAFTAR MERCHANDISE")
        table = PrettyTable()
        table.field_names = ["No","Nama Barang", "Harga (Poin)"]
        i = 1
        for nama_barang, keterangan in dic_barang.items():
            table.add_row([i,nama_barang,keterangan["poin"]])
            i += 1

        print(table)

        #Menampilkan Poin user
        poin = dic_user[username]["poin"]
        print(f"+===================================+")
        print(f"|         POIN ANDA : {poin}        |")
        print(f"+===================================+")
            
        try:
            nomor_barang = int(input("Pilih Barang yang ingin ditukar (0 untuk kembali): "))
        except ValueError:
            print("perintah harus berupa angka")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")
        
        if nomor_barang == 0:
            print("Kembali ke Menu User, LOADING...")
            time.sleep(2)
            break
        
        elif nomor_barang <= -1 or nomor_barang > len(daftar_barang):
            print(" Nomor tidak valid!")
            continue
        else:
            tukar_barang = daftar_barang[nomor_barang - 1]
            if dic_barang[tukar_barang]["jumlah"] >= 0 :
                if dic_user[username]["poin"] > dic_barang[tukar_barang]["poin"]:
                    dic_user[username]["poin"] -= 1
                    dic_barang[tukar_barang]["jumlah"] -= 1
                    print(f"Poin sejumlah '{dic_barang[tukar_barang]["poin"]}' berhasil ditukar dengan '{tukar_barang}'")
                    break
                else:
                    print("Poin tidak mencukupi")
            else:
                print("Maaf, Stok barang habis")



def menu_user(username):
    os.system('cls')
    while True:
        tabel = PrettyTable()
        print("-"*71)
        print(f"                        MENU USER - {username}")
        tabel.field_names = ["No","Fitur","Keterangan"]
        tabel.add_row(["1","Pinjam Buku","Meminjam buku perpustakan"])
        tabel.add_row(["2","Kembalikan Buku","mengembalikan buku perpustakaan"])
        tabel.add_row(["3","Daftar buku","Melihat daftar buku"])
        tabel.add_row(["4","Top Up","Top up Poin"])
        tabel.add_row(["5","Tukar Poin","Menukar Poin dengan Merchandise perpustakaan"])
        tabel.add_row(["6","Keluar","Log Out dan Kembali ke Menu Utama"])
        print(tabel)
        
        try:
            perintah = input("Masukkan perintah : ")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")
        if perintah == "1":
            pinjam(username)
        elif perintah == "2":
            kembalikan(username) 
        elif perintah =="3":
            daftar_buku()
        elif perintah =="4":
            topup_poin(username)
        elif perintah =="5":
            tukar_poin(username)
        elif perintah == "6":
            print("Log Out dari akun")
            break
        else:
            print("perintah tidak tersedia, Mohon Tunggu...")
            time.sleep(1)

#Program Mulai
def menu_utama():
    while True:
        os.system('cls')
        print("+=================================================+")
        print("| Selamat Datang di Aplikasi Perpustakaan Digital |")
        print("|-------------------------------------------------|")
        print("| 1. L O G I N                                    |")
        print("| 2. R E G I S T R A S I                          |")
        print("| 3. K E L U A R                                  |")
        print("+=================================================+")

        try:
            perintah = input("Silahkan pilih (1/2/3): ")
        except EOFError:
            print(" Jgn Klik CTRL+Z ")
            continue
        except KeyboardInterrupt:
            print(" Jgn Klik CTRL+C ")
            continue
            
        if perintah == "1":
            username = login()  # Terima return value dari login
            if username:  # Jika login berhasil
                with open(data_user, "r") as f:
                    user = json.load(f)
                dic_user = user[0]
                role = dic_user[username]["role"]
                
                if role == "admin":
                    menu_admin()  
                elif role == "user":
                    menu_user(username)  
                else:
                    print("Role Tidak Valid")
                    time.sleep(1)
                    
        elif perintah == "2":
            registrasi()
        elif perintah == "3":
            print("LOADING...")
            time.sleep(1)
            os.system('cls')
            print("+==========================================================+")
            print("|                                                          |")
            print("|               (TELAH KELUAR DARI PROGRAM)                |")
            print("| TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI, SAMPAI JUMPA |")
            print("|                                                          |")
            print("+==========================================================+")
            break
        else:
            print("Perintah Tidak Valid, Mohon Tunggu...")
            time.sleep(1)

menu_utama()

