import cmd
import os
#print(dir(cmd.Cmd))
class MyCommand(cmd.Cmd):
    prompt = "(AshTheGr8t)>>>"
    def do_exit(self,arg):
        """helps to quit CLI"""
        print("Bye bye")
        return True
    do_quit=do_exit
    def do_pwd(self,arg):
        """gives the path of the current directory"""
        path=os.getcwd()
        print(path)
    def do_ls(self,arg):
        """list of files and folders present in the directory"""
        path=os.getcwd()
        files=os.listdir(path)
        for x in files:
            print(x)
    def do_cd(self,dir_name):
        """To traverse through directories"""
        path=os.getcwd()
        files=os.listdir(path)
        if(dir_name not in files):
            print("No such directory present")
        else:
            os.chdir(dir_name)
        
    
    def do_cat(self,file_name):
        """give the contents of the file"""
        path=os.getcwd();
        files=os.listdir(path)
        if(file_name in files):
            c=open(file_name,'r')
            print(str(c))
        else:
            print("No such file exists")
    
    def do_mkdir(self,dic_name):
        """creates a directory"""
        path=os.getcwd()
        p=os.path.join(path,dic_name)
        os.mkdir(p)
    
    def do_touch(self,file_name):
        """creates a file"""
        f=open(file_name,"x") 
    
    def do_vi(self,file_name):
        """opens a file"""
        path=os.getcwd()
        files=os.listdir()
        if(file_name in files):
            f=open(file_name,"a")
        else:
            print("No such file exits")

    #To do in the prjct 
    #def do_clear(self,arg)
    #def do_rm(self,args)
    #give path to cd
    #enhance vi functianlity
        
MyCommand().cmdloop()