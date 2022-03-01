Allows to launch bombardier Docker image and attack all URLs from given txt file


# Usage

0. Install Python3 and Docker

1. 
```
https://github.com/absent1706/bombard-urls-from-txt
pip3 install click
```

2. Put all your urls to `urls.txt` file (see provided example)

3.
```
python3 bombard-urls-from-txt.py
```

or customize params:
```
python3 bombard-urls-from-txt.py --filepath urls.txt --connections 1000 --duration 60s --infinitely on --output_docker_stdout off
```
