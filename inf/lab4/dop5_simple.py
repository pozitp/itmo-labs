class SimpleXMLToCSV:
    def __init__(self):
        self.pos = 0
        self.xml = ""
        
    # Проверка на то, что следующий символ - это начало тега
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
        parts = tag_text.split(None, 1)
        tag_name = parts[0]
        attributes = {}
        
        if len(parts) > 1:
            attr_text = parts[1]
            while attr_text:
                attr_text = attr_text.lstrip()
                if not attr_text:
                    break
                    
                equals_pos = attr_text.find('=')
                if equals_pos == -1:
                    break
                    
                attr_name = attr_text[:equals_pos].strip()
                attr_text = attr_text[equals_pos + 1:].lstrip()
                
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
        self.pos += 1  # пропуск <
        while self.pos < len(self.xml) and self.xml[self.pos] != '>':
            tag += self.xml[self.pos]
            self.pos += 1
        if self.pos < len(self.xml):
            self.pos += 1  # пропуск >
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
        
        if attributes:
            result[tag_name]["@attributes"] = attributes

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

    def escape_csv_field(self, field):
        if not field:
            return ''
        field = str(field)
        if ',' in field or '"' in field or '\n' in field:
            return f'"{field.replace("`", "``")}"'
        return field

    def format_csv(self, data):
        rows = []
        headers = ['Day', 'Subject', 'Type', 'Start Time', 'End Time', 'Teacher', 'Room', 'Building']
        rows.append(','.join(headers))

        # Ищем нужный элемент в словаре
        schedule = data.get('schedule', {})
        days = schedule.get('day', [])
        
        # Проверка на случай, если день один
        if not isinstance(days, list):
            days = [days]
            
        for day in days:
            day_name = day.get('@attributes', {}).get('name', '')
            lessons = day.get('lesson', [])
            
            # Проверка на случай, если урок один
            if not isinstance(lessons, list):
                lessons = [lessons]
                
            for lesson in lessons:
                row = [
                    day_name,
                    lesson.get('subject', ''),
                    lesson.get('type', ''),
                    lesson.get('time', {}).get('start', ''),
                    lesson.get('time', {}).get('end', ''),
                    lesson.get('teacher', ''),
                    lesson.get('room', ''),
                    lesson.get('building', '')
                ]
                rows.append(','.join(self.escape_csv_field(field) for field in row))
        
        return '\n'.join(rows)

    def convert_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            self.xml = f.read()
        
        self.pos = 0
        result = self.parse_element()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.format_csv(result))


converter = SimpleXMLToCSV()
converter.convert_file('input.xml', 'output.csv')