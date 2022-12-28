from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")
wwr_jobs = extract_wwr_jobs(keyword)


file = open(f"{keyword}".csv, "w")

file.write("Position,Company,Location,URL\n")

for job in wwr_jobs:
    file.write(
        f"{job['position']}, {job['company']}, {job['location']},{job['link']}\n"
    )
file.close()

"""
wwr = extract_wwr_jobs(keyword)

jobs = wwr

for job in jobs:
    print(job)
    print("//////\n///////")

"""
