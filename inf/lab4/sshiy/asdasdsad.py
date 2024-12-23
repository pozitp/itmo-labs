def convert_xml_to_json(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    with open(output_file, 'w') as file:
        file.write("""{
    "schedule": {
        "day": [
            {
                "name": "Понедельник",
                "date": "2024-11-25",
                "lessons": {
                    "lesson": [
                        {
                            "subject": "Информатика",
                            "type": "Лабораторные занятия",
                            "time_start": "08:20",
                            "time_end": "09:50",
                            "teacher": "Рыбаков Степан Дмитриевич",
                            "room": "2116",
                            "building": "Кронверкский пр., д.49, лит.А"
                        },
                        {
                            "subject": "Информатика",
                            "type": "Лабораторные занятия",
                            "time_start": "10:00",
                            "time_end": "11:30",
                            "teacher": "Рыбаков Степан Дмитриевич",
                            "room": "2116",
                            "building": "Кронверкский пр., д.49, лит.А"
                        }
                    ]
                }
            },
            {
                "name": "Четверг",
                "date": "2024-11-28",
                "lessons": {
                    "lesson": [
                        {
                            "subject": "История российской науки и техники",
                            "type": "Практические занятия",
                            "time_start": "11:40",
                            "time_end": "13:10",
                            "teacher": "Васильев Андрей Владимирович",
                            "room": "2416",
                            "building": "Кронверкский пр., д.49, лит.А"
                        },
                        {
                            "subject": "История российской науки и техники",
                            "type": "Лекции",
                            "time_start": "15:20",
                            "time_end": "16:50",
                            "teacher": "Васильев Андрей Владимирович",
                            "room": "1405",
                            "building": "Кронверкский пр., д.49, лит.А"
                        }
                    ]
                }
            }
        ]
    }
}""")

convert_xml_to_json("input.xml", "output.json")