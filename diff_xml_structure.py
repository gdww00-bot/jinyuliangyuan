import zipfile
import xml.etree.ElementTree as ET

def get_xml_structure(filepath):
    with zipfile.ZipFile(filepath, 'r') as z:
        doc_xml = z.read('word/document.xml')
    root = ET.fromstring(doc_xml)
    body = root.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body')
    
    result = []
    for i, child in enumerate(body):
        tag = child.tag.split('}')[-1]
        if tag == 'sectPr':
            continue
        # serialize child XML without text node content for structural diff
        # clone element and clear text
        clone = ET.fromstring(ET.tostring(child))
        for elem in clone.iter():
            elem.text = "TEXT" if elem.text and elem.text.strip() else None
            elem.tail = None
        result.append((i, tag, ET.tostring(clone, encoding='unicode')))
    return result

fanben_struct = get_xml_structure(r'd:\jinyuliangyuan\格式范本\新范本.docx')

print("--- 新范本.docx Structure ---")
for i, tag, xml_str in fanben_struct:
    print(f"[{i}] <{tag}>: {xml_str[:250]}")
