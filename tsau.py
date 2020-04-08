from datetime import date
from os import makedirs
from os.path import join
import re
from subprocess import run, PIPE
from sys import argv


def main(sootsai):
    kiatko = []
    for panpun in [11, 12]:
        kiatko.append(
            run([
                'docker', 'ps',
                '--filter', 'ancestor=postgres:{}'.format(panpun),
                '--format', '{{.Names}}'
            ], stdout=PIPE, encoding='utf-8', check=True)
            .stdout
            .strip()
        )
        if kiatko[-1] == '':
            kiatko.pop()
    sikan = date.today().isoformat()
    bokphiau = join(sootsai, sikan)
    makedirs(bokphiau, exist_ok=True)
    for tsua in '\n'.join(kiatko).split('\n'):
        if tsua == '':
            print('Bo mih-kiann')
            return
        print('Pī-hūn', tsua)
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
