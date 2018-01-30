from data_provider import Dataprovider

# Load the class
data_provider = Dataprovider()

# Load the properties
numpos = data_provider.num_positive
numneg = data_provider.num_negative
numall = data_provider.num_sequences

print(numpos)
print(numneg)
print(numall)

if numpos + numneg == numall:
    print("approved")


# class_dict = data_provider.i_to_pol
# csv = open('class_dict.csv', "w")
# for key in class_dict.keys():
# 	text_id = key
# 	label = class_dict[key]
#     row = str(text_id) + "," + str(label) + "\n"
#     csv.write(row)
# csv.close()

#data_provider.write_content_to_file()
