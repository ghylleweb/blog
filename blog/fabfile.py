from fabric.api import lcd, local


def prepare_deployment(branch_name):
    local('git commit')


def deploy():
    with lcd('/path/to/prod/area'):
        local('git pull /path/to/dev/area')

        local('python manage.py migrate')
        local('/path/to/restart/server')