import sys
import subprocess
from time import perf_counter

def average_runtime(times_to_run, file_base, file_extension, interpreter):
    times_to_run = int(times_to_run)
    start_time = perf_counter()
    for i in range(times_to_run):
        subprocess.run([f'{interpreter}', f'{file_base}.{file_extension}'])
    end_time = perf_counter()
    return (end_time - start_time) / times_to_run


if __name__ == '__main__':
    if len(sys.argv) % 2 == 0:
        print('Wrong number of arguments.')
        print('Usage: compare.py <file_without_extension> <num_loops> [<extension> <language_name> ... ]')
        sys.exit(0)
        
    maps = []
    file_base = sys.argv[1]
    num_loops = sys.argv[2]

    for i in range(3, len(sys.argv), 2):
        maps.append({'extension' : sys.argv[i], 'interpreter' : sys.argv[i + 1]})

    for i in range(len(maps)):
        print(f'Running {maps[i]["interpreter"]}')
        maps[i]['average_run'] = average_runtime(num_loops, file_base, maps[i]['extension'], maps[i]['interpreter'])

    maps = sorted(maps, key = lambda x : x['average_run'])
    
    for _map in maps:
        print(f'{_map["interpreter"]} ran in an average of {_map["average_run"]} seconds')
        
    
