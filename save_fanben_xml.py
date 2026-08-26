import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile(r'd:\jinyuliangyuan\格式范本\新范本.docx', 'r')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)
body = root.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body')

out = []
for i, child in enumerate(body):
    tag = child.tag.split('}')[-1]
    if tag == 'sectPr': continue
    xml_str = ET.tostring(child, encoding='unicode')
    out.append(f"=== ELEMENT [{i}] ({tag}) ===")
    out.append(xml_str)
    out.append("\n" + "="*60 + "\n")

with open(r'd:\jinyuliangyuan\full_fanben_xml.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
print("Saved full fanben xml.")
