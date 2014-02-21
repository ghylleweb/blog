from fabric.api import lcd, local, env, require, run
import os

production_server = os.environ['PRODUCTION_SERVER']


def prod():
    env.hosts = [production_server]
    env.remote_app_dir = '~/webapps/blog/repo/blog/'
    env.remote_apache_dir = '~/webapps/blog/apache2/'


def restart():
    """Restart apache on the server."""
    require('hosts', provided_by=[prod])
    require('remote_apache_dir', provided_by=[prod])

    run("%s/bin/restart" % env.remote_apache_dir)


def commit(branch_name):
    message = raw_input("Enter a git commit message:  ")
    local("git add -A && git commit -m \"%s\"" % message)
    local("git push origin %s" % branch_name)

    print "Changes pushed to %s..." % branch_name


def collectstatic():
    require('hosts', provided_by=[prod])
    run("cd %s; python manage.py collectstatic --noinput" % env.remote_app_dir)


def deploy():
    require('hosts', provided_by=[prod])
    require('remote_app_dir', provided_by=[prod])

    # First lets commit changes to github
    commit("master")
    # Now lets pull the changes to the server
    run("cd %s; git pull git@github.com:jghyllebert/blog.git" % env.remote_app_dir)
    # And lastly update static media files
    collectstatic()