# How to prepare expiriment in Netlogo
1. Put input file inside model's folder - `models\GameOfLife`. 
   - Input file should be called 'input.csv', if you have different name you can change it in `exp_creator.py`.
2. Run `exp_creator.py` to setup experiment (pandas has to be installed):
    ```bash
        python exp_creator.py
    ```
3. Build docker image
    ```docker
        docker build --build-arg MODEL_FOLDER=GameOfLife -t netlogo2 .
    ```
4. Run container
    ```docker
        docker run netlogo2
    ```