import csv

def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

empty_dict = {}  
empty_list = []
fieldnames = ['Symbol', 'Ukey', 'Qty', 'MarketVolume', 'MarketShare']
f_ob = open("20140923_MarketVolume.csv")
f_obj = open("20140923_MarketShare.csv")
reade = csv.DictReader(f_ob, delimiter=',')
reader = csv.DictReader(f_obj, delimiter=',')
path = "result.csv"
errors = 0

for line in reade:
 		a = line["UKey"]
 		b = line["Volume"]
 		empty_dict[a] = b

for line in reader:
 	empty_list.append(line)

for i in empty_list:
	h = i["Ukey"]
	
	try:
		i["MarketVolume"] = empty_dict[h] 
	
	except:
		errors += 1

print errors, "errors"

csv_dict_writer(path, fieldnames, empty_list)
