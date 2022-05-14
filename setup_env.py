import subprocess


def install(path: str):
    subprocess.call(f'pip install -r {path}/requirements.txt')
    subprocess.call(f'pip install -e {path}')


install('ext/doer')
