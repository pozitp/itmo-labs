import re

def count_smileys(arr):
    pattern = re.compile(r';</')
    smileys = pattern.findall(arr)

    return len(smileys)

test_text = ':-) ;-) :-D ;</ ;</ O:) ):0 >:| ;('
print(count_smileys(test_text))