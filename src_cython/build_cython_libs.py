import os
import shutil
from pathlib import Path

if __name__=="__main__":
    current_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_path)
    print("Working directory: ", current_path)
    os.system("python setup.py build_ext --inplace")
    # find build pyd files
    for file in os.listdir(current_path):
        src_file = os.path.join(current_path, file)
        if file.endswith(".pyd") or file.endswith(".so"):
            print("Parent Folder:", os.path.abspath(current_path))

            dest_file=Path(current_path).parent.absolute()
            project_name=os.path.basename(dest_file)
            print("Project Name: ",project_name)
            dest_file=os.path.join(dest_file,'src',project_name,"libs",file)
            print("dest_file: ",dest_file)
            shutil.copy(src_file,dest_file)
