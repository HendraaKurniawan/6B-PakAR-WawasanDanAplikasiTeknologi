# Contoh sederhana analisis prediktif
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Data contoh: [waktu_belajar, jumlah_akses_materi, nilai_ujian]
data = pd.DataFrame({
    'waktu': [5, 10, 3, 8, 2],
    'akses': [15, 20, 5, 18, 3],
    'lulus': [1, 1, 0, 1, 0]  # 1=lulus, 0=tidak
})

# Model prediksi sederhana
model = DecisionTreeClassifier()
model.fit(data[['waktu', 'akses']], data['lulus'])

# Prediksi
print(model.predict([[7, 12]]))  # Output: [1] (prediksi lulus)