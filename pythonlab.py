import random
import os


def generate_random_integers():
    return [random.randint(1, 300) for _ in range(100)]


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, data)))


def read_and_display_sorted_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            data = list(map(int, data))
            sorted_data = sorted(data)
            print(f"Sorted data: {sorted_data}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    filename = input("Enter the filename: ")

    # Check if the file already exists
    if not os.path.exists(filename):
        random_integers = generate_random_integers()
        write_to_file(filename, random_integers)
        print(f"Data has been written to '{filename}'.")
    else:
        print(f"The file '{filename}' already exists. It will not be overridden.")

    # Read and display sorted data from the file
    read_and_display_sorted_data(filename)


if __name__ == "__main__":
    main()
