
import os 
import shutil

def get_extension(file_name):
  
  reverse_filename = file_name[::-1]
  
  aux = 0

  for i in reverse_filename:

    if i != ".":

        aux += 1
    
    else:
       
       break

  return file_name[len(file_name)-aux:len(file_name)]


directory_path = input("directory that you want to organize: \n")

filenames = os.listdir(directory_path)

for file in filenames:
   
   file_extension = ""
   
   if os.path.isdir(directory_path+"/"+file) == False:
    
    file_extension = get_extension(file)

    if (os.path.isdir(directory_path+"/"+file_extension) == False) and file_extension != file:
         
        try:

            os.makedirs(os.path.join(directory_path, file_extension), exist_ok = True)
        
        except OSError as e:
            
            print(f"effor creating folder {e}")

    if file_extension != file:

        try:

            shutil.move((directory_path+"/"+file),(directory_path+"/"+file_extension+"/"+file))

        except OSError as e:

            print(f"Error moving file {e}")
           
           

         

         
         


   
  

