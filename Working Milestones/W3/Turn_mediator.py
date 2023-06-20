import os
import time


time.sleep(0.5) #Adding a delay to make sure the init of the generate is done

def transform_to_percentage(number):
    percentage = number * 20
    return percentage

def count_files_in_directory(directory_path):
    # Check how many files are in a directory
    if not os.path.isdir(directory_path):
        return "Error: Invalid directory path"

    file_count = 0
    for _, _, files in os.walk(directory_path):
        file_count += len(files)

    return file_count

def loading_screen(file_count):
    progress = min(file_count, 5)
    percentage = transform_to_percentage(progress)
    loading_bar = "[" + "#" * progress + " " * (5 - progress) + "]"
    print(f"Loading: {percentage}% {loading_bar}")

previous_count = 0

tour =0 #le fichier qui sera lue

print("\nLoading:  0% [    ]")
while True:
    current_count = count_files_in_directory("discussion")

    if current_count > 5:

        if (tour) % 2 == 0:
            gender = "m"
        else:
            gender = "f"
        os.system(f'powershell.exe -command .\display_console.ps1 discussion\{tour}.txt {gender}')
        os.system(f'powershell.exe -command .\Reader.ps1 {tour} {gender}')
        tour +=1

    elif current_count != previous_count:
        loading_screen(current_count)
        previous_count = current_count
