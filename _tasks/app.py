from invoke import task


@task
def test(c):
    c.run('python -m unittest discover tests')


@task
def lint(c):
    c.run('pylint app tests _tasks')


@task
def coverage_report(c):
    c.run('coverage run -m unittest discover tests')
    c.run('coverage report -m')
