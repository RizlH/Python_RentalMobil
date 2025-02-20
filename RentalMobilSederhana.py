import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter import ttk


class RentalMobilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jasa Rental Mobil")
        self.root.geometry("850x600")

        self.username = "admin"
        self.password = "123"
        self.penyewa_list = [] 
        self.login_widgets()

    def login_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(fill="both")

        tk.Label(self.login_frame, text="Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.login_frame, text="Username:").pack(anchor='w', padx=10)
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Password:").pack(anchor='w', padx=10)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self.login_frame, text="Masuk", command=self.login, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == self.username and password == self.password:
            self.login_frame.pack_forget() 
            self.widgets() 
        else:
            messagebox.showwarning("Login Gagal", "Username atau password salah.")

    def widgets(self):
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="both")

        tk.Label(self.frame1, text="Pilih Mobil:", font=("Arial", 18)).pack(pady=20)

        self.mobil_list = {
            "Toyota Avanza": {"harga": 300000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC double blower, audio, dan irit.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None},
            "Daihatsu Xenia": {"harga": 280000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC single blower, audio, dan irit.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None},
            "Honda Mobilio": {"harga": 350000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC double blower, audio, dan responsif.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None},
            "Nissan Livina": {"harga": 320000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC double blower, audio, dan responsif.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None},
            "Toyota Innova": {"harga": 400000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC, fitur canggih, audio, irit dan responsif.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None},
            "Toyota Alphard": {"harga": 1000000, "deskripsi": "Mobil MPV, kapasitas 7 orang, AC, fitur canggih, audio, irit dan responsif.", "status": "Tersedia", "tanggal_sewa": None, "tanggal_kembali": None}
        }

        self.selected_mobil = tk.StringVar(value="Toyota Avanza")
        
        self.info_label = tk.Label(self.frame1, text="", font=("Arial", 12), wraplength=400, justify="left")
        self.info_label.pack(anchor='w', padx=10)

        for mobil in self.mobil_list.keys():
            tk.Radiobutton(self.frame1, text=mobil, variable=self.selected_mobil, value=mobil, command=self.update_info, font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)

        self.update_info() 

        tk.Button(self.frame1, text="Lanjutkan", command=self.tampil_info, font=("Arial", 12), bg="blue", fg="white").pack(pady=20, padx=20 , anchor="w")
        tk.Button(self.frame1, text="Lihat Daftar Penyewa", command=self.show_renters_page, font=("Arial", 12), bg="purple", fg="white").pack(pady=10, padx=20, anchor="w")
        tk.Button(self.frame1, text="Keluar", command=self.keluar, font=("Arial", 12), bg="red", fg="white").pack(pady=10, padx=20, anchor="e")

        self.frame2 = tk.Frame(self.root)

        tk.Button(self.frame2, text="Kembali", command=self.tampil_hal_pilihan, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

        tk.Label(self.frame2, text="Nama Penyewa:").pack(anchor='w', padx=10)
        self.nama_penyewa_entry = tk.Entry(self.frame2, font=("Arial", 12))
        self.nama_penyewa_entry.pack(pady=5)

        tk.Label(self.frame2, text="Durasi Sewa (hari):").pack(anchor='w', padx=10)
        self.durasi_entry = tk.Entry(self.frame2, font=("Arial", 12))
        self.durasi_entry.pack(pady=5)

        tk.Label(self.frame2, text="Tanggal Sewa (YYYY-MM-DD):").pack(anchor='w', padx=10)
        self.tanggal_entry = tk.Entry(self.frame2, font=("Arial", 12))
        self.tanggal_entry.pack(pady=5)

        tk.Button(self.frame2, text="Sewa Mobil", command=self.sewa_mobil, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

        tk.Label(self.frame2, text="Tanggal Kembali (YYYY-MM-DD):").pack(anchor='w', padx=10)
        self.tanggal_kembali_entry = tk.Entry(self.frame2, font=("Arial", 12))
        self.tanggal_kembali_entry.pack(pady=5)

        tk.Button(self.frame2, text="Kembalikan Unit", command=self.hitung_denda, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

        tk.Label(self.frame2, text="Note : ").pack(anchor='w', padx=10)
        tk.Label(self.frame2, text="Bila Tanggal Pengembalian Mobil telat maka akan dikenakan sanksi/denda").pack(anchor='w', padx=10)

        self.update_info()

    def keluar(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            self.root.quit()

    def update_info(self):
        mobil = self.selected_mobil.get()
        info = self.mobil_list[mobil]
        self.info_label.config(text=f"Deskripsi: {info['deskripsi']}\nHarga: Rp {info['harga']:,}\nStatus: {info['status']}")

    def tampil_info(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill="both")

    def tampil_hal_pilihan(self):
        self.frame2.pack_forget()
        self.frame1.pack(fill="both")

    def sewa_mobil(self):
        mobil = self.selected_mobil.get()
        info = self.mobil_list[mobil]
        nama_penyewa = self.nama_penyewa_entry.get()
        durasi = self.durasi_entry.get()
        tanggal_sewa = self.tanggal_entry.get()

        if nama_penyewa == "":
            messagebox.showwarning("Input Tidak Valid", "Nama penyewa harus diisi.")
            return

        if info["status"] == "Tersedia":
            if durasi.isdigit() and int(durasi) > 0:
                if len(tanggal_sewa) == 10 and tanggal_sewa[4] == '-' and tanggal_sewa[7] == '-':
                    tanggal_sewa = datetime.strptime(tanggal_sewa, "%Y-%m-%d")
                    durasi = int(durasi)
                    total_harga = info["harga"] * durasi
                    info["status"] = "Disewa"
                    info["tanggal_sewa"] = tanggal_sewa
                    info["tanggal_kembali"] = tanggal_sewa + timedelta(days=durasi)

                    penyewa = {
                        "nama": nama_penyewa,
                        "mobil": mobil,
                        "durasi": durasi,
                        "tanggal_sewa": tanggal_sewa,
                        "tanggal_kembali": info["tanggal_kembali"],
                        "total_harga": total_harga
                    }
                    self.penyewa_list.append(penyewa)

                    messagebox.showinfo("Sewa Mobil", f"{nama_penyewa} , telah menyewa {mobil} selama {durasi} hari dari tanggal {tanggal_sewa.date()}.\nTotal Harga: Rp {total_harga:,}\nTanggal Kembali: {info['tanggal_kembali'].date()}")
                    self.update_info()
                else:
                    messagebox.showwarning("Input Tidak Valid", "Format tanggal harus YYYY-MM-DD.")
            else:
                messagebox.showwarning("Input Tidak Valid", "Durasi harus berupa angka positif.")
        else:
            messagebox.showwarning("Mobil Tidak Tersedia", f"{mobil} sudah disewa.")

    def hitung_denda(self):
        tanggal_kembali = self.tanggal_kembali_entry.get()
        mobil = self.selected_mobil.get()
        info = self.mobil_list[mobil]

        if len(tanggal_kembali) == 10 and tanggal_kembali[4] == '-' and tanggal_kembali[7] == '-':
            tanggal_kembali = datetime.strptime(tanggal_kembali, "%Y-%m-%d")
            if info["tanggal_kembali"]:
                keterlambatan = (tanggal_kembali - info["tanggal_kembali"]).days
                if keterlambatan > 0:
                    denda_per_hari = info["harga"]
                    total_denda = keterlambatan * denda_per_hari
                    messagebox.showinfo("Denda Keterlambatan", f"Total denda untuk {keterlambatan} hari keterlambatan adalah: Rp {total_denda:,}")
                else:
                    messagebox.showinfo("Tidak Ada Denda", "Mobil dikembalikan tepat waktu atau lebih awal.")
                info["status"] = "Tersedia"

                self.penyewa_list = [penyewa for penyewa in self.penyewa_list if penyewa["mobil"] != mobil or penyewa["tanggal_kembali"] > tanggal_kembali]

                self.update_info()
            else:
                messagebox.showwarning("Error", "Tanggal kembali tidak ditemukan.")
        else:
            messagebox.showwarning("Input Tidak Valid", "Format tanggal harus YYYY-MM-DD.")


    def show_renters_page(self):
        self.frame1.pack_forget()

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="both", padx=10, pady=10)

        tk.Label(self.frame3, text="Daftar Penyewa", font=("Arial", 18)).pack(pady=20)

        self.tree = ttk.Treeview(self.frame3, columns=("Nama", "Mobil", "Durasi", "Sewa", "Kembali", "Total Biaya"), show="headings")

        self.tree.heading("Nama", text="Nama Penyewa")
        self.tree.heading("Mobil", text="Mobil")
        self.tree.heading("Durasi", text="Durasi (hari)")
        self.tree.heading("Sewa", text="Tanggal Sewa")
        self.tree.heading("Kembali", text="Tanggal Kembali")
        self.tree.heading("Total Biaya", text="Total Biaya")

        self.tree.column("Nama", width=150)
        self.tree.column("Mobil", width=150)
        self.tree.column("Durasi", width=100)
        self.tree.column("Sewa", width=120)
        self.tree.column("Kembali", width=120)
        self.tree.column("Total Biaya", width=150)

        if not self.penyewa_list:
            self.tree.insert("", "end", values=("Belum ada penyewaan", "", "", "", "", ""))
        else:
            for penyewa in self.penyewa_list:
                self.tree.insert("", "end", values=(
                    penyewa['nama'], 
                    penyewa['mobil'], 
                    penyewa['durasi'], 
                    penyewa['tanggal_sewa'].date(), 
                    penyewa['tanggal_kembali'].date(), 
                    f"Rp {penyewa['total_harga']:,}"
                ))

        self.tree.pack(fill="both", expand=True)

        tk.Button(self.frame3, text="Kembali", command=self.kembali_ke_halaman_utama, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)


    def kembali_ke_halaman_utama(self):
        self.frame3.pack_forget()
        self.frame1.pack(fill="both")


root = tk.Tk()
app = RentalMobilApp(root)
root.mainloop()
 