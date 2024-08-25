csv_filepathname="output.csv" # Full path to your django project directory 
your_djangoproject_home="F:/projects/restproj/webapp/" 
import sys,os 
sys.path.append(your_djangoproject_home) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'restproj.settings' 
from webapp.models import GetTagCode 
import csv 
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
for row in dataReader:
        TagCodeinst=GetTagCode() 
        TagCodeinst.TagCode = row[0] 
        TagCodeinst.Labels = row[1]  
        TagCodeinst.save()
        