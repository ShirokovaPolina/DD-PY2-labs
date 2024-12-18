import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]  # Используем list comprehension для создания списка

    json_string = json.dumps(data, indent=4)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as outfile:
        outfile.write(json_string)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
            
