import requests
from rembg import remove


def remove_background_from_url(input_url, output_filename):
    try:
        response = requests.get(input_url)
        input_data = response.content
        output_data = remove(input_data)
        with open(output_filename, 'wb') as o:
            o.write(output_data)
        print(f"\nBackground removed --> {output_filename}\n")
    except requests.RequestException:
        print(
            "\nAn error occurred while trying to remove the background. Please check your URL or connection then try "
            "again.\n")


def remove_background_from_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as i:
            input_data = i.read()
            output_data = remove(input_data)
            with open(output_filename, "wb") as o:
                o.write(output_data)
            print(f"\nBackground removed --> {output_filename}\n")
    except FileNotFoundError:
        print("\nFile not found. Please check your file path and try again.\n")


def main():
    while True:
        print("1-Remove the background from an image URL")
        print("2-Remove the background from a local file")
        print("3-Exit")
        answer = input("\nEnter your choice (1,2 or 3): ")

        if answer == "1":
            input_url = input("Enter the image URL: ")
            output_filename = input("Enter the output file name (e.g., output.png): ")
            remove_background_from_url(input_url, output_filename)
        elif answer == "2":
            input_filename = input("Enter the input file name (e.g., image.jpg): ")
            output_filename = input("Enter the output file name (e.g., output.png): ")
            remove_background_from_file(input_filename, output_filename)
        elif answer == "3":
            exit()
        else:
            print("\nInvalid choice. Please enter 1, 2 or 3.\n")


if __name__ == "__main__":
    main()
