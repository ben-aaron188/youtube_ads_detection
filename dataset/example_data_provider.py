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
