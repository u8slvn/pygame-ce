from typing import Any, Callable, Iterable, List, Optional, Tuple, Union

from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface

from ._common import ColorValue, FileArg, RectValue

def get_error() -> str: ...
def get_version(linked: bool = True) -> Tuple[int, int, int]: ...
def init(cache_size: int = 64, resolution: int = 72) -> None: ...
def quit() -> None: ...
def get_init() -> bool: ...
def was_init() -> bool: ...
def get_cache_size() -> int: ...
def get_default_resolution() -> int: ...
def set_default_resolution(resolution: int) -> None: ...
def SysFont(
    name: Union[str, bytes, Iterable[Union[str, bytes]], None],
    size: int,
    bold: int = False,
    italic: int = False,
    constructor: Optional[Callable[[Optional[str], int, bool, bool], Font]] = None,
) -> Font: ...
def get_default_font() -> str: ...
def get_fonts() -> List[str]: ...
def match_font(
    name: Union[str, bytes, Iterable[Union[str, bytes]]],
    bold: Any = False,
    italic: Any = False,
) -> str: ...

STYLE_NORMAL: int
STYLE_UNDERLINE: int
STYLE_OBLIQUE: int
STYLE_STRONG: int
STYLE_WIDE: int
STYLE_DEFAULT: int

class Font:
    @property
    def size(self) -> Union[float, Tuple[float, float]]: ...
    @size.setter
    def size(self, value: Union[float, Tuple[float, float]]) -> None: ...
    @property
    def style(self) -> int: ...
    @style.setter
    def style(self, value: int) -> None: ...
    @property
    def height(self) -> int: ...
    @property
    def ascender(self) -> int: ...
    @property
    def descender(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def style_name(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def scalable(self) -> bool: ...
    @property
    def fixed_width(self) -> bool: ...
    @property
    def fixed_sizes(self) -> int: ...
    @property
    def antialiased(self) -> bool: ...
    @antialiased.setter
    def antialiased(self, value: bool) -> None: ...
    @property
    def kerning(self) -> bool: ...
    @kerning.setter
    def kerning(self, value: bool) -> None: ...
    @property
    def vertical(self) -> bool: ...
    @vertical.setter
    def vertical(self, value: bool) -> None: ...
    @property
    def pad(self) -> bool: ...
    @pad.setter
    def pad(self, value: bool) -> None: ...
    @property
    def oblique(self) -> bool: ...
    @oblique.setter
    def oblique(self, value: bool) -> None: ...
    @property
    def strong(self) -> bool: ...
    @strong.setter
    def strong(self, value: bool) -> None: ...
    @property
    def underline(self) -> bool: ...
    @underline.setter
    def underline(self, value: bool) -> None: ...
    @property
    def wide(self) -> bool: ...
    @wide.setter
    def wide(self, value: bool) -> None: ...
    @property
    def strength(self) -> float: ...
    @strength.setter
    def strength(self, value: float) -> None: ...
    @property
    def underline_adjustment(self) -> float: ...
    @underline_adjustment.setter
    def underline_adjustment(self, value: float) -> None: ...
    @property
    def ucs4(self) -> bool: ...
    @ucs4.setter
    def ucs4(self, value: bool) -> None: ...
    @property
    def use_bitmap_strikes(self) -> bool: ...
    @use_bitmap_strikes.setter
    def use_bitmap_strikes(self, value: bool) -> None: ...
    @property
    def resolution(self) -> int: ...
    @property
    def rotation(self) -> int: ...
    @rotation.setter
    def rotation(self, value: int) -> None: ...
    @property
    def fgcolor(self) -> Color: ...
    @fgcolor.setter
    def fgcolor(self, value: Color) -> None: ...
    @property
    def bgcolor(self) -> Color: ...
    @bgcolor.setter
    def bgcolor(self, value: Color) -> None: ...
    @property
    def origin(self) -> bool: ...
    @origin.setter
    def origin(self, value: bool) -> None: ...
    def __init__(
        self,
        file: Optional[FileArg],
        size: float = 0,
        font_index: int = 0,
        resolution: int = 0,
        ucs4: int = False,
    ) -> None: ...
    def get_rect(
        self,
        text: str,
        style: int = STYLE_DEFAULT,
        rotation: int = 0,
        size: float = 0,
    ) -> Rect: ...
    def get_metrics(
        self, text: str, size: float = 0
    ) -> List[Tuple[int, int, int, int, float, float]]: ...
    def get_sized_ascender(self, size: float) -> int: ...
    def get_sized_descender(self, size: float) -> int: ...
    def get_sized_height(self, size: float) -> int: ...
    def get_sized_glyph_height(self, size: float) -> int: ...
    def get_sizes(self) -> List[Tuple[int, int, int, float, float]]: ...
    def render(
        self,
        text: str,
        fgcolor: Optional[ColorValue] = None,
        bgcolor: Optional[ColorValue] = None,
        style: int = STYLE_DEFAULT,
        rotation: int = 0,
        size: float = 0,
    ) -> Tuple[Surface, Rect]: ...
    def render_to(
        self,
        surf: Surface,
        dest: RectValue,
        text: str,
        fgcolor: Optional[ColorValue] = None,
        bgcolor: Optional[ColorValue] = None,
        style: int = STYLE_DEFAULT,
        rotation: int = 0,
        size: float = 0,
    ) -> Rect: ...
    def render_raw(
        self,
        text: str,
        style: int = STYLE_DEFAULT,
        rotation: int = 0,
        size: float = 0,
        invert: bool = False,
    ) -> Tuple[bytes, Tuple[int, int]]: ...
    def render_raw_to(
        self,
        array: Any,
        text: str,
        dest: Optional[RectValue] = None,
        style: int = STYLE_DEFAULT,
        rotation: int = 0,
        size: float = 0,
        invert: bool = False,
    ) -> Rect: ...
