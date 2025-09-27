import csv

def load_jobs():
    jobs = []
    with open('job list.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_reader.__next__() # skipping the first row

        for row in csv_reader:
            jobs.append((int(row[0]), int(row[1]), int(row[2])))
        csvfile.close()

    return jobs

def load_memory_blocks():
    memory = []
    with open('memory list.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_reader.__next__() # skipping the header row

        for row in csv_reader:
            memory.append((int(row[0]), int(row[1])))
        csvfile.close()

    return memory