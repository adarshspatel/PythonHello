#Create Excel file using make_excel
#Thanks to make_excel author to make such useful library


import make_excel
import pyexcel as readingobj

#Change file path and name before your run
make_excel.make_excel({'data': [1, 2, 3, 4, 5, 6, 7], 'data1': ['apples', 'oranges'],  'data3': 1}, full_filepath='d:\\folder\\file1.xls')

print("File Created Succesfully\n")

print("Now Let's Try to read file")

#Install pyexcel-xls before you run
#Reading Excel File using pyexcel library
#Change file path and name before your run
mydata = readingobj.iget_records(file_name="d:\\folder\\file1.xls")

for row in mydata:
    print("%d %s" % ( row['data'],row['data1']))

