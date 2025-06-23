# Contoh sederhana chatbot edukasi
def chatbot_response(question):
    knowledge_base = {
        "apa itu ai": "AI adalah kecerdasan buatan yang...",
        "bagaimana cara kerja chatbot": "Chatbot bekerja dengan menganalisis input dan...",
        "default": "Maaf, saya tidak mengerti pertanyaan Anda"
    }
    return knowledge_base.get(question.lower(), knowledge_base["default"])

# Contoh penggunaan
print(chatbot_response("Apa itu AI"))  # Output: "AI adalah kecerdasan buatan yang..."