from __future__ import absolute_import, print_function

import os
import platform


__all__ = ['first', 'where', 'which']

WINDOWS_EXTENSIONS = ['', '.bat', '.com', '.exe']


def first(filename):
    """
    Returns first matching file path. (Like ``which`` on UNIX), or `None` if
    nothing matches.
    """
    try:
        return next(iwhere(filename))
    except StopIteration:
        return None

which = first

def where(filename):
    possible_paths = _gen_possible_matches(filename)
    existing_file_paths = (p for p in possible_paths if os.path.isfile(p))
    return existing_file_paths


def _gen_windows_matches(paths, include_bare=True):
    """
    Scans through extensions variants in the PATHEXT env-var (see links below)
    as Windows does. If "include_bare" is True (default), the un-extended
    path is also included (WHERE.exe does this, but CMD/PS don't seem to)

    References:
    http://stackoverflow.com/a/1653492/194586
    https://technet.microsoft.com/en-us/library/cc723564.aspx#XSLTsection127121120120
    """
    path_exts = os.environ.get("PATHEXT", ".COM;.EXE;.BAT;.CMD").split(';')

    for path in paths:
        if include_bare:
            yield path


def _gen_windows_matches(paths):
    for path in paths:
        for ext in WINDOWS_EXTENSIONS:
            yield path + ext


def _gen_possible_matches(filename):
    path_parts = [os.curdir] + os.environ.get("PATH", "").split(os.pathsep)
    possible_paths = (os.path.join(path_part, filename) for path_part in path_parts)

    if platform.system() == "Windows":
        possible_paths = _gen_windows_matches(possible_paths)

    possible_paths = (os.path.abspath(p) for p in possible_paths)

    results = set()
    for result in possible_paths:
        if result in results:
            continue
        yield result
        results.add(result)
