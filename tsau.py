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
    ], stdout=PIPE, encoding='utf-8', check=True)
    sikan = date.today().isoformat()
    bokphiau = join(sootsai, sikan)
    makedirs(bokphiau, exist_ok=True)
    for tsua in ps.stdout.rstrip().split('\n'):
        tsiling = docker_tsiling(tsua.rstrip(), bokphiau)
        run(tsiling, shell=True, check=True)


def docker_tsiling(mia, bokphiau):
    return 'docker exec {} pg_dump -U postgres | gzip > {}.sql.gz'.format(
        mia, join(bokphiau, tongmia(mia))
    )


def tongmia(mia):
    return re.sub('_postgres_.*', '', mia)


if __name__ == '__main__':
    if len(argv) != 2:
        print('usage: {0} soo-tsai\ne.g. {0} /backup/'.format(argv[0]))
        exit(1)
    main(argv[1])
