import xml.etree.ElementTree as ET

def find_and_override_lemma(input_file, output_file, select_tag, target_opening, target_closing, new_lemma):
    tree = ET.parse(input_file)
    root = tree.getroot()

    stack = [root]
    while stack:
        current = stack.pop()
        for child in current:
            if child.tag == select_tag:
                print(current.attrib['lemma'])
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

