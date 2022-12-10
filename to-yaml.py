# Convert landmarks.csv from CSV to YAML format

import csv, yaml

data_file = "landmarks.csv"

landmarks_list = []

with open(data_file, 'rt') as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    next(reader)  # skip header
    for row in reader:
        country = row[0]
        type = row[1]
        name = row[2]
        city = row[3]
        comment = row[4]
        landmarks_list.append(
                {
                    'country' : country,
                    'type' : type,
                    'name' : name,
                    'city' : city,
                    'comment' : comment,
                 }
                )

with open('landmarks.yaml', 'w') as file:
    output_file = yaml.dump(landmarks_list, file, allow_unicode=True)
