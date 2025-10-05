from pathlib import Path
import shutil


class sorter:
    def __init__(self, path : str, categories):
        self.path = Path(path)
        self.categories = categories

    def sort(self):
        folder = self.path
        files = []

        try:
            for file in folder.iterdir():
                if file.is_file():
                    files.append(file)
                    print(f"{file} Append to files!")

            other_folder = folder / "Other"
            other_folder.mkdir(parents=True, exist_ok=True)

            for file in files:
                moved = False
                for category, extensions in self.categories.items():
                    if file.suffix.lower() in extensions:
                        temp = folder / category

                        temp.mkdir(parents=True, exist_ok=True)
                        print(f"{category} Folder was created!")

                        shutil.move(str(file), str(temp / file.name))
                        print(f"{file.name} Moved to {temp}!")

                        moved = True
                        break

                if not moved:
                    new_path = other_folder / file.name
                    shutil.move(str(file), str(new_path))
                    print(f"{file.name} Moved to Other!")

            print("Sorting was successful!")

        except FileNotFoundError:
            print("Source file was not found.")
        except PermissionError:
            print("Lack of permission to move the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
