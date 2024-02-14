PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

lines = [line for line in PRICE_LIST.split('\n') if line.strip()]
items = [tuple(line.split()) for line in lines]
new_dict = {key: int(value.rstrip('р')) for key, value in items}
print(new_dict)
