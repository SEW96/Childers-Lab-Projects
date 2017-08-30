import csv

single_point = {}
single_point_2 = []
bac_dict = {}
x = ordered_bac_list = []

def main():
    build_indices(single_point, single_point_2)
    organize_by_bacteria(single_point_2)
    organize_bacteria_sequentially(bac_dict)
    with open('data_processer_output.tsv', 'w') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerows(x)


def build_indices(single_point, single_point_2):
    with open ('46_39_A_First_1hr data copy.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = 0
        for row in reader:
            if row[0] != '':
                point = []
                inner_dict = {}
                foci_type = row[0]
                intensity = float(row[1])
                parent = str(row[2])
                point = [parent, intensity, foci_type]

                if (parent, foci_type) in single_point: #finallyworksbitches
                    single_point[parent, foci_type] = str(point[1] + float(single_point[parent, foci_type]))
                    inner_dict[parent] = single_point[parent, foci_type], point[2]
                    single_point_2.pop()
                    single_point_2.append(inner_dict)

                else:
                    single_point[parent, foci_type] = str(float(point[1]))
                    inner_dict[parent] = single_point[parent, foci_type], point[2]
                    single_point_2.append(inner_dict)
            lines += 1
        return lines

def organize_by_bacteria(single_point_2):
    lines = 0
    for subVal in single_point_2:
        bac_list = []
        for key in subVal:
            bac_list.append(subVal[key])
            if key in bac_dict:
                bac_dict[key] = bac_dict[key] + bac_list
            else:
                bac_dict[key] = bac_list
    lines += 1
    return lines

def organize_bacteria_sequentially(bac_dict):
    keylist = bac_dict.keys()
    newkeylist = []
    for key in keylist:
        newkey = int(key[1:])
        newkeylist.append(newkey)
    orderednewkeylist = sorted(newkeylist)
    finalkeylist = []
    for x in orderednewkeylist:
        x = str(x)
        finalkeylist.append('b'+ x)
    lines = 0
    for key in finalkeylist:
        x = key , str(bac_dict[key])
        ordered_bac_list.append(x)
    lines += 1
    return lines
    
main()
