import re

class XMLtoJSONConverterRegex:
    def __init__(self):
        self.xml = ""
        
    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.xml = file.read()
            
    def parse_xml(self, xml_string):
        # Remove comments
        xml_string = re.sub(r'<!--.*?-->', '', xml_string, flags=re.DOTALL)
        
        # Parse tag with attributes and content
        tag_pattern = r'<(?P<tag>[^\s/>]+)(?P<attrs>[^>]*)>(?P<content>.*?)</\1>'
        self_closing_pattern = r'<(?P<tag>[^\s/>]+)(?P<attrs>[^>]*)/>'
        
        def parse_attributes(attrs_string):
            if not attrs_string.strip():
                return {}
            attr_pattern = r'\s*(\w+)="([^"]*)"'
            return dict(re.findall(attr_pattern, attrs_string))
            
        def parse_element(text):
            # Try self-closing tag first
            self_closing_match = re.match(self_closing_pattern, text.strip())
            if self_closing_match:
                tag = self_closing_match.group('tag')
                attrs = parse_attributes(self_closing_match.group('attrs'))
                return {tag: attrs if attrs else ""}
            
            # Try normal tag
            match = re.match(tag_pattern, text.strip(), re.DOTALL)
            if not match:
                # Pure text content
                text = re.sub(r'\s+', ' ', text.strip())
                return text if text else None
                
            tag = match.group('tag')
            attrs = parse_attributes(match.group('attrs'))
            content = match.group('content').strip()
            
            # Split content into child elements
            child_elements = []
            remaining_content = content
            while remaining_content:
                remaining_content = remaining_content.strip()
                if not remaining_content:
                    break
                    
                # Try to match a complete tag
                child_match = re.match(tag_pattern, remaining_content, re.DOTALL)
                self_close_match = re.match(self_closing_pattern, remaining_content)
                
                if child_match:
                    child_elements.append(parse_element(child_match.group(0)))
                    remaining_content = remaining_content[len(child_match.group(0)):].strip()
                elif self_close_match:
                    child_elements.append(parse_element(self_close_match.group(0)))
                    remaining_content = remaining_content[len(self_close_match.group(0)):].strip()
                else:
                    # Text content until next tag
                    next_tag = re.search(r'<\w+', remaining_content)
                    if next_tag:
                        text_content = remaining_content[:next_tag.start()].strip()
                        if text_content:
                            child_elements.append(text_content)
                        remaining_content = remaining_content[next_tag.start():].strip()
                    else:
                        if remaining_content.strip():
                            child_elements.append(remaining_content.strip())
                        break
            
            result = {tag: {}}
            
            if len(child_elements) == 1 and isinstance(child_elements[0], str):
                result[tag] = child_elements[0]
            elif child_elements:
                for child in child_elements:
                    if isinstance(child, dict):
                        for k, v in child.items():
                            if k in result[tag]:
                                if not isinstance(result[tag][k], list):
                                    result[tag][k] = [result[tag][k]]
                                result[tag][k].append(v)
                            else:
                                result[tag][k] = v
            
            if attrs:
                if isinstance(result[tag], dict):
                    result[tag]["@attributes"] = attrs
                else:
                    result[tag] = {
                        "#text": result[tag],
                        "@attributes": attrs
                    }
                    
            return result
            
        return parse_element(xml_string)
    
    def format_json_string(self, obj, level=0):
        indent = "    " * level
        
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                formatted_key = f'"{k}"'
                formatted_value = self.format_json_string(v, level + 1)
                items.append(f'{indent}    {formatted_key}: {formatted_value}')
            return "{\n" + ",\n".join(items) + f"\n{indent}}}"
            
        elif isinstance(obj, list):
            items = [self.format_json_string(item, level + 1) for item in obj]
            return "[\n" + ",\n".join(f"{indent}    {item}" for item in items) + f"\n{indent}]"
            
        elif isinstance(obj, str):
            cleaned = obj.replace('\n', ' ').replace('  ', ' ').strip()
            escaped = cleaned.replace('"', '\\"')
            return f'"{escaped}"'
            
        return str(obj)

    def convert(self, input_file, output_file):
        self.read_file(input_file)
        if not self.xml.strip():
            raise ValueError("Empty XML file")
            
        result = self.parse_xml(self.xml)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            formatted_json = self.format_json_string(result)
            file.write(formatted_json)

# Usage
converter = XMLtoJSONConverterRegex()
converter.convert("input.xml", "output_regex.json")