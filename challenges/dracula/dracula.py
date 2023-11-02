def main():
    count = 0
    with open(
        "/home/student/mycode/challenges/dracula/dracula.txt", encoding="utf-8"
    ) as file:
        for line in file:
            if "vampire" in line.lower():
                print(line, end="")
                count += 1

    print(f"\nThe number of lines that contain 'vampire' are: {count}")


if __name__ == "__main__":
    main()
