from cartalog_server.data.classes import ImmutableData, frozen_dataclass


@frozen_dataclass
class DomainCategory(ImmutableData):
  name: str
  description: str
  uid: int = -1