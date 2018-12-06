
import json
import csv
import sys

def json_to_csv(input_, output):
    """."""
    with open(input_) as inputfile:
        jsondata = json.load(inputfile)
        header = max([item.keys() for item in jsondata])
        data = [{key: item.get(key) for key in header} for item in jsondata]
        print(data)
        with open(output , 'w') as outputfile:
            csvwriter = csv.DictWriter(outputfile, fieldnames=header)
            csvwriter.writeheader()
            csvwriter.writerows(data)

input_, output = sys.argv[1], sys.argv[2]
json_to_csv(input_, output)

