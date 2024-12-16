import time
from main_simple import SimpleXMLToJSON
from dop2_simple import RegexXMLToJSON
import xmltodict
import json

def measure_performance(test_func, iterations=100):
    start_time = time.time()
    
    for _ in range(iterations):
        test_func()
        
    total_time = time.time() - start_time
    return total_time / iterations

def test_simple():
    converter = SimpleXMLToJSON()
    converter.convert_file('input.xml', 'output.json')

def test_regex():
    converter = RegexXMLToJSON()
    converter.convert_file('input.xml', 'output_dop2.json')

def test_xmltodict():
    with open("input.xml", "r", encoding='utf-8') as xml_file:
        o = xmltodict.parse(xml_file.read())
    with open("output_dop1.json", "w", encoding='utf-8') as f:
        json.dump(o, f, indent=4, ensure_ascii=False)

def main():
    try:
        iterations = 100
        print(f"\nЗапускаю тест на {iterations} циклов...\n")

        simple_time = measure_performance(test_simple, iterations)
        regex_time = measure_performance(test_regex, iterations)
        xmltodict_time = measure_performance(test_xmltodict, iterations)

        print("Результаты (среднее время на выполнение 1 цикла):")
        print("-" * 50)
        print(f"{'Скрипт':<20} {'Время (секунды)':<15}")
        print("-" * 50)
        print(f"{'Обычный':<20} {simple_time:.6f}")
        print(f"{'Regex':<20} {regex_time:.6f}")
        print(f"{'xmltodict':<20} {xmltodict_time:.6f}")
        print("-" * 50)

    except Exception as e:
        print(f"ОШИБКА: {e}")

if __name__ == "__main__":
    main()