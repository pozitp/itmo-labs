import xml.etree.ElementTree as ET
import json

class XMLtoJSONConverterWithLib:
    def __init__(self):
        self.root = None

    def convert(self, input_file, output_file):
        # Parse XML using ElementTree
        tree = ET.parse(input_file)
        self.root = tree.getroot()
        
        # Convert to dictionary
        result = self.element_to_dict(self.root)
        
        # Write JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

    def element_to_dict(self, element):
        result = {}
        
        # Handle children
        if len(element) > 0:
            # Element has child elements
            children = {}
            for child in element:
                child_data = self.element_to_dict(child)
                
                if child.tag in children:
                    # Convert to list if multiple elements with same tag
                    if isinstance(children[child.tag], list):
                        children[child.tag].append(child_data[child.tag])
                    else:
                        children[child.tag] = [children[child.tag], child_data[child.tag]]
                else:
                    children[child.tag] = child_data[child.tag]
            
            result[element.tag] = children
        else:
            # Element has only text
            result[element.tag] = element.text.strip() if element.text else ""
        
        # Handle attributes
        if element.attrib:
            if isinstance(result[element.tag], dict):
                result[element.tag]["@attributes"] = element.attrib
            else:
                result[element.tag] = {
                    "#text": result[element.tag],
                    "@attributes": element.attrib
                }
                
        return result

# Usage
converter = XMLtoJSONConverterWithLib()
converter.convert("input.xml", "output_library.json")