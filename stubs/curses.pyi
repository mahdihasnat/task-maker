from typing import Any, BinaryIO, IO, Optional, Tuple, Union, overload

# pylint: disable=invalid-name
# pylint: disable=pointless-statement
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=redefined-outer-name
# pylint: disable=no-self-use
# pylint: disable=function-redefined

_chtype = Union[str, bytes, int]

ALL_MOUSE_EVENTS = ...  # type: int
A_ALTCHARSET = ...  # type: int
A_ATTRIBUTES = ...  # type: int
A_BLINK = ...  # type: int
A_BOLD = ...  # type: int
A_CHARTEXT = ...  # type: int
A_COLOR = ...  # type: int
A_DIM = ...  # type: int
A_HORIZONTAL = ...  # type: int
A_INVIS = ...  # type: int
A_LEFT = ...  # type: int
A_LOW = ...  # type: int
A_NORMAL = ...  # type: int
A_PROTECT = ...  # type: int
A_REVERSE = ...  # type: int
A_RIGHT = ...  # type: int
A_STANDOUT = ...  # type: int
A_TOP = ...  # type: int
A_UNDERLINE = ...  # type: int
A_VERTICAL = ...  # type: int
BUTTON1_CLICKED = ...  # type: int
BUTTON1_DOUBLE_CLICKED = ...  # type: int
BUTTON1_PRESSED = ...  # type: int
BUTTON1_RELEASED = ...  # type: int
BUTTON1_TRIPLE_CLICKED = ...  # type: int
BUTTON2_CLICKED = ...  # type: int
BUTTON2_DOUBLE_CLICKED = ...  # type: int
BUTTON2_PRESSED = ...  # type: int
BUTTON2_RELEASED = ...  # type: int
BUTTON2_TRIPLE_CLICKED = ...  # type: int
BUTTON3_CLICKED = ...  # type: int
BUTTON3_DOUBLE_CLICKED = ...  # type: int
BUTTON3_PRESSED = ...  # type: int
BUTTON3_RELEASED = ...  # type: int
BUTTON3_TRIPLE_CLICKED = ...  # type: int
BUTTON4_CLICKED = ...  # type: int
BUTTON4_DOUBLE_CLICKED = ...  # type: int
BUTTON4_PRESSED = ...  # type: int
BUTTON4_RELEASED = ...  # type: int
BUTTON4_TRIPLE_CLICKED = ...  # type: int
BUTTON_ALT = ...  # type: int
BUTTON_CTRL = ...  # type: int
BUTTON_SHIFT = ...  # type: int
COLOR_BLACK = ...  # type: int
COLOR_BLUE = ...  # type: int
COLOR_CYAN = ...  # type: int
COLOR_GREEN = ...  # type: int
COLOR_MAGENTA = ...  # type: int
COLOR_RED = ...  # type: int
COLOR_WHITE = ...  # type: int
COLOR_YELLOW = ...  # type: int
COLORS = ...  # type: int
ERR = ...  # type: int
KEY_A1 = ...  # type: int
KEY_A3 = ...  # type: int
KEY_B2 = ...  # type: int
KEY_BACKSPACE = ...  # type: int
KEY_BEG = ...  # type: int
KEY_BREAK = ...  # type: int
KEY_BTAB = ...  # type: int
KEY_C1 = ...  # type: int
KEY_C3 = ...  # type: int
KEY_CANCEL = ...  # type: int
KEY_CATAB = ...  # type: int
KEY_CLEAR = ...  # type: int
KEY_CLOSE = ...  # type: int
KEY_COMMAND = ...  # type: int
KEY_COPY = ...  # type: int
KEY_CREATE = ...  # type: int
KEY_CTAB = ...  # type: int
KEY_DC = ...  # type: int
KEY_DL = ...  # type: int
KEY_DOWN = ...  # type: int
KEY_EIC = ...  # type: int
KEY_END = ...  # type: int
KEY_ENTER = ...  # type: int
KEY_EOL = ...  # type: int
KEY_EOS = ...  # type: int
KEY_EXIT = ...  # type: int
KEY_F0 = ...  # type: int
KEY_F1 = ...  # type: int
KEY_F10 = ...  # type: int
KEY_F11 = ...  # type: int
KEY_F12 = ...  # type: int
KEY_F13 = ...  # type: int
KEY_F14 = ...  # type: int
KEY_F15 = ...  # type: int
KEY_F16 = ...  # type: int
KEY_F17 = ...  # type: int
KEY_F18 = ...  # type: int
KEY_F19 = ...  # type: int
KEY_F2 = ...  # type: int
KEY_F20 = ...  # type: int
KEY_F21 = ...  # type: int
KEY_F22 = ...  # type: int
KEY_F23 = ...  # type: int
KEY_F24 = ...  # type: int
KEY_F25 = ...  # type: int
KEY_F26 = ...  # type: int
KEY_F27 = ...  # type: int
KEY_F28 = ...  # type: int
KEY_F29 = ...  # type: int
KEY_F3 = ...  # type: int
KEY_F30 = ...  # type: int
KEY_F31 = ...  # type: int
KEY_F32 = ...  # type: int
KEY_F33 = ...  # type: int
KEY_F34 = ...  # type: int
KEY_F35 = ...  # type: int
KEY_F36 = ...  # type: int
KEY_F37 = ...  # type: int
KEY_F38 = ...  # type: int
KEY_F39 = ...  # type: int
KEY_F4 = ...  # type: int
KEY_F40 = ...  # type: int
KEY_F41 = ...  # type: int
KEY_F42 = ...  # type: int
KEY_F43 = ...  # type: int
KEY_F44 = ...  # type: int
KEY_F45 = ...  # type: int
KEY_F46 = ...  # type: int
KEY_F47 = ...  # type: int
KEY_F48 = ...  # type: int
KEY_F49 = ...  # type: int
KEY_F5 = ...  # type: int
KEY_F50 = ...  # type: int
KEY_F51 = ...  # type: int
KEY_F52 = ...  # type: int
KEY_F53 = ...  # type: int
KEY_F54 = ...  # type: int
KEY_F55 = ...  # type: int
KEY_F56 = ...  # type: int
KEY_F57 = ...  # type: int
KEY_F58 = ...  # type: int
KEY_F59 = ...  # type: int
KEY_F6 = ...  # type: int
KEY_F60 = ...  # type: int
KEY_F61 = ...  # type: int
KEY_F62 = ...  # type: int
KEY_F63 = ...  # type: int
KEY_F7 = ...  # type: int
KEY_F8 = ...  # type: int
KEY_F9 = ...  # type: int
KEY_FIND = ...  # type: int
KEY_HELP = ...  # type: int
KEY_HOME = ...  # type: int
KEY_IC = ...  # type: int
KEY_IL = ...  # type: int
KEY_LEFT = ...  # type: int
KEY_LL = ...  # type: int
KEY_MARK = ...  # type: int
KEY_MAX = ...  # type: int
KEY_MESSAGE = ...  # type: int
KEY_MIN = ...  # type: int
KEY_MOUSE = ...  # type: int
KEY_MOVE = ...  # type: int
KEY_NEXT = ...  # type: int
KEY_NPAGE = ...  # type: int
KEY_OPEN = ...  # type: int
KEY_OPTIONS = ...  # type: int
KEY_PPAGE = ...  # type: int
KEY_PREVIOUS = ...  # type: int
KEY_PRINT = ...  # type: int
KEY_REDO = ...  # type: int
KEY_REFERENCE = ...  # type: int
KEY_REFRESH = ...  # type: int
KEY_REPLACE = ...  # type: int
KEY_RESET = ...  # type: int
KEY_RESIZE = ...  # type: int
KEY_RESTART = ...  # type: int
KEY_RESUME = ...  # type: int
KEY_RIGHT = ...  # type: int
KEY_SAVE = ...  # type: int
KEY_SBEG = ...  # type: int
KEY_SCANCEL = ...  # type: int
KEY_SCOMMAND = ...  # type: int
KEY_SCOPY = ...  # type: int
KEY_SCREATE = ...  # type: int
KEY_SDC = ...  # type: int
KEY_SDL = ...  # type: int
KEY_SELECT = ...  # type: int
KEY_SEND = ...  # type: int
KEY_SEOL = ...  # type: int
KEY_SEXIT = ...  # type: int
KEY_SF = ...  # type: int
KEY_SFIND = ...  # type: int
KEY_SHELP = ...  # type: int
KEY_SHOME = ...  # type: int
KEY_SIC = ...  # type: int
KEY_SLEFT = ...  # type: int
KEY_SMESSAGE = ...  # type: int
KEY_SMOVE = ...  # type: int
KEY_SNEXT = ...  # type: int
KEY_SOPTIONS = ...  # type: int
KEY_SPREVIOUS = ...  # type: int
KEY_SPRINT = ...  # type: int
KEY_SR = ...  # type: int
KEY_SREDO = ...  # type: int
KEY_SREPLACE = ...  # type: int
KEY_SRESET = ...  # type: int
KEY_SRIGHT = ...  # type: int
KEY_SRSUME = ...  # type: int
KEY_SSAVE = ...  # type: int
KEY_SSUSPEND = ...  # type: int
KEY_STAB = ...  # type: int
KEY_SUNDO = ...  # type: int
KEY_SUSPEND = ...  # type: int
KEY_UNDO = ...  # type: int
KEY_UP = ...  # type: int
OK = ...  # type: int
REPORT_MOUSE_POSITION = ...  # type: int
_C_API = ...  # type: Any
version = ...  # type: bytes


def baudrate() -> int:
    ...


def beep() -> None:
    ...


def can_change_color() -> bool:
    ...


def cbreak(flag: bool = ...) -> None:
    ...


def color_content(color_number: int) -> Tuple[int, int, int]:
    ...


def color_pair(color_number: int) -> int:
    ...


def curs_set(visibility: int) -> int:
    ...


def def_prog_mode() -> None:
    ...


def def_shell_mode() -> None:
    ...


def delay_output(ms: int) -> None:
    ...


def doupdate() -> None:
    ...


def echo(flag: bool = ...) -> None:
    ...


def endwin() -> None:
    ...


def erasechar() -> bytes:
    ...


def filter() -> None:
    ...


def flash() -> None:
    ...


def flushinp() -> None:
    ...


def getmouse() -> Tuple[int, int, int, int, int]:
    ...


def getsyx() -> Tuple[int, int]:
    ...


def getwin(f: BinaryIO) -> '_CursesWindow':
    ...


def halfdelay(tenths: int) -> None:
    ...


def has_colors() -> bool:
    ...


def has_ic() -> bool:
    ...


def has_il() -> bool:
    ...


def has_key(ch: int) -> bool:
    ...


def init_color(color_number: int, r: int, g: int, b: int) -> None:
    ...


def init_pair(pair_number: int, fg: int, bg: int) -> None:
    ...


def initscr() -> '_CursesWindow':
    ...


def intrflush(ch: bool) -> None:
    ...


def is_term_resized(nlines: int, ncols: int) -> bool:
    ...


def isendwin() -> bool:
    ...


def keyname(k: int) -> bytes:
    ...


def killchar() -> bytes:
    ...


def longname() -> bytes:
    ...


def meta(yes: bool) -> None:
    ...


def mouseinterval(interval: int) -> None:
    ...


def mousemask(mousemask: int) -> Tuple[int, int]:
    ...


def napms(ms: int) -> int:
    ...


def newpad(nlines: int, ncols: int) -> '_CursesWindow':
    ...


def newwin(nlines: int, ncols: int, begin_y: int = 0,
           begin_x: int = 0) -> '_CursesWindow':
    ...


def nl(flag: bool = ...) -> None:
    ...


def nocbreak() -> None:
    ...


def noecho() -> None:
    ...


def nonl() -> None:
    ...


def noqiflush() -> None:
    ...


def noraw() -> None:
    ...


def pair_content(pair_number: int) -> Tuple[int, int]:
    ...


def pair_number(attr: int) -> int:
    ...


def putp(string: bytes) -> None:
    ...


def qiflush(flag: bool = ...) -> None:
    ...


def raw(flag: bool = ...) -> None:
    ...


def reset_prog_mode() -> None:
    ...


def reset_shell_mode() -> None:
    ...


def resetty() -> None:
    ...


def resize_term(nlines: int, ncols: int) -> None:
    ...


def resizeterm(nlines: int, ncols: int) -> None:
    ...


def savetty() -> None:
    ...


def setsyx(y: int, x: int) -> None:
    ...


def setupterm(termstr: str = ..., fd: int = 0) -> None:
    ...


def start_color() -> None:
    ...


def termattrs() -> int:
    ...


def termname() -> bytes:
    ...


def tigetflag(capname: str) -> int:
    ...


def tigetnum(capname: str) -> int:
    ...


def tigetstr(capname: str) -> bytes:
    ...


def tparm(fmt: str,
          i1: int = 0,
          i2: int = 0,
          i3: int = 0,
          i4: int = 0,
          i5: int = 0,
          i6: int = 0,
          i7: int = 0,
          i8: int = 0,
          i9: int = 0) -> str:
    ...


def typeahead(fd: int) -> None:
    ...


def unctrl(ch: _chtype) -> bytes:
    ...


def unget_wch(ch: _chtype) -> None:
    ...


def ungetch(ch: _chtype) -> None:
    ...


def ungetmouse(id: int, x: int, y: int, z: int, bstate: int) -> None:
    ...


def update_lines_cols() -> int:
    ...


def use_default_colors() -> None:
    ...


def use_env(flag: bool) -> None:
    ...


class error(Exception):
    ...


def wrapper(func: Any, *args: Any, **kwds: Any) -> None:
    ...


class _CursesWindow:
    encoding = ...  # type: str

    @overload
    def addch(self, ch: _chtype, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def addch(self, y: int, x: int, ch: _chtype,
              attr: Optional[int] = 0) -> None:
        ...

    @overload
    def addnstr(self, str: str, n: int, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def addnstr(self,
                y: int,
                x: int,
                str: str,
                n: int,
                attr: Optional[int] = 0) -> None:
        ...

    @overload
    def addstr(self, str: str, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def addstr(self, y: int, x: int, str: str,
               attr: Optional[int] = 0) -> None:
        ...

    def attroff(self, attr: int) -> None:
        ...

    def attron(self, attr: int) -> None:
        ...

    def attrset(self, attr: int) -> None:
        ...

    def bkgd(self, ch: _chtype, attr: Optional[int] = 0) -> None:
        ...

    def bkgset(self, ch: _chtype, attr: Optional[int] = 0) -> None:
        ...

    def border(self,
               ls: Optional[int] = 0,
               rs: Optional[int] = 0,
               ts: Optional[int] = 0,
               bs: Optional[int] = 0,
               tl: Optional[int] = 0,
               tr: Optional[int] = 0,
               bl: Optional[int] = 0,
               br: Optional[int] = 0) -> None:
        ...

    def box(self, vertch: Optional[Tuple[int, int]],
            horch: Optional[Tuple[int, int]]) -> None:
        ...

    @overload
    def chgat(self, attr: int) -> None:
        ...

    @overload
    def chgat(self, num: int, attr: int) -> None:
        ...

    @overload
    def chgat(self, y: int, x: int, attr: int) -> None:
        ...

    @overload
    def chgat(self, y: int, x: int, num: int, attr: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def clearok(self, yes: int) -> None:
        ...

    def clrtobot(self) -> None:
        ...

    def clrtoeol(self) -> None:
        ...

    def cursyncup(self) -> None:
        ...

    @overload
    def delch(self) -> None:
        ...

    @overload
    def delch(self, y: int, x: int) -> None:
        ...

    def deleteln(self) -> None:
        ...

    @overload
    def derwin(self, begin_y: int, begin_x: int) -> '_CursesWindow':
        ...

    @overload
    def derwin(self, nlines: int, ncols: int, begin_y: int,
               begin_x: int) -> '_CursesWindow':
        ...

    def echochar(self, ch: _chtype, attr: Optional[int] = 0) -> None:
        ...

    def enclose(self, y: int, x: int) -> bool:
        ...

    def erase(self) -> None:
        ...

    def getbegyx(self) -> Tuple[int, int]:
        ...

    def getbkgd(self) -> Tuple[int, int]:
        ...

    def getch(self, y: Optional[int] = 0, x: Optional[int] = 0) -> _chtype:
        ...

    def get_wch(self, y: Optional[int] = 0, x: Optional[int] = 0) -> _chtype:
        ...

    def getkey(self, y: Optional[int] = 0, x: Optional[int] = 0) -> str:
        ...

    def getmaxyx(self) -> Tuple['_CursesWindow', int, int]:
        ...

    def getparyx(self) -> Tuple[int, int]:
        ...

    def getstr(self, y: Optional[int] = 0, x: Optional[int] = 0) -> None:
        ...

    def getyx(self) -> Tuple['_CursesWindow', int, int]:
        ...

    @overload
    def hline(self, ch: _chtype, n: int) -> None:
        ...

    @overload
    def hline(self, y: int, x: int, ch: _chtype, n: int) -> None:
        ...

    def idcok(self, flag: bool) -> None:
        ...

    def idlok(self, yes: bool) -> None:
        ...

    def immedok(self, flag: bool) -> None:
        ...

    def inch(self, y: Optional[int] = 0, x: Optional[int] = 0) -> _chtype:
        ...

    @overload
    def insch(self, ch: _chtype, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def insch(self, y: int, x: int, ch: _chtype,
              attr: Optional[int] = 0) -> None:
        ...

    def insdelln(self, nlines: int) -> None:
        ...

    def insertln(self) -> None:
        ...

    @overload
    def insnstr(self, str: str, n: int, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def insnstr(self,
                y: int,
                x: int,
                str: str,
                n: int,
                attr: Optional[int] = 0) -> None:
        ...

    @overload
    def insstr(self, str: str, attr: Optional[int] = 0) -> None:
        ...

    @overload
    def insstr(self, y: int, x: int, str: str,
               attr: Optional[int] = 0) -> None:
        ...

    @overload
    def instr(self, n: Optional[int] = 0) -> str:
        ...

    @overload
    def instr(self, y: int, x: int, n: Optional[int] = 0) -> str:
        ...

    def is_linetouched(self, line: int) -> bool:
        ...

    def is_wintouched(self) -> bool:
        ...

    def keypad(self, yes: bool) -> None:
        ...

    def leaveok(self, yes: bool) -> None:
        ...

    def move(self, new_y: int, new_x: int) -> None:
        ...

    def mvderwin(self, y: int, x: int) -> None:
        ...

    def mvwin(self, new_y: int, new_x: int) -> None:
        ...

    def nodelay(self, yes: bool) -> None:
        ...

    def notimeout(self, yes: bool) -> None:
        ...

    def noutrefresh(self) -> None:
        ...

    def overlay(self,
                destwin: '_CursesWindow',
                sminrow: Optional[int] = 0,
                smincol: Optional[int] = 0,
                dminrow: Optional[int] = 0,
                dmincol: Optional[int] = 0,
                dmaxrow: Optional[int] = 0,
                dmaxcol: Optional[int] = 0) -> None:
        ...

    def overwrite(self,
                  destwin: '_CursesWindow',
                  sminrow: Optional[int] = 0,
                  smincol: Optional[int] = 0,
                  dminrow: Optional[int] = 0,
                  dmincol: Optional[int] = 0,
                  dmaxrow: Optional[int] = 0,
                  dmaxcol: Optional[int] = 0) -> None:
        ...

    def putwin(self, file: IO[Any]) -> None:
        ...

    def redrawln(self, beg: int, num: int) -> None:
        ...

    def redrawwin(self) -> None:
        ...

    def refresh(self,
                pminrow: Optional[int] = 0,
                pmincol: Optional[int] = 0,
                sminrow: Optional[int] = 0,
                smincol: Optional[int] = 0,
                smaxrow: Optional[int] = 0,
                smaxcol: Optional[int] = 0) -> None:
        ...

    def resize(self, nlines: int, ncols: int) -> None:
        ...

    def scroll(self, lines: int) -> None:
        ...

    def scrollok(self, flag: bool) -> None:
        ...

    def setscrreg(self, top: int, bottom: int) -> None:
        ...

    def standend(self) -> None:
        ...

    def standout(self) -> None:
        ...

    @overload
    def subpad(self, begin_y: int, begin_x: int) -> '_CursesWindow':
        ...

    @overload
    def subpad(self, nlines: int, ncols: int, begin_y: int,
               begin_x: int) -> '_CursesWindow':
        ...

    @overload
    def subwin(self, begin_y: int, begin_x: int) -> '_CursesWindow':
        ...

    @overload
    def subwin(self, nlines: int, ncols: int, begin_y: int,
               begin_x: int) -> '_CursesWindow':
        ...

    def syncdown(self) -> None:
        ...

    def syncok(self, flag: bool) -> None:
        ...

    def syncup(self) -> None:
        ...

    def timeout(self, delay: int) -> None:
        ...

    def touchline(self, start: int, count: int,
                  changed: Optional[bool]) -> None:
        ...

    def touchwin(self) -> None:
        ...

    def untouchwin(self) -> None:
        ...

    @overload
    def vline(self, ch: _chtype, n: int) -> None:
        ...

    @overload
    def vline(self, y: int, x: int, ch: _chtype, n: int) -> None:
        ...
