# WebCrawler

## The technical assignment:
Webcrawler
Expected time to spend on this: About 4 hours.

EXERCISE 1: In a language of your choice, implement a simple web crawler that gets a news
website as input (e.g. http://www.spiegel.de) and crawls the HTML content of up to 100
pages of that site with a breadth-first approach. The downloaded pages should be stored as
HTML in a folder in the file system.

EXERCISE 2: The crawler needs to be able to work with up to 50 parallel processes. The
number of processes can be passed as a parameter. If no input is given the default value
shall be 5 processes.

## The solution:
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
