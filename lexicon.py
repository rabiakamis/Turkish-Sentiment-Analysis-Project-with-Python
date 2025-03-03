import xml.etree.ElementTree as ET

def load_lexicon_from_xml(xml_file):
    lexicon = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for word in root.findall(".//WORD"):
        name = word.find("NAME").text
        pscore = float(word.find("PSCORE").text)
        nscore = float(word.find("NSCORE").text)
        lexicon[name] = pscore - nscore  # Pozitif ve negatif skoru birleştirerek genel skor oluştur

    return lexicon

def load_modifiers(file_path):
    modifiers = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            word, value = line.strip().split(":")
            modifiers[word] = float(value)
    return modifiers

def load_negation_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]
   