import os

def main():
    i = 1
    path = r"C:\Users\amsal\Desktop\pics"

    for filename in os.listdir(path):
        my_dest = f"lion{i}.jpg"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest)

        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()
