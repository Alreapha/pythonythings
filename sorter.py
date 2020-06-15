import os
import glob
print("I'm ALIVE!")
Counter = 0
SRCDIR = input(r"Source Directory: ") + "\*"
FileSize = input("Minimum File Size(In Bytes!): ")
for files in glob.glob(SRCDIR):
	print(files)
	Size = os.stat(files).st_size
	try:
		if Size < int(FileSize):
			os.remove(files)
			print("File Removed")
			Counter = Counter + 1
		else:
			print("1KB +")
	except:
		print("IDK what happened...")
print(Counter)

#this fails on a few things but IDC it works for the most part.