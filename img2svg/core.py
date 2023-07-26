import os
from typing import Tuple, Union
from PIL import Image as PILImage

import click
from pysvg.structure import Svg, Image
from pysvg.shape import Rect
from pysvg.linking import A

from . import util


class Img2SVG:
    """
    Class to convert an image to an SVG format with interactive elements.
    """

    def __init__(self, image: str, fill_color: str = '#CCCCCC', fill_opacity: float = 0.3):
        """
        Initialize the Img2SVG instance.

        :param image: Path to the image file.
        :param fill_color: Color to fill the rect element, default is '#CCCCCC'.
        :param fill_opacity: Opacity to fill the rect element, default is 0.3.
        """
        self.image = image
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.im = PILImage.open(self.image)
        self.svg = self.init_svg()

    def init_svg(self) -> Svg:
        """
        Initialize the Svg object and add the image to it.

        :return: Initialized Svg object.
        """
        svg = Svg(width='100%', height='100%')
        svg.setAttribute('viewBox', f'0 0 {self.im.width} {self.im.height}')
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet')
        im_element = self.create_image_element()
        svg.addElement(im_element)
        return svg

    def wrap(self, conf: str) -> None:
        """
        Wrap the Svg with linking and rect elements.

        :param conf: Path to the configuration file.
        """
        if conf and os.path.isfile(conf):
            click.secho(f'>>> reading conf: {conf}', fg='green')
            for linelist in util.parse_conf(conf):
                print(linelist)
                position = map(int, linelist[:4])
                title = linelist[4]
                href = linelist[5]
                a = self.create_linking_element(title=title, href=href)
                rect = self.create_rect_element(position)
                a.addElement(rect)
                self.svg.addElement(a)

    def create_rect_element(self, position: Tuple[int, int, int, int]) -> Rect:
        """
        Create a rect element with mouse event.

        :param position: A tuple of four integers specifying the position of the rect element.
        :return: Rect object.
        """
        x, y, rx, ry = position
        w, h = rx - x, ry - y
        rect = Rect(x=x, y=y, width=w, height=h, fill=self.fill_color, fill_opacity=0)
        rect.setAttribute('onmouseover', f"evt.target.style['fill-opacity'] = {self.fill_opacity};")
        rect.setAttribute('onmouseout', "evt.target.style['fill-opacity'] = 0;")
        return rect

    def create_linking_element(self, title: str = '', href: str = '') -> A:
        """
        Create a linking element.

        :param title: Title of the link, default is ''.
        :param href: Target URL of the link, default is ''.
        :return: A object.
        """
        a = A(target='new_window')
        a.set_xlink_title(title)
        a.set_xlink_href(href)
        return a

    def create_image_element(self) -> Image:
        """
        Create an image element.

        :return: Image object.
        """
        im_element = Image(x=0, y=0, width=self.im.width, height=self.im.height)
        data_url = self.img_to_data_url()
        im_element.set_xlink_href(data_url)
        return im_element

    def img_to_data_url(self) -> str:
        """
        Convert the image to a data URL.

        :return: String of data URL.
        """
        data_url = f'data:image/png;base64,' + util.img_to_b64(self.image)
        return data_url

    def save(self, outfile: str) -> None:
        """
        Save the Svg to a file.

        :param outfile: Path to the output file.
        """
        self.svg.save(outfile, encoding='UTF-8', standalone='no')
        click.secho(f'save file: {outfile}', fg='cyan')


if __name__ == '__main__':
    svg_builder = Img2SVG('tests/input.png')
    svg_builder.wrap('tests/config.txt')
    svg_builder.save('out.svg')
