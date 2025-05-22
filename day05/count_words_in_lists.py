celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

words_count_dict = {}
for word in celestial_objects:
    if word not in words_count_dict:
        words_count_dict[word] = 1
    elif word in words_count_dict:
        words_count_dict[word] += 1

for word in words_count_dict:
    print(f"{word}  {words_count_dict[word]}")