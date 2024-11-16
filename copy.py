import os
import shutil

def copy_contents(src_folder, dest_folder):
    """
    Copy all contents from src_folder to dest_folder.
    """
    try:
        for item in os.listdir(src_folder):
            src_item = os.path.join(src_folder, item)
            dest_item = os.path.join(dest_folder, item)
            if os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item)
            else:
                shutil.copy2(src_item, dest_item)
        print(f"Copied contents from '{src_folder}' to '{dest_folder}'.")
    except Exception as e:
        print(f"Error copying from '{src_folder}' to '{dest_folder}': {e}")

def traverse_and_copy(base_folder):
    """
    Traverse all directories starting from base_folder.
    For any directory, if it contains multiple subdirectories,
    copy contents from a non-empty subdirectory to an empty one.
    """
    for root, dirs, _ in os.walk(base_folder):
        # Find all subdirectories in the current directory
        # print(dirs)
        subdirs = [os.path.join(root, d) for d in dirs]
        if len(subdirs) < 2:
            continue  # Need at least two subdirectories to proceed

        # Separate empty and non-empty subdirectories
        empty_dirs = [d for d in subdirs if not os.listdir(d)]
        non_empty_dirs = [d for d in subdirs if os.listdir(d)]

        # Copy contents from a non-empty directory to an empty one
        if empty_dirs and non_empty_dirs:
            src_folder = non_empty_dirs[0]
            for dest_folder in empty_dirs:
                print(f"Copying from '{src_folder}' to empty folder '{dest_folder}'...")
                copy_contents(src_folder, dest_folder)
        else:
            print(f"No matching directories to copy in '{root}'.")

# Example usage
base_folder = "./"  # この経路を実際のルートディレクトリ経路に置き換え
traverse_and_copy(base_folder)
