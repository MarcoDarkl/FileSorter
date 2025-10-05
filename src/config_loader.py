import json

class config_loader:
    def __init__(self, path : str):
        self.path = path 

    def load(self):
        try :
            with open(self.path, "r", encoding="utf-8") as f:

                print("Config loaded successfully!")

                return json.load(f)
            
        except FileNotFoundError:
            print("The file was not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON - invalid file format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")