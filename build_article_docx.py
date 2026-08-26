# -*- coding: utf-8 -*-
import os
import shutil
import zipfile
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

def create_promo_docx(template_path, output_path, content_data):
    # Read template zip
    with zipfile.ZipFile(template_path, 'r') as zin:
        file_dict = {item.filename: zin.read(item.filename) for item in zin.infolist()}
    
    # Extract sectPr from original document.xml
    orig_doc_xml = file_dict['word/document.xml'].decode('utf-8')
    sectPr_start = orig_doc_xml.find('<w:sectPr')
    if sectPr_start != -1:
        sectPr_end = orig_doc_xml.find('</w:sectPr>', sectPr_start) + len('</w:sectPr>')
        sect_pr_xml = orig_doc_xml[sectPr_start:sectPr_end]
    else:
        sect_pr_xml = '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/><w:cols w:space="720" w:num="1"/><w:docGrid w:linePitch="360" w:charSpace="0"/></w:sectPr>'

    # Extract w:document attributes and namespaces
    w_doc_start = orig_doc_xml.find('<w:document')
    w_doc_end = orig_doc_xml.find('>', w_doc_start) + 1
    w_doc_tag = orig_doc_xml[w_doc_start:w_doc_end]

    # Build body elements
    body_elements = []

    def make_title(text):
        return f'''<w:p><w:pPr><w:spacing w:after="280"/><w:jc w:val="left"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="微软雅黑" w:hAnsi="微软雅黑" w:eastAsia="微软雅黑"/><w:b/><w:color w:val="36579A"/><w:sz w:val="36"/></w:rPr><w:t>{escape(text)}</w:t></w:r></w:p>'''

    def make_body_p(text, bold_prefix=None):
        if bold_prefix:
            return f'''<w:p><w:pPr><w:pStyle w:val="16"/><w:spacing w:before="0" w:after="120" w:line="384" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="STXihei" w:hAnsi="华文细黑" w:eastAsia="华文细黑"/><w:b/><w:color w:val="2B2B2B"/><w:sz w:val="22"/></w:rPr><w:t>{escape(bold_prefix)}</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="STXihei" w:hAnsi="华文细黑" w:eastAsia="华文细黑"/><w:b w:val="0"/><w:color w:val="2B2B2B"/><w:sz w:val="22"/></w:rPr><w:t>{escape(text)}</w:t></w:r></w:p>'''
        else:
            return f'''<w:p><w:pPr><w:spacing w:before="0" w:after="120" w:line="384" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="STXihei" w:hAnsi="华文细黑" w:eastAsia="华文细黑"/><w:b w:val="0"/><w:color w:val="2B2B2B"/><w:sz w:val="22"/></w:rPr><w:t>{escape(text)}</w:t></w:r></w:p>'''

    def make_heading(text):
        return f'''<w:p><w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="STKaiti" w:hAnsi="华文楷体" w:eastAsia="华文楷体"/><w:b/><w:color w:val="8B1C1C"/><w:sz w:val="28"/></w:rPr><w:t>{escape(text)}</w:t></w:r></w:p>'''

    def make_empty_p():
        return '''<w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>'''

    def make_callout_box(text):
        return f'''<w:tbl><w:tblPr><w:tblStyle w:val="32"/><w:tblW w:w="0" w:type="auto"/><w:tblInd w:w="0" w:type="dxa"/><w:tblBorders><w:top w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:left w:val="single" w:color="4F81BD" w:sz="12" w:space="0"/><w:bottom w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:right w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:insideH w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:insideV w:val="none" w:color="auto" w:sz="0" w:space="0"/></w:tblBorders><w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tblGrid><w:gridCol w:w="9360"/></w:tblGrid><w:tr><w:tblPrEx><w:tblBorders><w:top w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:left w:val="single" w:color="4F81BD" w:sz="12" w:space="0"/><w:bottom w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:right w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:insideH w:val="none" w:color="auto" w:sz="0" w:space="0"/><w:insideV w:val="none" w:color="auto" w:sz="0" w:space="0"/></w:tblBorders><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPrEx><w:tc><w:tcPr><w:tcW w:w="9360" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F7F9FB"/></w:tcPr><w:p><w:pPr><w:spacing w:before="160" w:after="160" w:line="360" w:lineRule="auto"/><w:ind w:left="173"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="STXihei" w:hAnsi="华文细黑" w:eastAsia="华文细黑"/><w:b/><w:bCs/><w:i/><w:color w:val="8B1C1C"/><w:sz w:val="21"/></w:rPr><w:t>{escape(text)}</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'''

    # Build sequence
    # 1. Title
    body_elements.append(make_title(content_data['title']))
    
    # 2. Lead paragraph
    body_elements.append(make_body_p(content_data['lead']))

    # 3. First callout quote
    if 'callout1' in content_data and content_data['callout1']:
        body_elements.append(make_callout_box(content_data['callout1']))
        body_elements.append(make_empty_p())

    # 4. Sections
    for sec in content_data['sections']:
        body_elements.append(make_heading(sec['heading']))
        if 'intro' in sec and sec['intro']:
            body_elements.append(make_body_p(sec['intro']))
        for item in sec.get('paragraphs', []):
            if isinstance(item, tuple):
                bold_pre, p_text = item
                body_elements.append(make_body_p(p_text, bold_prefix=bold_pre))
            else:
                body_elements.append(make_body_p(item))

    # 5. Conclusion & Contact
    if 'closing' in content_data:
        closing = content_data['closing']
        body_elements.append(make_heading(closing['heading']))
        if 'intro' in closing and closing['intro']:
            body_elements.append(make_body_p(closing['intro']))
        for item in closing.get('items', []):
            if isinstance(item, tuple):
                bold_pre, p_text = item
                body_elements.append(make_body_p(p_text, bold_prefix=bold_pre))
            else:
                body_elements.append(make_body_p(item))
        if 'summary' in closing and closing['summary']:
            body_elements.append(make_body_p(closing['summary']))

    # 6. Final Callout Box
    if 'callout_final' in content_data and content_data['callout_final']:
        body_elements.append(make_callout_box(content_data['callout_final']))
        body_elements.append(make_empty_p())

    # 7. Add sectPr
    body_elements.append(sect_pr_xml)

    full_doc_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
{w_doc_tag}
<w:body>
{''.join(body_elements)}
</w:body>
</w:document>'''

    # Update zip
    file_dict['word/document.xml'] = full_doc_xml.encode('utf-8')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for fname, data in file_dict.items():
            zout.writestr(fname, data)
    print(f"Successfully generated docx: {output_path}")

