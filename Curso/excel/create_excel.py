import openpyxl

excel_book = openpyxl.Workbook()
sheet = excel_book.active

data = [
    ("Name", "Age", "Company"),
    ("John", 21, "Facebook"),
    ("Hannah", 21, "Apple"),
    ("Camila", 27, "Toyota"),
    ("Steven", 32, "Google")
]

for index, row in enumerate(data):
    sheet[f'A{index+1}'] = row[0]
    sheet[f'B{index+1}'] = row[1]
    sheet[f'C{index+1}'] = row[2]

excel_book.save("my_excel_file.xlsx")
