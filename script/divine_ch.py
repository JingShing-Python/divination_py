import random

def read_txt_file(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(' ', 1)
                data[key] = value
    return data

def random_selection(data, num_selections):
    keys = list(data.keys())
    selected = random.sample(keys, num_selections)
    return {key: data[key] for key in selected}

txt_file_path = 'card.txt'

data = read_txt_file(txt_file_path)

num_selections = int(input("請輸入要抽取的數量: "))

selected_data = random_selection(data, num_selections)

sorted_data = sorted(selected_data.items(), key=lambda x: int(x[0]))

print("隨機抽取結果:")
for key, value in sorted_data:
    print(f"{key}: {value}")

print("隨機抽取結果:")
output = ""
for key, value in sorted_data:
    output += f"{key} {value}, "
output = output.rstrip(", ")
print(output)
