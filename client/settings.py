import os
import sys

# global configuration/Users/chenzhang
# GIT_URL = 'https://github.com/postgres/postgres.git'
GIT_URL = 'https://gitee.com/purpleyu/postgres.git'  # changed to a local repo
REPOSITORY_PATH = '/raid/git-postgres'
# BUILD_PATH = '/Users/chenzhang/anaconda3'
BUILD_PATH = '/usr/lib/postgresql/11'
BIN_PATH = os.path.join(BUILD_PATH, 'bin')
DATADIR_PATH = '/raid/data-postgres'
SCRIPTS_DIR = 'scripts/files/'

POSTGRES_CONFIG = {
    'shared_buffers': '1GB',
    'work_mem': '64MB',
    'maintenance_work_mem': '128MB',
    'min_wal_size': '2GB',
    'max_wal_size': '4GB',
    'log_line_prefix': '%t [%p]: [%l-1] db=%d,user=%u,app=%a,client=%h ',
    'log_checkpoints': 'on',
    'log_autovacuum_min_duration': '0',
    'log_temp_files': '32',
    'checkpoint_timeout': '30min',
    'checkpoint_completion_target': '0.9',
}

DATABASE_NAME = 'postgres'  # This name needs to be the same as rest_api settings_local.py database NAME

OUTPUT_DIR = '/raid/perf-output'

# configuration for PgBench
# runs - number of repetitions (including test for all client counts)
# duration - duration (in seconds) of a single benchmark (per client count)
PGBENCH_CONFIG = {
    'runs': 3,
    'duration': 1,  # 600
    'csv': False
}

# Benchmarking options for PgBench
# clients - number of concurrent database sessions
# threads - number of worker threads within PgBench
PGBENCH_BENCHMARKING_OPTIONS = {
    'scale': 10,
    'clients': [1, 2, 4],
    'threads': 1
}

# ignore missing file with local config
try:
    from settings_local import *
except Exception as e:
    print(sys.stderr, "ERROR: local configuration (settings_local.py) " \
                      "not found")
    sys.exit(1)
