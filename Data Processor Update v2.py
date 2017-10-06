import csv

#Enter the name of your data file here, must be an Excel CSV file
FILE = '46_39_41 Raw data'

single_point = {}
single_point_2 = []
bac_dict = {}
x = ordered_bac_list = []

def main():
    build_indices(single_point, single_point_2)
    organize_by_bacteria(single_point_2)
    organize_bacteria_sequentially(bac_dict)
    type_separation(ordered_bac_list)
    with open('data_processer_output.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['Total Bacterial Data Set: '])
        writer.writerows(x)
        writer.writerow(['Total Number of bacteria: ', lines])
        writer.writerow(['Single entry fluorescence: '])
        writer.writerows(a)
        writer.writerow(['Number of bacteria: ', one_count])
        writer.writerow(['Two entry fluorescence: '])
        writer.writerows(b)
        writer.writerow(['Number of bacteria: ', two_count])
        writer.writerow(['Three entry fluorescence: '])
        writer.writerows(c)
        writer.writerow(['Number of bacteria: ', three_count])
        writer.writerow(['Four entry fluorescence: '])
        writer.writerows(d)
        writer.writerow(['Number of bacteria: ', four_count])
        writer.writerow(['Five entry fluorescence: '])
        writer.writerows(e)
        writer.writerow(['Number of bacteria: ', five_count])
        print('Finished, look for data_processer_output file.')

def build_indices(single_point, single_point_2):
    with open ('{}.csv'.format(FILE)) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = 0
        for row in reader:
            if lines >= 3 and row[0] != '':
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
    global lines
    lines = 0
    for key in finalkeylist:
        x = key , str(bac_dict[key])
        ordered_bac_list.append(x)
        lines += 1
    return lines

def type_separation(ordered_bac_list):
    global a
    global b
    global c
    global d
    global e
    global one_count
    global two_count
    global three_count
    global four_count
    global five_count
    a = one_entry = []
    b = two_entry = []
    c = three_entry = []
    d = four_entry = []
    e = five_entry = [] 
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    for row in ordered_bac_list:
        for item in row:
            bacteria = row[0]
            rest = row[1]
            length = len(rest)
            #one entry fluorescence 
            if length <= 30: 
                bac_list1 = []
                for entry in one_entry:
                    bac1 = entry[0]
                    bac_list1.append(bac1)
                if bacteria not in bac_list1:
                    one_entry.append(row)
                    one_count +=1
            #two entry fluorescence
            elif length <= 70:
                bac_list2 = []
                for entry in two_entry:
                    bac2 = entry[0]
                    bac_list2.append(bac2)
                if bacteria not in bac_list2:
                    two_entry.append(row)
                    two_count += 1
            #three entry fluorescence
            elif length <=100:
                bac_list3 = []
                for entry in three_entry:
                    bac3 = entry[0]
                    bac_list3.append(bac3)
                if bacteria not in bac_list3:
                    three_entry.append(row)
                    three_count += 1
            #four entry fluorescence
            elif length <= 130:
                bac_list4 = []
                for entry in four_entry:
                    bac4 = entry[0]
                    bac_list4.append(bac4)
                if bacteria not in bac_list4:
                    four_entry.append(row)
                    four_count += 1
            #five entry fluorescence
            else:
                bac_list0 = []
                for entry in five_entry:
                    bac0 = entry[0]
                    bac_list0.append(bac0)
                if bacteria not in bac_list0:
                    five_entry.append(row)
                    five_count += 1
    return(a,b,c,d,e)
    return(one_count, two_count, three_count, four_count, five_count)

    
main()
