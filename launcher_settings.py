from collections import OrderedDict
params = OrderedDict()

###
#   Name of this file
settings_name = 'Skyrmions'
settings_file = __file__


###
#   Executable arguments
#   key     will be name of parameter
#   'def'   is the default value
#   'descr' is the description
params['Nx'] =               {'def': '30',        'descr': 'cell width [atoms]'}
params['Ny'] =               {'def': '30',        'descr': 'cell height [atoms]'}

params['steps'] =            {'def': '1e5',       'descr': 'simulation steps number'}
params['every_step'] =       {'def': '1000',      'descr': 'periods to write on disk. -1 means only last. -2 means not at all'}

params['J1'] =               {'def': '5.7',       'descr': '[meV] see PRL 117 207202'}
params['J2'] =               {'def': '-0.84',     'descr': '[meV]'}
params['J3'] =               {'def': '-1.45',     'descr': '[meV]'}
params['J4'] =               {'def': '-0.06',     'descr': '[meV]'}
params['J5'] =               {'def': '0.2',       'descr': '[meV]'}
params['J6'] =               {'def': '0.2',       'descr': '[meV]'}
params['J7'] =               {'def': '-0.2',      'descr': '[meV]'}
params['J8'] =               {'def': '0.5',       'descr': '[meV]'}

params['K4'] =               {'def': '-1.8',      'descr': '[meV]'}
params['D'] =                {'def': '-1.05',     'descr': '[meV]'}
params['B'] =                {'def': '-0.2',      'descr': '[meV]'}
params['K'] =                {'def': '-0.8',      'descr': '[meV]'}

params['T'] =                {'def': '1',         'descr': '[K]'}

params['seed'] =             {'def': '0',         'descr': 'seed for PRNG. 0 means random'}


###
#   Below are keys for GNU Parallel/executable choosing/etc = not executable arguments
#   Their number is `launch_parameters_count`
params['iterations'] =      {'def': '1',          'descr': ''}


###
#   Number of jobs to run simultaneously.
#   Will be passed to GNU Parallel. Empty means utilize every CPU.
params['jobs'] =            {'def': '',           'descr': ''}


###
#   If 'y' then --shuf will be passed to GNU Parallel to shuffle jobs
params['shuffle'] =         {'def': 'n',          'descr': ''}


###
#   If 'y' then an ampersand (&) will be added on the end of the command to run in background
#   If 'n' then progressbar and ETA will be shown (--eta and --progress)
params['background'] =      {'def': 'y',          'descr': 'work in bg? y / n'}


###
#   Correct order of all parameters that go into the command
#   Only main executable arguments are allowed here
right_order = ['Nx', 'Ny', 'steps', 'every_step', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'K4', 'D', 'B', 'K', 'T', 'seed']


###
#   List of parameters that will need expansion during command constructing
#   Expansion means a:b:c --> a a+b a+2b ... c
#   Example: '10:5:50' --> '10 15 20 25 30 35 40 45 50'
need_expansion = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'K4', 'D', 'B', 'K', 'T']


###
#   Main executable file to call
executable = './main'


###
#   Additional keys to pass to GNU Parallel
additional_parallel_keys = ''


###
#   Name of filename to write the command to
out_filename = 'command.sh'



###
#   Simple check that lists above were updated on adding new parameter
#   Number of parameters that don't go into the command
launch_parameters_count = 4

try:
    assert len(params.keys()) == len(right_order) + launch_parameters_count
except AssertionError as e:
    print('*** You may have forgotten to update parameters in', __file__)
    print('If not then review launch_parameters_count inside that file\n')
    raise e
