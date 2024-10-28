#Files

#Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 

#Does the new file show up in the directory where you ran your scripts? 
#Ні, з'явився не в піддерикторії з якої я запускав скрипт, а в основній дерикторії, це через те що я не працюю не в Pycharm а в VS code

#What if you add a different directory path to the filename passed to open?
#створить новий файл в каталозі

def create_file():
    with open("myfile.txt", "w") as file:# "w" перезаписує все що є в файлі 
        file.write("Hello file world!\n")
def read_file():
    with open("myfile.txt", "r") as file:
        print(file.read()) 
create_file()
read_file()