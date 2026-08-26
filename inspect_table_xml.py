import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile(r'd:\jinyuliangyuan\格式范本\新范本.docx', 'r')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)
body = root.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body')

for i, child in enumerate(body):
    tag = child.tag.split('}')[-1]
    if tag == 'tbl':
        print(f"=== Table Child [{i}] XML ===")
        print(ET.tostring(child, encoding='unicode'))
