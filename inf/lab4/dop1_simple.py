import xmltodict
import json

with open("./input.xml", "r", encoding='utf-8') as xml_file:
    o = xmltodict.parse(xml_file.read())


with open("./output_dop1.json", "w", encoding='utf-8') as f:
    json.dump(o, f, indent=4, ensure_ascii=False)