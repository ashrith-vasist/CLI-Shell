import cmd
import os
import subprocess
path=os.getcwd()


class MyCommand(cmd.Cmd):
    
    # Gets the return value from update_prompt() and updates the value
    def __init__(self):
        super().__init__()
        self.prompt = self.update_prompt()

    #Update the prompt to the new directory !!    
    def update_prompt(self):
        return f"AshShell:{os.getcwd()}$ "

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
        
        path = os.getcwd()
        files = os.listdir(path)

        if dir_name == "..":
            parent_dir = os.path.dirname(path)
            os.chdir(parent_dir)
        elif dir_name not in files:
            print("No such directory present")
        else:
            os.chdir(dir_name)
        self.prompt = self.update_prompt() #calls the update_promtp function everytime it travers
    
    def do_cat(self,file_name):
        """give the contents of the file"""
        path=os.getcwd();
        files=os.listdir(path)
        if(file_name in files):
            with open(file_name,'r') as f:
                print(f.read())
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

    
    # This function is ambigous still needs work
    # def do_vi(self,file_name):
    #     """opens a file"""
    #     if os.path.isfile(file_name):
    #         with open(file_name, "r") as file:
    #             content = file.read()
    #             print(content)
    #             while True:
    #                 new_content = input("Enter new content (or 'save' to save and exit): ")
    #                 if new_content.lower() == 'save':
    #                     with open(file_name, "w") as f:
    #                         f.write(content)
    #                     break
    #                 content += new_content + '\n'
    #     else:
    #         print("No such file exists")
        
    def do_vi(self,file_name):
        if os.path.isfile(file_name):
            subprocess.run(["vi",file_name])
        else:
            print("No such file exists")

    def do_clear(self,arg):
        os.system("clear")

    
    
    def do_rm(self,file_name):
        path=os.getcwd();
        files=os.listdir(path)
        if(file_name in files):
            os.remove(file_name)
        else:
            print("No such file exits")
    
    def do_rmdir(self,dirname):
        path=os.getcwd()
        dirn=os.listdir(path)
        if(dirname in dirn):
            os.rmdir(dirname)
        else:
            print("Directory does not exits")
    def emptyline(self):
        pass
###
#Have to add piping

cli = MyCommand()      
#cli.update_prompt()
cli.cmdloop()
