import multiprocessing as mp
import os
import sys
import subprocess

import time

import click

@click.command()
@click.option('--filepath',  default='urls.txt', help='txt file containing bombarded url in each line')
@click.option('--connections',  default=1000, help='# of bombardier connections')
@click.option('--duration', default=60, help='time to bombard each url during 1 cycle, in seconds')
@click.option('--infinitely',  default=True, help='whether to bombard given URLs infinitely. If set to true, program will run "while True"')
@click.option('--output_docker_stdout',  default=False, help='whether to print stdout that Docker returns (with bombarding statistics)')
def main(filepath, connections, duration, infinitely, output_docker_stdout):
    urls = []

    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           urls.append(line.strip())
           line = fp.readline()
           cnt += 1
    print('will now bombard these urls:', urls)

    def bombard():
        for url in urls:
            print('bombarding', url, 'for', duration, ' seconds ...')
            result = subprocess.run(
                ['docker', 'run', '-d', '-ti', 'alpine/bombardier', 
                 '-c', str(connections), 
                 '-d', f'{duration}s', 
                 '-l', url],
                capture_output=True, text=True)
            if output_docker_stdout:
                print(result.stdout)

    if infinitely:
        i = 1
        while True:
            print(f'\n===== Starting bombarding session #{i} ==========')
            bombard()
            time.sleep(duration)
            i = i+1
    else:
        bombard()

if __name__ == '__main__':
    main()