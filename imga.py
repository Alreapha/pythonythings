import glob
import shutil
print("PYTHON!")
SourceLoc1 = r"C:\*"
SourceLoc = r"D:\*"
DestLoc = r"E:\HERE"
FileType = ".png"
FileType1 = ".jpg"
import os
DestLoc = input("To Here: " +"/")
logg = open("Log.txt","a+")
print(SourceLoc + "\*" + FileType)
counter = 0
Diran = 0
Dira = ["\*","\*\*","\*\*\*","\*\*\*\*","\*\*\*\*\*\*","\*\*\*\*\*\*","\*\*\*\*\*\*\*","\*\*\*\*\*\*\*"]

while Diran < 8:
	loc1 = SourceLoc + Dira[Diran] + FileType
	loc2 = SourceLoc + Dira[Diran] + FileType1
	loc3 = SourceLoc1 + Dira[Diran] + FileType
	loc4 = SourceLoc1 + Dira[Diran] + FileType1
	
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	print(Diran)
	
	try:
		for file in glob.glob(loc1):
			print(file)
			logg.writelines(file + '\n')
			shutil.copy(file, DestLoc + "/" + str(counter) + FileType)
			counter = counter + 1
	except:
		print("Failed")
	try:
		for file in glob.glob(loc2):
			print(file)
			logg.writelines(file + '\n')
			shutil.copy(file, DestLoc + "/" + str(counter) + FileType1)
			counter = counter + 1
	except:
		print("Failed")
	try:
		for file in glob.glob(loc3):
			print(file)
			logg.writelines(file + '\n')
			shutil.copy(file, DestLoc + "/" + str(counter) + FileType)
			counter = counter + 1
	except:
		print("Failed")
	try:
		for file in glob.glob(loc4):
			print(file)
			logg.writelines(file + '\n')
			shutil.copy(file, DestLoc + "/" + str(counter) + FileType1)
			counter = counter + 1
	except:
		print("Failed")
	Diran = Diran + 1
print(counter)

#Yes, I know it's messy
#No, I don't care.
#It works, what more do you want?