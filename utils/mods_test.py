import numpy
import pandas
from pymods import MODSReader, MODSRecord

mods_file = "../samplefiles/digibok_sample.mods"
mods = MODSReader(mods_file)


#for record in mods:
#    for child in record.iterdescendants():
#        print(child.tag)


#for record in mods:
#    print(record.dates)


for record in mods:
    for name in record.names:
        #author
        if name.role.code == "aut":
            print(f'Author: {name.elem[0].text}')
       
        if name.role.code == "trl":
            print(f'Translator: {name.elem[0].text}')



