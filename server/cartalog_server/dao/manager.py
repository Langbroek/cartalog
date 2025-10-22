import sqlite3
from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from flask import g, current_app


def get_db() -> Connection:
  """ Get a database connection from the Flask global context. """
  if not 'database' in g:
    g.database = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.execute('PRAGMA foreign_keys = ON')
    g.database.row_factory = sqlite3.Row
    sqlite3.register_adapter(bool, int)
    sqlite3.register_converter('BOOL', lambda v: bool(int(v)))
  return g.database
    

@dataclass(frozen=True)
class NoneCursor(Cursor):
  """ A no-op database connection for use in functions that may not need a database. """
  def __init__(self, *args, **kwargs) -> None:
    pass

  def __getattribute__(self, name: str):
    if name in ('execute', 'executemany', 'executescript', 'fetchall', 'fetchmany', 'fetchone', 
                'setinputsizes', 'setoutputsize', '__iter__', '__next__', 'close'):
      raise RuntimeError('Attempted to use a NoneCursor')
    return super().__getattribute__(name)


