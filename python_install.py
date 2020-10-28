import pandas as pd
import xlrd
import subprocess 
import sys as platform
#df = pd.read_excel ('product_model.xlsx')
#print (df)c
import pandas as pd

data = pd.read_excel(r'Product_Model1.xlsx', sheet_name='VersionDetail') 
df = pd.DataFrame(data, columns= ['CreatedBy', 'CreatedDate', 'ModifiedDate', 'ModifiedBy',	'AutoScheduleFrequency', 'VunerabilityScanFrequency', 'LastScannedDate', 'SourceUrl', 'Bit', 'DiscoverType', 'Platform', 'FileFormat',	'VersionPattern', 'VersionID', 'VerionNumber', 'ExternalRef', 'VulnerabilityScanRef', 'LicensingScanREf'
], dtype=str,)


df.head()

for row in df['SourceUrl']:
    print("row is---->",row)
    if platform == "linux" or platform == "linux2":
        print("Linux")
        dirName="/home/prince"
        subprocess.call(f"wget {row}", shell=True, cwd=dirName)
 
    elif platform == "win64":
        print("Windows")
        dirName="C:\\Users\\"
        subprocess.call(f"wget {row}", shell=True, cwd=dirName)

    
    dirName="E:\TCS_Doc\Python"
    subprocess.call(f"wget {row}", shell=True, cwd=dirName)





