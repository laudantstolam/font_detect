from create_excel import*

number2category = {}
for i in range(1, number+1):
    number2category[i] = s1.cell(i+1, 2).value

category2font = {}
for i in range(1, number+1):
    category_value = s1.cell(i+1, 2).value
    category2font[category_value] = s1.cell(i+1, 4).value
