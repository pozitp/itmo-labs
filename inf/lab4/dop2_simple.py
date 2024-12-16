import re

class RegexXMLToJSON:
    TAG_PATTERN = re.compile(r'<([^>]+)>')
    ATTR_PATTERN = re.compile(r'([^\s=]+)\s*=\s*["\']([^"\']*)["\']')
    PROCESSING_PATTERN = re.compile(r'<\?.*?\?>|<!.*?>')
    
    def __init__(self):
        self.pos = 0
        self.xml = ""

    def parse_content(self):
        # Извлечение текста между тегами
        next_tag = self.TAG_PATTERN.search(self.xml, self.pos)
        if not next_tag:
            content = self.xml[self.pos:].strip()
            self.pos = len(self.xml)
            return content
            
        content = self.xml[self.pos:next_tag.start()].strip()
        self.pos = next_tag.start()
        return content

    def parse_attributes(self, tag_text):
        # Разделение на имя тега и атрибуты
        parts = tag_text.strip().split(None, 1)
        tag_name = parts[0].strip('/')
        attributes = {}
        
        if len(parts) > 1:
            # Ищем все атрибуты в теге
            matches = self.ATTR_PATTERN.finditer(parts[1])
            attributes = {m.group(1): m.group(2) for m in matches}
                
        return tag_name, attributes

    def parse_tag(self):
        match = self.TAG_PATTERN.match(self.xml, self.pos)
        if not match:
            return None, {}
            
        self.pos = match.end()
        return self.parse_attributes(match.group(1))

    def skip_processing_instructions(self):
        while True:
            match = self.PROCESSING_PATTERN.match(self.xml, self.pos)
            if not match:
                break
            self.pos = match.end()

    def parse_element(self):
        if self.pos >= len(self.xml):
            return None

        # Пропуск пробелов и ненужных тегов
        self.xml = self.xml[self.pos:].lstrip()
        self.pos = 0
        self.skip_processing_instructions()
        
        if not self.xml[self.pos:]:
            return None

        if self.xml[self.pos] != '<':
            return self.parse_content()

        # Проверка на закрывающий тег
        if self.xml[self.pos:self.pos+2] == '</':
            match = self.TAG_PATTERN.match(self.xml, self.pos)
            if match:
                self.pos = match.end()
            return None

        tag_name, attributes = self.parse_tag()
        if not tag_name:
            return None
        
        children = []
        while True:
            child = self.parse_element()
            if child is None:
                break
            children.append(child)

        result = {tag_name: {}}
        
        # Добавление атрибутов если они есть
        if attributes:
            result[tag_name]["@attributes"] = attributes

        # Добавление текста или дочерних элементов
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


converter = RegexXMLToJSON()
converter.convert_file('input.xml', 'output_dop2.json')