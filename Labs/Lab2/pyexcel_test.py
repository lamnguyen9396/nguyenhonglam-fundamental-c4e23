import pyexcel
from collections import OrderedDict

#2 Prepare data
data = [
     OrderedDict({
         "Name": 'Adam',
         "Age": 28
     }),
     OrderedDict({
         "Name": 'Beatrice',
         "Age": 29
     }),
     OrderedDict({
         "Name": 'Ceri',
         "Age": 30
     }),
     OrderedDict({
         "Name": 'Dean',
         "Age": 26
     })
 ]

#list comprehension

#3 Save file using save_as()
pyexcel.save_as(records=data, dest_file_name="pyexcel_test.xls")