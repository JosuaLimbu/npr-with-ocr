import pymysql
from datetime import datetime

def write_to_mysql(cleaned_plate_text):
    # Membuat koneksi ke database
    conn = pymysql.connect(host="localhost", user="root", password="limbujosua23", database="db_upark")

    # Mendapatkan waktu saat ini
    current_time = datetime.now().strftime("%d %B %Y %H:%M:%S")

    try:
        with conn.cursor() as cursor:
            # Menyiapkan pernyataan SQL untuk memasukkan data ke dalam tabel platedetect
            sql = "INSERT INTO platedetect (number_plate, date) VALUES (%s, %s)"
            
            # Menjalankan pernyataan SQL untuk memasukkan data ke dalam tabel
            cursor.execute(sql, (cleaned_plate_text, current_time))
        
        # Commit perubahan ke database
        conn.commit()
        print("Data berhasil dimasukkan ke dalam tabel platedetect.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Menutup koneksi
        conn.close()
