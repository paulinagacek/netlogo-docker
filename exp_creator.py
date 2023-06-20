import pandas as pd, os

MODEL_FOLDER='models/GameOfLife'
INPUT_NAME='input.csv'
EXPERIMENT_LAYOUT_FILE='exp_layout.xml'
EXPERIMENT_FILE='experiment.xml'

MAX_ITER=1000 # max nr of iterations

if __name__ == '__main__':
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

        with open(os.path.join(MODEL_FOLDER, EXPERIMENT_FILE), 'w') as exp_file:
            exp_file.truncate(0)
            exp_file.write(data)