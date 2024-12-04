import os
import shutil

def delete_folder_contents(folder_path):
    """
    Deletes all files and folders within the specified folder.

    :param folder_path: Path to the folder whose contents need to be deleted
    """
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Iterate through each item in the folder
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)

        # Check if it's a file or folder and remove it accordingly
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Remove file or symbolic link
                # print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove directory
                # print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Failed to delete '{item_path}'. Reason: {e}")

# Example usage
def delete_multiple_folders(folder_paths):
    """
    Deletes contents of multiple folders.

    :param folder_paths: List of folder paths to clean
    """
    for folder_path in folder_paths:
        # print(f"Cleaning folder: {folder_path}")
        delete_folder_contents(folder_path)

folders_to_clean = ["usr_processed/", "txt_files/bulk_USRs_mod"]
delete_multiple_folders(folders_to_clean)
