import os

BASE_PATH = "./"

with open(BASE_PATH + "Labels.txt", 'r') as f:
    lines = f.readlines()[:100]
    labels = [line.replace('\n', '').replace(' ', '-').lower() for line in lines]

with open(BASE_PATH + 'batch-script/base.script', 'r') as fb:
    base_script = fb.read()

for product in labels:
    os.system("mkdir {}scraped-images/{}".format(BASE_PATH, product))
    for i in range(1, 101, 10):
        code_path = BASE_PATH + "image_downloader.py"
        url_path = BASE_PATH + "image-urls/{}.txt".format(product)
        out_fpath = BASE_PATH + "scraped-images/{}/".format(product)
        COMMAND = "python {} {} {} {} {}".format(code_path, url_path, i, i + 10, out_fpath)

        JOB_NAME = product + str(i)
        OUTPUT = './logs/{}.txt'.format(JOB_NAME)

        new_script = base_script
        new_script = new_script.replace('REPLACE_JOB_NAME', JOB_NAME)
        new_script = new_script.replace('REPLACE_OUTPUT', OUTPUT)
        new_script = new_script.replace('REPLACE_COMMAND', COMMAND)

        with open(BASE_PATH + 'batch-script/' + JOB_NAME + '.script', 'w') as fo:
            fo.write(new_script)