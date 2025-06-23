# Contoh sederhana sistem rekomendasi materi
def recommend_material(student_skills):
    materials = {
        "pemula": ["Dasar-dasar Python", "Pengenalan AI"],
        "menengah": ["Algoritma Machine Learning", "Pemrosesan Bahasa Alami"],
        "mahir": ["Deep Learning", "Computer Vision"]
    }
    
    if student_skills < 3:
        return materials["pemula"]
    elif 3 <= student_skills < 7:
        return materials["menengah"]
    else:
        return materials["mahir"]

# Contoh penggunaan
print(recommend_material(4))  # Output: ["Algoritma Machine Learning", ...]