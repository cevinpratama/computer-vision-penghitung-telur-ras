# 🥚 Penghitung Telur Real-Time dengan YOLOv8

Selamat datang di Proyek Penghitung Telur Real-Time! Ini adalah sebuah sistem cerdas yang dirancang untuk mendeteksi, melacak, dan menghitung telur secara otomatis menggunakan umpan video dari webcam. Proyek ini dibangun dengan teknologi *computer vision* modern seperti **YOLOv8**, **OpenCV**, dan pustaka **Supervision**.

## 🚀 Fitur Utama

-   🎯 **Deteksi Akurat**: Menggunakan model YOLOv8 yang telah dilatih khusus untuk mengenali telur dengan presisi tinggi di berbagai kondisi.
-   👣 **Pelacakan Objek (Tracking)**: Setiap telur yang terdeteksi diberi ID unik menggunakan algoritma ByteTrack, memungkinkannya untuk dilacak secara konsisten bahkan saat bergerak.
-   🔢 **Penghitungan Otomatis**: Sebuah garis virtual di layar berfungsi sebagai pemicu. Setiap kali telur yang dilacak melewatinya, total hitungan akan bertambah secara otomatis.
-   🖥️ **Visualisasi Real-Time**: Tampilan antarmuka yang informatif, lengkap dengan kotak pembatas (*bounding box*), ID pelacakan, garis virtual, dan total hitungan yang selalu diperbarui.

## 🛠️ Teknologi yang Digunakan

Proyek ini dibangun menggunakan beberapa pustaka dan kerangka kerja:

-   [**Python 3.10**](https://www.python.org/)
-   [**Ultralytics YOLOv8**](https://github.com/ultralytics/ultralytics)
-   [**OpenCV-Python**](https://opencv.org/)
-   [**Supervision**](https://github.com/roboflow/supervision)
-   [**NumPy**](https://numpy.org/)