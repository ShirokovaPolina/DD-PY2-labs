import json


def task() -> float:
    json_file_path = 'input.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    total_sum = 0.0
    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total_sum += score * weight
    return round(total_sum, 3)


print(task())
