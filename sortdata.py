import xlrd
from shutil import copy2

book = xlrd.open_workbook("../Messidor database - diabetes/Hospital 1/Annotation_Base12.xls")
sheet = book.sheet_by_index(0)

filenames = sheet.col_slice(0,1)

row = 1
for image in filenames:
    filename = image.value
    folder = int(sheet.cell(row,2).value)
    
    source = "../Messidor database - diabetes/Hospital 1/Base12/" + filename
    if(folder == 0): #if grading is 0 put into healthy folder
        destination = "../Messidor database - diabetes/Sorted/Healthy"
    else: #if grading is 3 or 4 put into diabetic folder
        destination = "../Messidor database - diabetes/Sorted/Diabetic"
    copy2(source,destination)
    
    row = row + 1