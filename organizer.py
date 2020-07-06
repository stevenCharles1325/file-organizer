'''
	This program organize files in your current directory by moving them to their designated folder

'''
import os 
import shutil

def split_names_and_extension(files):
	'''
		split the filename and its file extension and store them in an array
		
		EX:
			filename : sample.txt
			output	 : ('sample', '.txt')
	'''
	files_info = []
	for file in files:
		files_info.append(os.path.splitext(file))
	return files_info

def move_files(files):
	'''
		Algorithm for organizing the file.
		1.) Loop through all files
		2.) Check if the current file type is not a folder.
		3.) If in the dictionary named CREATED_FOLDER's key has a file named by its extension then just append the file.
		4.) Else create an item in the dictionary and named it with its file extension then also create an actual folder for the file
	'''
	created_folders = {}
	
	for filesName, extension in files:

		if os.path.isfile(filesName+extension): # check if it is a file not a folder
			
			if extension[1:] in created_folders.keys(): # check if that folder named by its file extension (without "dot") already exist. If it is then add the file
				created_folders[extension[1:]].append(filesName+extension)
				shutil.move(('./'+filesName+extension), ('./'+extension[1:]))

			else:	# else create a folder and name it by its file extension (without "dot")
				created_folders[extension[1:]] = []
				created_folders[extension[1:]].append(filesName+extension)

				os.makedirs(extension[1:])
				shutil.move(('./'+filesName+extension), ('./'+extension[1:]))

def organize():
	path = os.getcwd()	# get current directory
	files = os.listdir(path) # list all files 
	move_files(split_names_and_extension(files))

if __name__ == '__main__':
	print('ORGANIZING FILES..')
	organize()
	print('FINISHED')
