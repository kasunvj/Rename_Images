import xml.etree.ElementTree as ET
from glob import glob
import shutil
import os
import logging

#logging.basicConfig(filename='renamelog.log',filemode ='w', format = '%(asctime)s - %(message)s', level= logging.INFO)
logging.basicConfig(level = logging.INFO)

inputFolder = 'D:/Projects/Research_Project/tf_object_detector_api_3_ssd/images/New folder/*'
fileTypes = ['*.png','*.jpg']
startNumber = 34


outputFolder = "D:/Projects/Research_Project/tf_object_detector_api_3_ssd/images/New folder/output/"
try :
	os.mkdir(outputFolder)
except FileExistsError:
	logging.warning('File Exist error')

c = startNumber;

for i in range(len(fileTypes)):
	imagefiles = glob(inputFolder + fileTypes[i])

	for file in imagefiles:
		shutil.copy(file, outputFolder)
		logging.info(os.path.basename(file)+" "+"copied")

renamefiles = glob(outputFolder+'/*')

for file2 in renamefiles:
	logging.info(os.path.basename(file2)+' renamed')
	if c<10 :
		os.rename (file2,outputFolder+'/'+'0'+str(c)+'.jpg')
	else :
		os.rename (file2,outputFolder+'/'+str(c)+'.jpg')
	c = c + 1


		


	
	


