import time, subprocess
import pandas as pd, os

MODEL_FOLDER='/opt/models/GameOfLife'
INPUT_NAME='input.csv'
EXPERIMENT_LAYOUT_FILE='exp_layout.xml'
EXPERIMENT_FILE='experiment.xml'

MAX_ITER=1000 # max nr of iterations

directory = os.getcwd()

def create_experiment_netlogo():
    df = pd.read_csv(os.path.join(MODEL_FOLDER, INPUT_NAME))
    ROWS=len(df.axes[0]) + 1 
    COLS=len(df.axes[1]) 
    MAX_ROW_NR = ROWS-1
    MAX_COL_NR = COLS-1

    with open(EXPERIMENT_LAYOUT_FILE, 'r') as file:
        data = file.read()
        data = data.replace('MAX_ITER', str(MAX_ITER))
        data = data.replace('ROWS', str(ROWS))
        data = data.replace('COLS', str(COLS))
        data = data.replace('MAX_ROW_NR', str(MAX_ROW_NR))
        data = data.replace('MAX_COL_NR', str(MAX_COL_NR))
        data = data.replace('INPUT', str(INPUT_NAME))

        with open(os.path.join(MODEL_FOLDER, EXPERIMENT_FILE), 'w') as exp_file:
            exp_file.truncate(0)
            exp_file.write(data)

input_names = ['10x10board.csv', '100x100board.csv', '1000x1000board.csv']
for INPUT_NAME in input_names:
    create_experiment_netlogo()

    REPETITIONS = 1
    start = time.time()
    for idx in range(REPETITIONS):
        subprocess.run(["./NetLogo 6.3.0/NetLogo_Console","--headless", 
            "--model", "/opt/models/NLModel.nlogo" ,
            "--setup-file", "/opt/models/experiment.xml" ,
            "--table", "models/table-output.csv ",
            "--spreadsheet", "models/table-output.csv"],  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    end = time.time()
    print((end - start)/REPETITIONS)