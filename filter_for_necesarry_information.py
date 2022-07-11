import numpy as np
import pandas as pd

def read_csv(file_name, extension):
    data = pd.read_csv(file_name + extension)
    return data

def create_address_data_frame(dataframe):
    address = list()
    for row in range(len(dataframe["address"])): 
        country, postal_code, city, other = "", "", "", ""

        row_address = dataframe["address"].iloc[row].split(" - ")

        country = row_address[-1]
        if row_address[-2].isdigit() and len(row_address[-2]) == 4: postal_code = row_address[-2]
        city = row_address[-3]
        other = " - ".join(row_address[:-3])
        row_address = [country, postal_code, city, other]

        address.append(row_address)

    address = pd.DataFrame(address, columns=["Country", "Postal Code", "City", "Building, Street, etc."])

    return address
file_name = "cleaned_tattoo_studios"
extension = ".csv"
data = read_csv(file_name, extension)
address = create_address_data_frame(data)

data = data[["Title", "website", "phoneNumber"]]
data = pd.concat([data, address], axis=1)
data.columns = ['Title', 'Website', 'Phone Number', 'Country', 'Postal Code', 'City', 'Building, Street, etc.']

new_file_name = "tattoo_studios_database"
data.to_csv(new_file_name + extension, index=False)

print("Database COnversion Successful!")