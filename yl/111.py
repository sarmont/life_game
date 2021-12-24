print("Какое у вас настроение?")
smile = input()
if "хорош" in smile or "отличн" in smile or "супер" in smile:
    print("Отлично! У меня тоже все хорошо!")
elif "плохо" in smile or "ужасно" in smile or \
        "отвратительно" in smile or "хуже" in smile:
    print("Ничего страшного. Все наладится!")
else:
    print("Я не очень понимаю, какое у вас настроение.")
