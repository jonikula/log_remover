import datetime
import os

def getFiles(path):
        files = os.listdir(path) #Get a list of files in the path
        return files

def checkDates(filelist, date):
        list = []
        for filename in filelist:
                if (date.day == 28): #Run the script on 28th and 15th
                        moddate = os.path.getmtime(filename)
                        if datetime.datetime.fromtimestamp(moddate).day <= 15:
                                list.append(filename) #Add over 2 weeks old files to the list
								
                elif (date.day == 15):
                        moddate = os.path.getmtime(filename)
                        if datetime.datetime.fromtimestamp(moddate).day > 15:
                                list.append(filename)
        return list #Return the list

def remover(files):
        size = 0
        for filename in files:
                size = size + os.path.getsize(str(filename)) #Store the file sizes before removing
                os.remove(str(filename)) #Remove files
        return size #Return stored file size

def writer(stuff):
		f = open('CLEANER_LOG', 'a')
		f.write(stuff + '\n') #Write stuff to file
		f.close()
		return 0
        
		
def main():
        path = "D:\\teamspeak3-server_win32\\logs"
        os.chdir(path) #Change working directory
        date = datetime.datetime.now() #Get current date
        files = getFiles(path) 
        removefiles = checkDates(files, date)
        size = remover(removefiles)
        log = str(len(removefiles)) + " files (" + str(size) + " bytes) removed on " + str(date) #Write log
        writer(log)
        return 0
main()
	
	
	
		
	
