import src, os, pyfiglet


os.system('cls' if os.name == 'nt' else 'clear')

print(pyfiglet.figlet_format("FileSorter", font="ansi_shadow"))

path = str(input("Enter the path to the folder you want to sort: "))

if __name__ == "__main__":
    try :
        config = src.config_loader(path="data/config.json")
        categories = config.load()

        sorter = src.sorter(path=path, categories=categories)
        sorter.sort()

    except Exception as e:
        print(f"An error occurred: {e}")

os.system('pause')


