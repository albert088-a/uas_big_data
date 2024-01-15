# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_big_data"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE daftar_nomor_pokok_sekolah (
    
     id INT AUTO_INCREMENT PRIMARY KEY,
     
    kode_provinsi INT  ,
    
    nama_provinsi VARCHAR(255),
    
    kode_kabupaten_kota INT,
    
    nama_kabupaten_kota VARCHAR(255),
    
    bps_kode_kecamatan INT,
    
    bps_nama_kecamatan VARCHAR(255),
    
    kemendagri_kode_kecamatan INT,
    
    kemendagri_nama_kecamatan VARCHAR(255),
    
    nama_sekolah VARCHAR(255),
    
    npsn INT,
    
    status_sekolah VARCHAR(255),
    
    alamat_sekolah VARCHAR(255),
    
    tahun INT

    
)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()