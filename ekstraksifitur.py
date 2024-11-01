import cv2
import os
import pandas as pd
import mahotas as mt

class extraction_feature:
    @staticmethod
    def ekstraksi_warna(pathImg):
        # Tentukan path file gambar
        file_path = pathImg
        filename = os.path.basename(file_path)

        # Cek apakah file adalah gambar (berformat .png, .jpg, atau .jpeg)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Baca gambar menggunakan OpenCV
            img = cv2.imread(file_path)

            # Hitung nilai rata-rata warna RGB untuk seluruh gambar
            avg_color_per_row = cv2.mean(img)[:3]  # Ambil 3 komponen pertama (R, G, B)
            R, G, B = avg_color_per_row

            # Klasifikasikan warna air berdasarkan nilai rata-rata warna
            warna_air = extraction_feature.klasifikasi_warna_air(R, G, B)

            return filename, R, G, B, warna_air
        else:
            raise ValueError("File yang dimasukkan bukan gambar yang valid (hanya .png, .jpg, .jpeg).")

    @staticmethod
    def ekstraksi_texture(pathImg):
        # Fungsi untuk menghitung fitur GLCM dengan mahotas
        def extract_glcm_features(image_gray):
            glcm = mt.features.haralick(image_gray).mean(axis=0)
            contrast = glcm[1]   # Contrast
            homogeneity = glcm[4]  # Homogeneity
            energy = glcm[8]   # Energy
            correlation = glcm[2]  # Correlation
            return contrast, homogeneity, energy, correlation

        # Path file gambar
        file_path = pathImg
        filename = os.path.basename(file_path)

        # Cek apakah file adalah gambar (berformat .png, .jpg, .jpeg)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Baca gambar menggunakan OpenCV
            img = cv2.imread(file_path)

            # Konversi gambar ke grayscale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Ekstraksi fitur GLCM
            contrast, homogeneity, energy, correlation = extract_glcm_features(img_gray)

            return filename, contrast, homogeneity, energy, correlation
        else:
            raise ValueError("File yang dimasukkan bukan gambar yang valid (hanya .png, .jpg, .jpeg).")

    @staticmethod
    def klasifikasi_warna_air(R, G, B):
        # Logika untuk menentukan warna air berdasarkan nilai R, G, B
        if (R > 200 and G > 200 and B > 200) or (G > 200 and B > 200):  # Air jernih atau sedikit hijau atau biru
            return "Jernih"
        elif (G > 100 and B < 100) or (R > 200 and G > 200 and B < 100):  # Air agak keruh atau kehijauan
            return "Agak Keruh"
        elif (R > 150 and G < 100 and B < 100) or (R > 100 and G > 100 and B < 100):  # Air keruh, cokelat, atau gelap
            return "Keruh"
        else:
            return "Tidak terdefinisi"

    @staticmethod
    def ekstraksi_gabungan(pathImg):
        # Ekstraksi warna
        filename, R, G, B, warna_air = extraction_feature.ekstraksi_warna(pathImg)

        # Ekstraksi tekstur
        _, contrast, homogeneity, energy, correlation = extraction_feature.ekstraksi_texture(pathImg)

        # Tentukan path output
        output_folder = 'output_feature'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)  # Buat folder jika belum ada

        output_path = os.path.join(output_folder, 'combined_features_output.xlsx')

        # Cek apakah file Excel sudah ada
        if os.path.exists(output_path):
            # Baca file Excel yang sudah ada
            df_existing = pd.read_excel(output_path)

            # Dapatkan nomor urut terakhir
            last_no = df_existing['No'].max()
        else:
            # Jika belum ada, buat dataframe baru
            df_existing = pd.DataFrame(columns=['No', 'Nama', 'R', 'G', 'B', 'Kontras', 'Homogenitas', 'Energi', 'Korelasi', 'Warna Air'])
            last_no = 0

        # Tambahkan data baru ke dataframe
        new_data = pd.DataFrame([[last_no + 1, filename, R, G, B, contrast, homogeneity, energy, correlation, warna_air]],
                                columns=['No', 'Nama', 'R', 'G', 'B', 'Kontras', 'Homogenitas', 'Energi', 'Korelasi', 'Warna Air'])
        df_updated = pd.concat([df_existing, new_data], ignore_index=True)

        # Simpan hasil ke file Excel (menimpa file lama dengan data baru)
        df_updated.to_excel(output_path, index=False)

        # Mengembalikan hasil path file yang tersimpan
        return f'Hasil ekstraksi gabungan telah disimpan di {output_path}'
