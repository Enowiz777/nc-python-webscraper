from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

file = open(f"{keyword}".csv, "w")

file.write("Position,Company,Location,URL")
file.close()

"""
wwr = extract_wwr_jobs(keyword)

jobs = wwr

for job in jobs:
    print(job)
    print("//////\n///////")

"""
