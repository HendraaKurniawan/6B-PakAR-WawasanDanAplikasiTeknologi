# Contoh sederhana sistem tutor adaptif
def provide_feedback(student_answer, correct_answer):
    if student_answer == correct_answer:
        return "Benar! Bagus sekali!"
    else:
        return "Coba lagi. Petunjuk: Perhatikan rumus dasarnya."

# Contoh penggunaan
print(provide_feedback(10, 15))  # Output: "Coba lagi..."
print(provide_feedback(15, 15))  # Output: "Benar!..."