from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from jpype import JClass
from jpype import startJVM, getDefaultJVMPath, JClass

startJVM(getDefaultJVMPath(), "-Djava.class.path=zemberek-full.jar")

# NLTK için Türkçe stopwords
turkish_stopwords = set(stopwords.words("turkish"))

# Zemberek Türkçe morfoloji analizi
TurkishMorphology = JClass("zemberek.morphology.TurkishMorphology")
morphology = TurkishMorphology.createWithDefaults()

def tokenize_and_stem(text):
    words = word_tokenize(text.lower())
    stemmed_words = []

    for word in words:
        if word.isalnum() and word not in turkish_stopwords:  # Alfanümerik olmayanları filtrele
            analysis = morphology.analyzeAndDisambiguate(word).bestAnalysis()
            stem = analysis[0].getStem()
            stemmed_words.append(stem)
    
    return stemmed_words
