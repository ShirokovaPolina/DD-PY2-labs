import json

def task() -> float:
    json_file_path = 'input.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    total_sum = sum(item.get("score", 0) * item.get("weight", 0) for item in data)
    return round(total_sum, 3)

print(task())
