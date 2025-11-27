import speech_recognition
from speech import speech_en as speeches
from random import choice, randint
import time 

seviyeler = {
    "kolay": ["Dairy", "Mouse", "Computer"],
    "orta": ["Programming", "Algorithm", "Developer"],
    "zor": ["Neural Network", "Machine Learning", "Artificial Intelligence"]
}

def bonus_game(level):
    words = seviyeler.get(level, [])
    if not words:
        return "Geçersiz seviye seçimi."
    score = 0 
    num_attends = 3 
    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Lütfen şu cümleyi söyleyiniz: {random_word}")
        recog_word = speeches()
        print(recog_word)

        if random_word == recog_word:
            score +=1
            print("Doğru!")
        else:
            print(f"Yanlış! doğru telaffuz ediniz: {random_word}")

        time.sleep(2)

    print(f"Oyun Bitti! Skorunuz: .{score}/{len(words)}")

select_level = input("Lütfen seviye seçin (kolay,orta,zor): ").lower()
bonus_game(select_level)