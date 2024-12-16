class SimpleXMLToJSON:
    def __init__(self):
        self.pos = 0
        self.xml = ""

    def is_valid_tag_start(self):
        if self.pos + 1 >= len(self.xml):
            return False
        next_char = self.xml[self.pos + 1]
        return (next_char.isalpha() or next_char == '/' or 
                next_char == '?' or next_char == '!')

    def parse_content(self):
        content = ""
        while self.pos < len(self.xml):
            if self.xml[self.pos] == '<' and self.is_valid_tag_start():
                break
            content += self.xml[self.pos]
            self.pos += 1
        return content.strip()

    def parse_attributes(self, tag_text):
        # Делим текст тега на имя и часть атрибутов
        parts = tag_text.split(None, 1)
        tag_name = parts[0]
        attributes = {}
        
        if len(parts) > 1:
            attr_text = parts[1]
            while attr_text:
                # Пропускаем пробелы
                attr_text = attr_text.lstrip()
                if not attr_text:
                    break
                    
                # Ищем имя атрибута
                equals_pos = attr_text.find('=')
                if equals_pos == -1:
                    break
                    
                attr_name = attr_text[:equals_pos].strip()
                attr_text = attr_text[equals_pos + 1:].lstrip()
                
                # Ищем значение атрибута
                quote = attr_text[0]
                if quote not in '"\'':
                    break
                    
                end_quote = attr_text.find(quote, 1)
                if end_quote == -1:
                    break
                    
                attr_value = attr_text[1:end_quote]
                attributes[attr_name] = attr_value
                attr_text = attr_text[end_quote + 1:]
                
        return tag_name, attributes

    def parse_tag(self):
        tag = ""
        self.pos += 1  # пропускаем <
        while self.pos < len(self.xml) and self.xml[self.pos] != '>':
            tag += self.xml[self.pos]
            self.pos += 1
        if self.pos < len(self.xml):
            self.pos += 1  # пропускаем >
        return self.parse_attributes(tag.strip())

    def parse_element(self):
        if self.pos >= len(self.xml):
            return None

        while self.pos < len(self.xml) and self.xml[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.xml):
            return None

        if self.xml[self.pos] != '<':
            return self.parse_content()

        if self.pos + 1 < len(self.xml) and self.xml[self.pos:self.pos+2] in ('<?', '<!'):
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            if self.pos < len(self.xml):
                self.pos += 1
            return self.parse_element()

        if self.pos + 1 < len(self.xml) and self.xml[self.pos:self.pos+2] == '</':
            self.pos += 2
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            if self.pos < len(self.xml):
                self.pos += 1
            return None

        tag_name, attributes = self.parse_tag()
        
        children = []
        while True:
            child = self.parse_element()
            if child is None:
                break
            children.append(child)

        result = {tag_name: {}}
        
        # Добавляем атрибуты при наличии
        if attributes:
            result[tag_name]["@attributes"] = attributes

        # Добавляем текстовое содержимое или дочерние элементы
        if len(children) == 1 and isinstance(children[0], str):
            if attributes:
                result[tag_name]["_text"] = children[0]
            else:
                result[tag_name] = children[0]
        elif children:
            for child in children:
                if isinstance(child, dict):
                    for k, v in child.items():
                        if k in result[tag_name]:
                            if not isinstance(result[tag_name][k], list):
                                result[tag_name][k] = [result[tag_name][k]]
                            result[tag_name][k].append(v)
                        else:
                            result[tag_name][k] = v

        return result

    def format_json(self, obj, level=0):
        indent = "    " * level
        
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                items.append(f'{indent}    "{k}": {self.format_json(v, level + 1)}')
            return "{\n" + ",\n".join(items) + f"\n{indent}}}"
        
        elif isinstance(obj, list):
            items = [self.format_json(item, level + 1) for item in obj]
            return "[\n" + ",\n".join(f"{indent}    {item}" for item in items) + f"\n{indent}]"
        
        elif isinstance(obj, str):
            return f'"{obj}"'
        
        return str(obj)

    def convert_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            self.xml = f.read()
        
        self.pos = 0
        result = self.parse_element()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.format_json(result))


converter = SimpleXMLToJSON()
converter.convert_file('input.xml', 'output.json')