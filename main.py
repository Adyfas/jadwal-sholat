# Create by : adyfas
# Tema : Sholat broo !!
# Terimakasih ini basic silakan ganti kalau mau dan Terimakasih untuk aladhan.com (:


import requests

x = input("Masukin Kode Negara bre, Contoh(id,us,): ")
b = input("Masukan kota bre, Contoh(jakarta,brebes): ")

def dapatkan_waktu_sholat(kota, negara):
    base_url = "http://api.aladhan.com/v1/calendarByCity"
    
    params = {
        "city": kota,
        "country": negara,
        "method": 2
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None

def tampilkan_waktu_sholat(waktu_sholat):
    for info_tanggal in waktu_sholat:
        tanggal = info_tanggal["date"]["gregorian"]["date"]
        print(f"\nWaktu Sholat untuk {tanggal}:")
        for sholat, waktu in info_tanggal["timings"].items():
            print(f"{sholat.capitalize()}: {waktu}")

if __name__ == "__main__":
    kota = b
    negara = x

    waktu_sholat = dapatkan_waktu_sholat(kota, negara)

    if waktu_sholat:
        tampilkan_waktu_sholat(waktu_sholat)
    else:
        print("Yahh gagal mengambil waktu sholat. ):")
