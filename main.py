import click

from hades.controller.output import output_controller
from hades.controller.input import input_controller
from hades.lib import APPLICATION_ID
from hades.lib import get_logger
from hades.matcher import matcher

logger = get_logger(__name__)


@click.command()
def cli():
    click.echo('Starting {}'.format(APPLICATION_ID))
    input_controller.start()
    while input_controller.running:
        if matcher.found_match:
            input_controller.stop()
            break
    if not matcher.found_match:
        click.echo('No sequence found. Exiting.')
        return
    click.echo('Sequence found')
    iterations = click.prompt('Enter number of iterations', type=int)
    click.echo('repeating sequence {} times'.format(iterations))
    output_controller.replay_actions(matcher.action_generator(), iterations=iterations)


if __name__ == '__main__':
    cli()
