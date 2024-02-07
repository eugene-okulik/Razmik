text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
       "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

for i in text.split():
    if "," in i:
        i += 'ing'
        comma_index = i.index(',')
        new_s = i[:comma_index] + i[comma_index + 1:] + i[comma_index]
        print(new_s, end=' ')
    elif "." in i:
        i += 'ing'
        comma_index = i.index('.')
        new_s = i[:comma_index] + i[comma_index + 1:] + i[comma_index]
        print(new_s, end=' ')
    else:
        i += 'ing'
        print(i, end=' ')
