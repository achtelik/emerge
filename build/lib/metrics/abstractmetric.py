"""
Defines AbstractMetric and relevant enums.
"""

# Authors: Grzegorz Lato <grzegorz.lato@gmail.com>
# License: MIT

from abc import ABC, abstractmethod
from typing import Any, Dict
from enum import Enum, unique, auto

from core.abstractresult import AbstractResult


class EnumLowerKebabCase(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):  # pylint: disable=unused-argument
        return str(name).lower().replace('_', '-')


@unique
class MetricKeys(EnumLowerKebabCase):

    # keys for metric names
    NUMBER_OF_METHODS = auto()
    SOURCE_LINES_OF_CODE = auto()
    FAN_IN_OUT = auto()


@unique
class MetricResultFilter(Enum):
    FILE_RESULTS = auto()
    ENTITY_RESULTS = auto()


class AbstractMetric(ABC):

    @property
    @abstractmethod
    def metric_name(self):
        ...

    @property
    @abstractmethod
    def pretty_metric_name(self):
        ...

    @property
    @abstractmethod
    def analysis(self):
        ...

    @property
    @abstractmethod
    def local_data(self):
        ...

    @property
    @abstractmethod
    def overall_data(self):
        ...

    @abstractmethod
    def calculate_from_results(self, results: Dict[str, AbstractResult]):
        ...


class AbstractGraphMetric(AbstractMetric):

    @property
    @abstractmethod
    def dependency_graph_representation(self) -> Any:
        ...

    @property
    @abstractmethod
    def inheritance_graph_representation(self) -> Any:
        ...

    @property
    @abstractmethod
    def complete_graph_representation(self) -> Any:
        ...

    @dependency_graph_representation.setter
    @abstractmethod
    def dependency_graph_representation(self, value):
        ...

    @inheritance_graph_representation.setter
    @abstractmethod
    def inheritance_graph_representation(self, value):
        ...

    @complete_graph_representation.setter
    @abstractmethod
    def complete_graph_representation(self, value):
        ...

    @abstractmethod
    def calculate_from_results(self, results: Dict[str, AbstractResult]):
        ...


class AbstractCodeMetric(AbstractMetric):

    @abstractmethod
    def calculate_from_results(self, results: Dict[str, AbstractResult]):
        ...
