import xml.etree.ElementTree as ET

def generateXML(val_employer_edrpou='', val_employer_name='', val_individual_rnokpp='',
    val_individual_seria_number='', val_individual_surname='',
    val_individual_name='', val_individual_patronymic='',
    val_record_employer_code='', val_record_edrpo_sign='',
    val_record_name_sign='', val_record_edrpo_lr='',
    val_record_name_lr='', val_record_action_type='',
    val_record_attribute_type='', val_record_action_dt='',
    val_record_action_text='', val_record_leave_reason='',
    val_record_doc_type='', val_record_doc_dt='', val_record_doc_number=''):


    document = ET.Element('DOCUMENT')
    employer = ET.SubElement(document, 'EMPLOYER')
    employer_edrpou = ET.SubElement(employer, 'EDRPOU')
    employer_edrpou.text = val_employer_edrpou
    employer_name = ET.SubElement(employer, 'NAME')
    employer_name.text = val_employer_name
    individuals = ET.SubElement(document, 'INDIVIDUALS')
    individual = ET.SubElement(individuals, 'INDIVIDUAL')
    individual_rnokpp = ET.SubElement(individual, 'RNOKPP')
    individual_rnokpp.text = val_individual_rnokpp
    individual_seria_number = ET.SubElement(individual, 'SERIA_NUMBER')
    individual_seria_number.text = val_individual_seria_number
    individual_surname = ET.SubElement(individual, 'SURNAME')
    individual_surname.text = val_individual_surname
    individual_name = ET.SubElement(individual, 'NAME')
    individual_name.text = val_individual_name
    individual_patronymic = ET.SubElement(individual, 'PATRONYMIC')
    individual_patronymic.text = val_individual_patronymic
    records = ET.SubElement(document, 'RECORDS')
    record = ET.SubElement(records, 'RECORD')
    record_employer_code = ET.SubElement(record, 'EMPLOYER_CODE')
    record_employer_code.text = val_record_employer_code
    record_edrpo_sign = ET.SubElement(record, 'EDRPO_SIGN')
    record_edrpo_sign.text = val_record_edrpo_sign
    record_name_sign = ET.SubElement(record, 'NAME_SIGN')
    record_name_sign.text = val_record_name_sign
    record_edrpo_lr = ET.SubElement(record, 'EDRPO_LR')
    record_edrpo_lr.text = val_record_edrpo_lr
    record_name_lr = ET.SubElement(record, 'NAME_LR')
    record_name_lr.text = val_record_name_lr
    record_action_type = ET.SubElement(record, 'ACTION_TYPE')
    record_action_type.text = val_record_action_type
    record_attribute_type = ET.SubElement(record, 'ATTRIBUTE_TYPE')
    record_attribute_type.text = val_record_attribute_type
    record_action_dt = ET.SubElement(record, 'ACTION_DT')
    record_action_dt.text = val_record_action_dt
    record_action_text = ET.SubElement(record, 'ACTION_TEXT')
    record_action_text.text = val_record_action_text
    record_leave_reason = ET.SubElement(record, 'LEAVE_REASON')
    record_leave_reason.text = val_record_leave_reason
    record_doc_type = ET.SubElement(record, 'DOC_TYPE')
    record_doc_type.text = val_record_doc_type
    record_doc_dt = ET.SubElement(record, 'DOC_DT')
    record_doc_dt.text = val_record_doc_dt
    record_doc_number = ET.SubElement(record, 'DOC_NUMBER')
    record_doc_number.text = val_record_doc_number

    tree = ET.ElementTree(document)
    ET.indent(tree, space="\t", level=0)
    tree.write('test.xml', xml_declaration=False, encoding='utf-8')


from tkinter import *

def generate_clicked():
    generateXML(val_record_doc_number='0000')

window = Tk()
window.title("Generate XML for pfu.gov.ua")
window.geometry('800x600')
lbl = Label(window, text="EDRPO")  
lbl.grid(column=0, row=0)
btn_generate = Button(window, text="Generate", command=generate_clicked)
btn_generate.grid(column=1, row=10)
window.mainloop()