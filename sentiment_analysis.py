def calculate_sentiment(text, lexicon, boosters, diminishers, negation_words, tokenize_and_stem):
    words = tokenize_and_stem(text)
    sentiment_score = 0.0
    negation_count = 0  # Olumsuzluk kelimesi sayacı

    for word in words:
        word_score = lexicon.get(word, 0)

        # Güçlendirici etkiler
        for booster in boosters:
            if booster in words:
                word_score *= boosters[booster]

        # Zayıflatıcı etkiler
        for diminisher in diminishers:
            if diminisher in words:
                word_score *= diminishers[diminisher]

        # Olumsuzluk kelimeleri kontrolü
        if word in negation_words:
            negation_count += 1  # Olumsuzluk sayısını artır
        else:
            # Çift sayıda olumsuzluk kelimesi varsa ters etkisi kaldırılır
            if negation_count % 2 != 0:
                word_score *= -1  # Negatif anlam uygula
            negation_count = 0  # Sayaç sıfırlanır

        # Duygu skorunu güncelle
        sentiment_score += word_score
    #print(f"Negatif Kelime Sayısı: {word}",negation_count)
    return sentiment_score

def analyze_sentiment(text, lexicon, boosters, diminishers, negation_words, tokenize_and_stem):
    sentiment_score = calculate_sentiment(
        text, lexicon, boosters, diminishers, negation_words, tokenize_and_stem
    )

    if sentiment_score > 0:
        sentiment = "Pozitif"
    elif sentiment_score < 0:
        sentiment = "Negatif"
    else:
        sentiment = "Nötr"

    return sentiment_score, sentiment
