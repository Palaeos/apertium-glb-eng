import xml.etree.ElementTree as ET
import csv, re


def find_and_override_lemma(input_file, output_file, select_tag, target_opening, target_closing, new_lemma):
    tree = ET.parse(input_file)
    root = tree.getroot()
    EngSpaGlb_dictionary = {}
    filename = "./word-list.csv"

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            englishGlosses = re.sub("\(_.*?_\)", "", row[4]).strip().split("; ")
            spanishGlosses = re.sub("\(_.*?_\)", "", row[7]).strip().split("; ")
            for englishGloss in englishGlosses[0].split(", "):
                for spanishGloss in spanishGlosses[0].split(", "):
                    EngSpaGlb_dictionary[(englishGloss, spanishGloss)] = row[0]



    stack = [root]
    while stack:
        current = stack.pop()
        for child in current:
            if child.tag == select_tag:
                if (current.attrib['lemma'], child.attrib['lemma']) in EngSpaGlb_dictionary:
                    child.attrib['lemma'] = EngSpaGlb_dictionary[current.attrib['lemma'], child.attrib['lemma']]
                print(child.attrib['lemma'])
            stack.append(child)

    tree.write(output_file)

# Example usage
if __name__ == "__main__":
    input_file = "apertium-eng-spa.eng-spa.lrx"
    output_file = "apertium-glb-eng.eng-glb.lrx"
    select_tag = "select"
    target_opening = "match"
    target_closing = "match"
    new_lemma = "new_lemma"
    
    find_and_override_lemma(input_file, output_file, select_tag, target_opening, target_closing, new_lemma)

