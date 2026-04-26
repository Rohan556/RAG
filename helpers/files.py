import glob

def get_all_files_from_directory(base_path):
    files = glob.glob(f"{base_path}/**/*.*", recursive=True)
    return files

def combine_files(files):
    entire_knowlege_base = ""
    for filepath in files:
        with open(filepath, 'r', encoding="utf-8") as f:
          entire_knowlege_base += f.read()
          entire_knowlege_base += "\n\n"

    return entire_knowlege_base  