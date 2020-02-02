from datetime import date
from os import makedirs
from os.path import join
import re
from subprocess import run, PIPE
from sys import argv


def main(sootsai):
    ps = run([
        'docker', 'ps',
        '--filter', 'ancestor=postgres:11',
        '--format', '{{.Names}}'
    ], stdout=PIPE, check=True)
    sikan = date.today().isoformat()
    bokphiau = join(sootsai, sikan)
    makedirs(bokphiau, exist_ok=True)
    for tsua in ps.stdout.readlines():
        tsiling = docker_tsiling(tsua.rstrip(), bokphiau)
        run(tsiling, shell=True, check=True)


def docker_tsiling(mia, bokphiau):
    print('docker exec {} pg_dump -U postgres | gzip > {}.sql.gz'.format(
        mia, join(bokphiau, tongmia(mia))
    ))


def tongmia(mia):
    return re.sub('_postgres_.*', '', mia)


if __name__ == '__main__':
    main(argv[1])
