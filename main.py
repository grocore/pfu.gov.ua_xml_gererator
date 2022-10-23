import xml.etree.ElementTree as ET


document = ET.Element('DOCUMENT')

employer = ET.SubElement(document, 'EMPLOYER')

employer_edrpou = ET.SubElement(employer, 'EDRPOU')
employer_name = ET.SubElement(employer, 'NAME')
employer_edrpou.text = ''
individuals = ET.SubElement(document, 'INDIVIDUALS')

individual = ET.SubElement(individuals, 'INDIVIDUAL')

individual_rnokpp = ET.SubElement(individual, 'RNOKPP')
individual_seria_number = ET.SubElement(individual, 'SERIA_NUMBER')
individual_surname = ET.SubElement(individual, 'SURNAME')
individual_name = ET.SubElement(individual, 'NAME')
individual_patronymic = ET.SubElement(individual, 'PATRONYMIC')

records = ET.SubElement(document, 'RECORDS')

record = ET.SubElement(records, 'RECORD')

record_employer_code = ET.SubElement(record, 'EMPLOYER_CODE')
record_edrpo_sign = ET.SubElement(record, 'EDRPO_SIGN')
record_name_sign = ET.SubElement(record, 'NAME_SIGN')
record_edrpo_lr = ET.SubElement(record, 'EDRPO_LR')
record_name_lr = ET.SubElement(record, 'NAME_LR')
record_action_type = ET.SubElement(record, 'ACTION_TYPE')
record_attribute_type = ET.SubElement(record, 'ATTRIBUTE_TYPE')
record_action_dt = ET.SubElement(record, 'ACTION_DT')
record_action_text = ET.SubElement(record, 'ACTION_TEXT')
record_leave_reason = ET.SubElement(record, 'LEAVE_REASON')
record_doc_type = ET.SubElement(record, 'DOC_TYPE')
record_doc_dt = ET.SubElement(record, 'DOC_DT')
record_doc_number = ET.SubElement(record, 'DOC_NUMBER')

#write to file
tree = ET.ElementTree(document)
ET.indent(tree, space="\t", level=0)
tree.write('test.xml', xml_declaration=False, encoding='utf-8')