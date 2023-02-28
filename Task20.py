skrabb = {1:'AEIOULNSTR''АВЕИНОРСТ', 2:'DG''ДКЛМПУ', 3:'BCMP''БГЁЬЯ', 4:'FHVWY''ЙЫ', 5:'K''ЖЗХЦЧ', 8:'JZ''ШЭЮ', 10:'QZ''ФЩЪ'}
text = input('Введите слово!').upper()
print(sum([k for i in text for k, v in skrabb.items() if i in v]))
