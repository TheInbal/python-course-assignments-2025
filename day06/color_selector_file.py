

def load_colors_from_file(file_path):
    with open(file_path, 'r') as file:
        colors = [line.strip() for line in file if line.strip()]
    return colors


def main():
    file_path = "C:/Inbal/University/Chemistry Msc Weizmann/Courses/Python Course/day06/colors.txt"

    colors = load_colors_from_file(file_path)

    if not colors:
        return

    print("Available colors:")
    for color in colors:
        print(f"- {color}")

    selected = input("Please type a color from the list above: ").strip().lower()

    if selected in [c.lower() for c in colors]:
        print(f"Selected: {selected}")
    else:
        print("Your choice is not in the list.")

if __name__ == "__main__":
    main()
