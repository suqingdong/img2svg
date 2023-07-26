import click
from typing import Optional

from . import version_info
from .core import Img2SVG


CONF_FORMAT = 'x y rx ry title href'

CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])

@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
@click.argument('image')
@click.option('-c', '--conf', help=f'the config file, format: "{CONF_FORMAT}", separate with <Tab>')
@click.option('-o', '--outfile', help='the output file', default='out.svg', show_default=True)
@click.option('-C', '--fill-color', help='the fill color', default='#CCCCCC', show_default=True)
@click.option('-P', '--fill-opacity', help='the fill opacity', default=0.3, show_default=True, type=float)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
def cli(image: str, conf: Optional[str], outfile: str, fill_color: str, fill_opacity: float) -> None:
    """
    CLI entrypoint for Img2SVG.

    :param image: Path to the image file.
    :param conf: Path to the configuration file.
    :param outfile: Path to the output file.
    :param fill_color: Fill color for SVG.
    :param fill_opacity: Fill opacity for SVG.
    """
    svg_builder = Img2SVG(image, fill_color=fill_color, fill_opacity=fill_opacity)
    svg_builder.wrap(conf)
    svg_builder.save(outfile)


def main() -> None:
    """
    Main function to start the CLI.
    """
    cli()


if __name__ == '__main__':
    main()
