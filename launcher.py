#! /usr/bin/python
from __future__ import print_function

'''Parallel launcher built upon GNU Parallel'''

__author__ = "Xtotdam"
__license__ = "MIT"
__version__ = "1.0"


### import configuration
from launcher_settings import *


### parse command line arguments
import argparse
parser = argparse.ArgumentParser(
    description='Parallel launcher. It is wrapper for GNU Parallel.',
    epilog='https://github.com/xtotdam/parallel-launcher'
)
parser.add_argument('-n', '--dry-run', action='store_const', const=True, default=False,
    help='Not write into {}, just show command on screen'.format(out_filename))
args = parser.parse_args()


### magic that makes input work as raw_input in both py2 and py3
try:
    input = raw_input
except NameError:
    pass


def str_range(s, sep=':'):
    '''
    This function expands string like 'a:b:c' into range from a to c with step b. Step may be negative.

    >>> str_range('10:5:50') '10 15 20 25 30 35 40 45 50'

    >>> str_range('50:-5:10') '50 45 40 35 30 25 20 15 10'

    :type       s:    str
    :param      s:    deflated string
    :type       sep:  str
    :param      sep:  separating symbol

    :returns:   expanded string
    :rtype:     str
    '''
    begin, step, end = map(int, s.split(sep))
    if step < 0:
        r = list(range(begin, end - 1, step))
    else:
        r = list(range(begin, end + 1, step))
    return ' '.join(map(str, r))


### prepare place for current values
for k in params.keys():
    params[k]['curr'] = None


### interactively get input for all keys
longest_key =       max(len(k) for k in params.keys())
longest_default =   max(len(params[k]['def']) for k in params.keys())
longest_descr =     max(len(params[k]['descr']) for k in params.keys())

template = '> {{:2s}}{{:<{}s}} {{:<{}s}} {{:>{}s}} : '.format(longest_key+2, longest_default+2, longest_descr+2)
redmark = '*'
header = ' ' * (len(redmark) + 1) + template[len(redmark)+1 : -2].format('', 'Key', 'Default', 'Description')
horline = '-' * len(header)

print('Using settings: {}\n{}\n'.format(settings_name, settings_file))
if len(need_expansion) > 0:
    print('[{}] marks expandable fields. start:step:stop is usable inside'.format(redmark))
print(header)
print(horline)

for k in params.keys():
    try:
        defvalue = '[{}]'.format(params[k]['def'])
        mark = redmark if k in need_expansion else str()
        prompt = template.format(mark, k, defvalue, params[k]['descr'])
        part = input(prompt)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')
        exit()

    if part:
        params[k]['curr'] = part
    else:
        params[k]['curr'] = params[k]['def']
        print('\033[1A\033[{}C{}'.format(len(prompt), params[k]['curr']))


### choose jobs number
# if no input was given then GNU Parallel will use every core
if params['jobs']['curr']:
    params['jobs']['curr'] = '-j' + params['jobs']['curr']


### expanding ranges
for key in need_expansion:
    if ':' in params[key]['curr']:
        tr = params[key]['curr']
        params[key]['curr'] = str_range(params[key]['curr'])
        print('Converting \'{}\': {} -> {}'.format(key, tr, params[key]['curr']))


### handling iterations number
# {1..1} is perfectly okay
params['iterations']['curr'] = '{{1..{}}}'.format(params['iterations']['curr'])


### handling backround operation
if not params['background']['curr'].startswith('y'):
    gnuparallel = 'parallel --eta --progress'
    ending = ''
else:
    gnuparallel = 'parallel'
    ending = ' &'


### shuffling jobs if needed
if params['shuffle']['curr'].startswith('y'):
    gnuparallel += ' --shuf'


### assembling final command
# part for `parallel`
command = [' '.join([gnuparallel, additional_parallel_keys, params['jobs']['curr'], executable])]

# part for executable arguments
for k in right_order:
    if ('seed' in k) and (len(params[k]['curr']) == 0):
        continue
    command.append(params[k]['curr'])
command.append(params['iterations']['curr'])

command = ' ::: '.join(command)

# part for background ending
command += ending



print(horline)
print(command)
print(horline)

if not args.dry_run:
    with open(out_filename, 'w') as f:
        f.write(command)
