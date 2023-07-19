# WebCrawler


1. Create docker image
```
docker build -t crawler .
```

2. Run the image
```
docker run -d crawler
```
## Start Crawling

1. Enter container:
```
docker exec -it crawler:latest /bin/sh
```
2. Run crawler
```
python3.11 main.py --url="http://www.spiegel.de" --workers=10
```

_**--workers**_ - is not required parameter.
Parsed sites will be stored in "storage/" directory in the project's root.
