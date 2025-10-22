from dataclasses import dataclass
from typing import Set
from typing_extensions import Self


def frozen_dataclass(_cls=None, **kwargs):
  """ Decorator to create a frozen dataclass with eq disabled. """
  def _wrap(cls):
    return dataclass(frozen=True, eq=False, repr=False, **kwargs)(cls)
  if _cls is None:
    return _wrap 
  return _wrap(_cls)


@frozen_dataclass
class ImmutableData:
  """ Base class for immutable data objects. """
  def new(self, **kwargs) -> Self:
    return self.__class__(**{**self.__dict__, **kwargs})
  
  def __eq__(self, value) -> bool:
    return self is value
  
  def __ne__(self, value) -> bool:
    return not self.__eq__(value)

  def __exclude_repr__(self) -> Set[str]:
    """ Get a set of attributes to exclude from the repr. """
    return set()

  def __repr__(self) -> str:
    excludes = self.__exclude_repr__()
    return f'{self.__class__.__name__}(' + ', '.join(
      f'{k}={v!r}' for k, v in self.__dict__.items() if k not in excludes
    ) + f') at 0x{id(self):x}'
