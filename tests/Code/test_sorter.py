from pathlib import Path
files = []

folder = Path("D:/My projects/FileSorter/tests/test1")
for file in folder.iterdir():
    if file.is_file():
        files.append(file)

for i in files :
    print(i) 

    