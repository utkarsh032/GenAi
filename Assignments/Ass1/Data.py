import csv
import os
import pandas as pd

data = [
    {"State Name": "Andhra Pradesh", "Popular Food": "Pulihora", "Population": "49,386,799", "Land Area": "162,968 km²", "Capital City": "Amaravati", "Gender Ratio": "993"},
    {"State Name": "Arunachal Pradesh", "Popular Food": "Thukpa", "Population": "1,383,727", "Land Area": "83,743 km²", "Capital City": "Itanagar", "Gender Ratio": "938"},
    {"State Name": "Assam", "Popular Food": "Masor Tenga", "Population": "35,607,039", "Land Area": "78,438 km²", "Capital City": "Dispur", "Gender Ratio": "958"},
    {"State Name": "Bihar", "Popular Food": "Litti Chokha", "Population": "104,099,452", "Land Area": "94,163 km²", "Capital City": "Patna", "Gender Ratio": "918"},
    {"State Name": "Chhattisgarh", "Popular Food": "Chana Samosa", "Population": "25,545,198", "Land Area": "135,191 km²", "Capital City": "Raipur", "Gender Ratio": "991"},
    {"State Name": "Goa", "Popular Food": "Fish Curry", "Population": "1,458,545", "Land Area": "3,702 km²", "Capital City": "Panaji", "Gender Ratio": "973"},
    {"State Name": "Gujarat", "Popular Food": "Dhokla", "Population": "60,439,692", "Land Area": "196,024 km²", "Capital City": "Gandhinagar", "Gender Ratio": "919"},
    {"State Name": "Haryana", "Popular Food": "Bajra Khichdi", "Population": "25,351,462", "Land Area": "44,212 km²", "Capital City": "Chandigarh", "Gender Ratio": "879"},
    {"State Name": "Himachal Pradesh", "Popular Food": "Dham", "Population": "6,864,602", "Land Area": "55,673 km²", "Capital City": "Shimla", "Gender Ratio": "972"},
    {"State Name": "Jharkhand", "Popular Food": "Rugra", "Population": "32,988,134", "Land Area": "79,716 km²", "Capital City": "Ranchi", "Gender Ratio": "948"},
    {"State Name": "Karnataka", "Popular Food": "Bisi Bele Bath", "Population": "61,095,297", "Land Area": "191,791 km²", "Capital City": "Bangalore", "Gender Ratio": "973"},
    {"State Name": "Kerala", "Popular Food": "Appam", "Population": "33,406,061", "Land Area": "38,863 km²", "Capital City": "Thiruvananthapuram", "Gender Ratio": "1084"},
    {"State Name": "Madhya Pradesh", "Popular Food": "Poha", "Population": "72,626,809", "Land Area": "308,245 km²", "Capital City": "Bhopal", "Gender Ratio": "931"},
    {"State Name": "Maharashtra", "Popular Food": "Vada Pav", "Population": "112,374,333", "Land Area": "307,713 km²", "Capital City": "Mumbai", "Gender Ratio": "929"},
    {"State Name": "Manipur", "Popular Food": "Eromba", "Population": "2,855,794", "Land Area": "22,327 km²", "Capital City": "Imphal", "Gender Ratio": "985"},
    {"State Name": "Meghalaya", "Popular Food": "Jadoh", "Population": "2,966,889", "Land Area": "22,429 km²", "Capital City": "Shillong", "Gender Ratio": "989"},
    {"State Name": "Mizoram", "Popular Food": "Bai", "Population": "1,097,206", "Land Area": "21,081 km²", "Capital City": "Aizawl", "Gender Ratio": "976"},
    {"State Name": "Nagaland", "Popular Food": "Bamboo Shoot", "Population": "1,978,502", "Land Area": "16,579 km²", "Capital City": "Kohima", "Gender Ratio": "931"},
    {"State Name": "Odisha", "Popular Food": "Pakhala Bhata", "Population": "41,974,218", "Land Area": "155,707 km²", "Capital City": "Bhubaneswar", "Gender Ratio": "979"},
    {"State Name": "Punjab", "Popular Food": "Makki di Roti and Sarson da Saag", "Population": "27,743,338", "Land Area": "50,362 km²", "Capital City": "Chandigarh", "Gender Ratio": "895"},
    {"State Name": "Rajasthan", "Popular Food": "Dal Baati Churma", "Population": "68,548,437", "Land Area": "342,239 km²", "Capital City": "Jaipur", "Gender Ratio": "928"},
    {"State Name": "Sikkim", "Popular Food": "Momos", "Population": "610,577", "Land Area": "7,096 km²", "Capital City": "Gangtok", "Gender Ratio": "890"},
    {"State Name": "Tamil Nadu", "Popular Food": "Idli", "Population": "72,147,030", "Land Area": "130,058 km²", "Capital City": "Chennai", "Gender Ratio": "996"},
    {"State Name": "Telangana", "Popular Food": "Hyderabadi Biryani", "Population": "35,193,978", "Land Area": "112,077 km²", "Capital City": "Hyderabad", "Gender Ratio": "988"},
    {"State Name": "Tripura", "Popular Food": "Mui Borok", "Population": "3,673,917", "Land Area": "10,486 km²", "Capital City": "Agartala", "Gender Ratio": "960"},
    {"State Name": "Uttar Pradesh", "Popular Food": "Tunde Kabab", "Population": "199,812,341", "Land Area": "243,286 km²", "Capital City": "Lucknow", "Gender Ratio": "912"},
    {"State Name": "Uttarakhand", "Popular Food": "Kafuli", "Population": "10,086,292", "Land Area": "53,483 km²", "Capital City": "Dehradun", "Gender Ratio": "963"},
    {"State Name": "West Bengal", "Popular Food": "Rosogolla", "Population": "91,276,115", "Land Area": "88,752 km²", "Capital City": "Kolkata", "Gender Ratio": "950"},
]

filename = "states_of_india.csv"
fieldnames = ["State Name", "Popular Food", "Population", "Land Area", "Capital City", "Gender Ratio"]

with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for state in data:
        writer.writerow(state)

print(f"Dataset saved as {filename}")
print("Current Working Directory:", os.getcwd())

df = pd.read_csv(filename, encoding='utf-8')
print(df)
