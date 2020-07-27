import os
import click

@click.group("edit")
def cli():
    pass

@cli.command("edit-config", help="Edit configuration.")
@click.pass_context
def config(ctx):
    filepath = os.path.join(os.environ['MARVIN_DATA_PATH'], '.conf', 'cli_conf.json')
    os.system(ctx.obj['editor'] + ' ' + filepath)

@cli.command("edit-metadata", help="Edit engine.metadata.")
@click.pass_context
def metadata(ctx):
    filepath = "engine.metadata"
    os.system(ctx.obj['editor'] + ' ' + filepath)
