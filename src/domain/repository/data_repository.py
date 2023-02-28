from typing import TypeVar, Union
from repository_constants import RepositoryErrorConstants
from src.domain.event.event import Event
from src.domain.statistic.statistic import Statistic

#TODO: decide if events or statistics(stateful translation of an event?) should be stored
T = TypeVar("T", bound = Union[Statistic, Event])
class DataRepository:

    def save(self, statistic: T):
        raise NotImplementedError(RepositoryErrorConstants.method_not_implemented.format("save"))

    def retrieve(self, id: str) -> T:
        raise NotImplementedError(RepositoryErrorConstants.method_not_implemented.format("retrieve"))