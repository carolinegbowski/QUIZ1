import json


def readcurrency(filename):
    currency_data = []
    for line in filename:
        currency_dict = {}
        currency_dict["symbol"] = line[:3] 
        currency_dict["rate"] = float(line[4:].strip())
        currency_data.append(currency_dict)
    return currency_data

with open("currency.txt", "r") as filename:
    currency_data = readcurrency(filename)

def save(filename, data):
    new_data = {}
    new_data["data"] = data
    with open(filename, "w") as json_file:
        json.dump(new_data, json_file, indent=2)

save("quiz.json", currency_data)


