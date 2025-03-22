while True :
    meme_dict = {
        "КРИНЖ": "Что-то очень странное или стыдное",
        "ЛОЛ": "Что-то очень смешное",
        "РОФЛ": "шутка",
        "ЩИЩ": "одобрение или восторг",
        "КРИПОВЫЙ":"страшный, пугающий",
        "АГРИТЬСЯ":"злиться"
        
    }
    
    # Demande un mot et le normalise
    word = input("Введите непонятное слово (n'importe comment) : ").strip().upper()  # Supprime espaces + met en majuscules
    
    # Vérifie si le mot normalisé est dans le dictionnaire
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("arrache ton crane")
