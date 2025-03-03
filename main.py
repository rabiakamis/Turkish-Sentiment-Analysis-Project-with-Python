import pandas as pd
from lexicon import load_lexicon_from_xml, load_modifiers, load_negation_words
from preprocessing import tokenize_and_stem
from sentiment_analysis import analyze_sentiment
from metrics import calculate_metrics

# Dosya yolları
LEXICON_FILE = "lexicon.xml"
BOOSTERS_FILE = "boosters.txt"
DIMINISHERS_FILE = "diminishers.txt"
NEGATION_FILE = "negation_words.txt"
INPUT_FILE = "ornek_duygu-analizi-verisi_pozitif_negatif.xlsx"
OUTPUT_FILE = "analyzed_sentences.xlsx"

# Veriyi yükle
lexicon = load_lexicon_from_xml(LEXICON_FILE)
boosters = load_modifiers(BOOSTERS_FILE)
diminishers = load_modifiers(DIMINISHERS_FILE)
negation_words = load_negation_words(NEGATION_FILE)

# Veriyi analiz et
def analyze_excel(input_file, output_file):
    df = pd.read_excel(input_file)

    results = []
    for _, row in df.iterrows():
        sentence = row["Cümle"]
        actual_class = row["Sınıf"]
        score, predicted_class = analyze_sentiment(
            sentence, lexicon, boosters, diminishers, negation_words, tokenize_and_stem
        )
        results.append((sentence, actual_class, score, predicted_class))

    result_df = pd.DataFrame(results, columns=["Cümle", "Sınıf", "Sentiment Score", "Tahmin"])
    metrics = calculate_metrics(result_df)

    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")

    result_df.to_excel(output_file, index=False)
    print(f"Analiz tamamlandı! Sonuçlar '{output_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    analyze_excel(INPUT_FILE, OUTPUT_FILE)
    ssentence = "Bugün gördüğüm kadarıyla ve hava durumuna baktığım kadarıyla hiç güzel bir gün değil."
    twords = tokenize_and_stem(ssentence)
    print("Kelimelerine ayrılmış hali:", twords)