import click
from ..communication.remote_calls import RemoteCalls

@click.group("test")
def cli():
    pass

@cli.command('test', help='Run tests.')
@click.option('--host', '-h', prompt='gRPC host', help='gRPC Host Address', default='localhost')
@click.option('--port', '-p', prompt='gRPC port', help='gRPC Port', default='50057')
@click.option('--cov/--no-cov', default=True)
@click.option('--no-capture', is_flag=True)
@click.option('--pdb', is_flag=True)
@click.argument('args', default='')
def test(host, port, cov, no_capture, pdb, args):
    rc = RemoteCalls(host, port)
    rc.run_test(cov, no_capture, pdb, args)

@cli.command('test-tox', help='Run tests using Tox environment.')
@click.option('--host', '-h', prompt='gRPC host', help='gRPC Host Address', default='localhost')
@click.option('--port', '-p', prompt='gRPC port', help='gRPC Port', default='50057')
@click.argument('args', default='--current-env')
def tox(host, port, args):
    rc = RemoteCalls(host, port)
    rc.run_tox(args)

@cli.command('test-tdd', help='Watch for changes to run tests automatically.')
@click.option('--host', '-h', prompt='gRPC host', help='gRPC Host Address', default='localhost')
@click.option('--port', '-p', prompt='gRPC port', help='gRPC Port', default='50057')
@click.option('--cov/--no-cov', default=False)
@click.option('--no-capture', is_flag=True)
@click.option('--pdb', is_flag=True)
@click.option('--partial', is_flag=True)
@click.argument('args', default='')
def tdd(host, port, cov, no_capture, pdb, partial, args):
    rc = RemoteCalls(host, port)
    rc.run_tdd(cov, no_capture, pdb, partial, args)