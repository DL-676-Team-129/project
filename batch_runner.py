import os

BASE_PATH = "./"

with open(BASE_PATH + "Labels.txt", 'r') as f:
    lines = f.readlines()[:100]
    labels = [line.replace('\n', '').replace(' ', '-').lower() for line in lines]

for product in labels:
    for i in range(1, 101, 10):
        JOB_NAME = product + str(i)
        os.system("sbatch {}".format(BASE_PATH + 'batch-script/' + JOB_NAME + '.script'))