import os
import shutil

def move_files_with_number(source_dir, target_dir, number):
    """
    Move files containing the specified number from the source directory to the target directory.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    files_moved = 0
    for filename in os.listdir(source_dir):
        if str(number) in filename:
            src_path = os.path.join(source_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            shutil.move(src_path, dst_path)
            files_moved += 1
    print(f"{files_moved} files moved containing the number {number}.")

def clear_directory(source_dir, target_dir):
    """
    Move all files from the source directory back to the target directory.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    files_moved = 0
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, filename)
        shutil.move(src_path, dst_path)
        files_moved += 1
    print(f"{files_moved} files moved back to the archive.")

def main():
    archive_dir = "/home/mjm/egs_brachy/eb_GUI/database/dose_archive"
    dose_dir = "/home/mjm/egs_brachy/eb_GUI/database/dose"
    
    while True:
        command = input("Enter a number to move files, or type 'clr' to clear the dose directory: ").strip()
        if command == 'clr':
            clear_directory(dose_dir, archive_dir)
        elif command.isdigit():
            move_files_with_number(archive_dir, dose_dir, command)
        else:
            print("Invalid input. Please enter a number or 'clr'.")

if __name__ == "__main__":
    main()
