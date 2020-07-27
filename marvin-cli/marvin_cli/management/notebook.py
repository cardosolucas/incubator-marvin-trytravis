import click
from ..communication.remote_calls import RemoteCalls

@click.group("notebook")
def cli():
    pass

@cli.command("notebook", help="Run custom engine Jupyter Notebook.")
@click.option('--host', '-h', prompt='gRPC host', help='gRPC Host Address', default='localhost')
@click.option('--port', '-p', prompt='gRPC port', help='gRPC Port', default='50057')
@click.option('--notebook-port', '-np', prompt='Notebook port', help='Notebook port', default='8888')
@click.option('--enable-security', '-s', default=False, is_flag=True, help='Enable notebook security.')
def notebook(host, port, notebook_port, enable_security):
    rc = RemoteCalls()
    rc.run_notebook(notebook_port, enable_security)

@cli.command("lab", help="Run custom engine Jupyter Lab.")
@click.option('--host', '-h', prompt='gRPC host', help='gRPC Host Address', default='localhost')
@click.option('--port', '-p', prompt='gRPC port', help='gRPC Port', default='50057')
@click.option('--notebook-port', '-np', prompt='Notebook port', help='Notebook port', default='8888')
@click.option('--enable-security', '-s', default=False, is_flag=True, help='Enable notebook security.')
def lab(host, port, notebook_port, enable_security):
    rc = RemoteCalls()
    rc.run_lab(notebook_port, enable_security)