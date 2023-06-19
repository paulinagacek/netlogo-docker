# How to run a model
1. Build docker image
    ```docker
    docker build --build-arg MODEL_FOLDER=name -t netlogo2 .
    ```
    - For Game of life `MODEL_FOLDER=GameOfLife`
        ```docker
        docker build --build-arg MODEL_FOLDER=GameOfLife -t netlogo2 .
        ```
2. Run container
```docker
docker run netlogo2
```

