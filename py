dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]  # список словарей
print(dictionaries)
unique_dictionary = set (val for dic in dictionaries for val in dic.values())
print(unique_dictionary)

dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]  # список словарей
print(dictionaries)
unique_dictionary = set (val for dic in dictionaries for val in dic.values())
print(unique_dictionary)
