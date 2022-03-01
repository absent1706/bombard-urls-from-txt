Allows to launch bombardier Docker image and attack all URLs from given txt file


# Usage

0. Install Python3 and Docker

1. 
```
pip3 install click
```

2. Put all your urls to `urls.txt` file (see provided example)

3.
```
python bombard-urls-from-txt.py --filepath urls.txt --connections 1000 --duration 20s --infinitely off --output_docker_stdout off
```
