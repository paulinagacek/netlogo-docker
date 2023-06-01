# How to run GameOfLife
1. Build docker image
```docker
docker build --build-arg MODEL_NAME=GameOfLife.nlogo --build-arg NETLOGO_VERSION=6.2.2 -t netlogo .
```

2. Install sth to run GUI
```docker
docker run -d --name x11-bridge -e MODE="tcp" -e XPRA_HTML="yes" -e DISPLAY=:14 -e XPRA_PASSWORD=111 -p 10000:10000 jare/x11-bridge
```
```docker
docker run -d --name netlogo --volumes-from x11-bridge -v ~/netlogo-docker/results:/home/results netlogo
```

3. Open webbrowser at `http://localhost:10000/index.html?encoding=rgb32&password=111#` and wait for GUI to load

4. Stop docker images when you're finished
```docker
docker stop netlogo 
docker stop x11-bridge
```