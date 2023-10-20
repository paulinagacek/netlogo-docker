# How to prepare expiriment in Netlogo
1. Build docker image
    ```docker
        sudo docker build --build-arg MODEL_FOLDER=GameOfLife -t netlogo .
    ```
2. Run container
    ```docker
        sudo docker run netlogo >> netlogo_logs.txt
    ```