import click

from hades.controller.input import input_controller
from hades.lib import get_logger
from hades.matcher import matcher

logger = get_logger(__name__)


@click.command()
def cli():
    click.echo('starting hades')
    input_controller.start()
    while input_controller.running:
        if matcher.found_match:
            input_controller.stop()
            break
    if matcher.found_match:
        iterations = click.prompt('Sequence found. Enter number of iterations', type=int)
        click.echo('repeating sequence {} times'.format(iterations))


if __name__ == '__main__':
    cli()
