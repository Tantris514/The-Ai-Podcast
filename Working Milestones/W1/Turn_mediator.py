import os

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


while True:
    current_count = count_files_in_directory("discussion")

    if current_count > 5:

        if (tour) % 2 == 0:
            gender = "m"
        else:
            gender = "f"
        print(gender)
        os.system(f'powershell.exe -command .\Reader.ps1 {tour} {gender}')
        tour +=1

    elif current_count != previous_count:
        os.system("cls")
        loading_screen(current_count)
        previous_count = current_count
