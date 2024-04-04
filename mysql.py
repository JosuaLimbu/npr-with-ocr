################################# POST langsung ke mysql ###########################################################################

import pymysql
from datetime import datetime

def write_to_mysql(cleaned_plate_text):
    conn = pymysql.connect(host="localhost", user="root", password="limbujosua23", database="db_upark")

    current_time = datetime.now().strftime("%d %B %Y %H:%M:%S")

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO tbl_detectin (plate_number, date) VALUES (%s, %s)"
            
            cursor.execute(sql, (cleaned_plate_text, current_time))
        
        conn.commit()
        print("Success.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()

# Tes fungsi write_to_mysql
def test_write_to_mysql():
    plate_number = "B1034RF"
    write_to_mysql(plate_number)
test_write_to_mysql()


############################### POST melalui REST API localhost ######################################################################

# import socket
# import requests
# from datetime import datetime

# def get_local_ip_address():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))  
#     local_ip_address = s.getsockname()[0]
#     s.close()
#     return local_ip_address

# def write_to_mysql(cleaned_plate_text):
#     # Mendapatkan alamat IP lokal
#     local_ip_address = get_local_ip_address()

#     # Menggunakan alamat IP lokal dalam URL API
#     api_url = f"http://{local_ip_address}/u-park/operator/platedetection/out/apioutpost.php"
    
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Mengubah format tanggal sesuai yang diharapkan oleh server

#     try:
#         payload = {
#             "plate_number": cleaned_plate_text,
#             "date": current_time,
#             # "last_checked_time": current_time  # Menyediakan nilai untuk last_checked_time
#         }
#         response = requests.post(api_url, json=payload)  # Mengirim data dalam format JSON
        
#         if response.status_code == 201:  # Mengubah status code menjadi 201 karena data berhasil ditambahkan
#             print("Data successfully sent.")
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#             print(f"Response content: {response.json()}")
#     except requests.exceptions.RequestException as e:
#         print(f"Request error: {e}")
#     except Exception as e:
#         print(f"Error: {e}")

# # Tes fungsi write_to_mysql
# # write_to_mysql("DP1234BU")


################################ POST melalui REST API perangkat lain ####################################################################
# import requests
# from datetime import datetime

# def write_to_mysql(cleaned_plate_text):
#     api_url = "http://192.168.10.1/u-park/operator/platedetection/out/apioutpost.php" # Ganti dengan IP perangkat lain
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

#     try:
#         payload = {
#             "plate_number": cleaned_plate_text,
#             "date": current_time,
#             "last_checked_time": current_time  
#         }
#         response = requests.post(api_url, json=payload)  # Kirim data dalam format JSON
        
#         if response.status_code == 201: 
#             print("Data successfully sent.")
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#             print(f"Response content: {response.json()}")
#     except requests.exceptions.RequestException as e:
#         print(f"Request error: {e}")
#     except Exception as e:
#         print(f"Error: {e}")

# # Tes fungsi write_to_mysql
# # write_to_mysql("B1034RF")