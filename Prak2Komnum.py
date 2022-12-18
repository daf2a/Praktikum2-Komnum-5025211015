import time

def romberg_integration(f, a, b, epsilon):
  # Inisialisasi tabel Romberg dengan nilai 0
  r = [[0 for j in range(10)] for i in range(10)]
  h = b - a
  r[1][1] = h * (f(a) + f(b)) / 2
 
  # Menghitung nilai integral dengan tingkat akurasi yang lebih tinggi
  for i in range(2, 10):
    h /= 2
    s = 0
    for j in range(1, 2**(i-2) + 1):
      s += f(a + (2*j - 1) * h)
    r[i][1] = r[i-1][1] / 2 + h * s
 
    # Menggunakan rumus untuk menghitung nilai integral dengan tingkat akurasi yang lebih tinggi
    for j in range(2, i+1):
      r[i][j] = (4**(j-1) * r[i][j-1] - r[i-1][j-1]) / (4**(j-1) - 1)
 
  # Mencari nilai integral dengan tingkat akurasi yang diinginkan
  for i in range(2, 10):
    if abs(r[i][i-1] - r[i-1][i-1]) < epsilon:
      return r[i][i-1]
 
  return "Tidak dapat mencapai tingkat akurasi yang diinginkan."

def trapezoidal_integration(f, a, b, n):
  # Menghitung h
  h = (b - a) / n
 
  # Menghitung nilai integral
  s = 0
  for i in range(1, n):
    s += f(a + i * h)
 
  # Menggabungkan hasil dengan rumus metode Trapezoidal
  result = (h / 2) * (f(a) + f(b) + 2 * s)
 
  return result
 
# Contoh penggunaan fungsi romberg_integration dan trapezoidal_integration
def f(x):
  return x**2 + 3*x + 2
 
# Menghitung waktu yang diperlukan untuk menghitung 1000 kali dengan metode romberg
start = time.time()
for i in range(0, 1000):
  result_romberg = romberg_integration(f, 1, 6, 1e-6)
end = time.time()
time_romberg = end - start
 
# Menghitung waktu yang diperlukan untuk menghitung 1000 kali dengan metode trapezoidal
start = time.time()
for i in range(0, 1000):
  result_trapezoidal = trapezoidal_integration(f, 1, 6, 1000)
end = time.time()
time_trapezoidal = end - start


# Menampilkan hasil perhitungan dan waktu yang diperlukan
print("Fungsi yang digunakan: x^2 + 3x + 2")
print("Dalam rentang 1 sampai 6, didapatkan :\n")

print("Hasil perhitungan dengan metode Romberg:", result_romberg)
print("Waktu yang diperlukan:", time_romberg/1000, "detik", "\n")

print("Hasil perhitungan dengan metode Trapezoidal:", result_trapezoidal)
print("Waktu yang diperlukan:", time_trapezoidal/1000, "detik", "\n")

# Menampilkan metode yang lebih cepat
if(time_romberg > time_trapezoidal):
  print("Sehingga, Metode Trapezoidal lebih cepat")
else:
  print("Sehingga, Metode Romberg lebih cepat")
