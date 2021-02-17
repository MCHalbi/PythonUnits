# This file was created automatically. Every change made in this file will be
# lost when the package is built the next time.
#
# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2020 - 2021
from ..units import MassUnit


class Mass:
    base_unit = MassUnit.KILOGRAM
    factors = {
        MassUnit.CENTIGRAM: 1e-5,
        MassUnit.DECAGRAM: 1e-2,
        MassUnit.DECIGRAM: 1e-4,
        MassUnit.EARTHMASS: 5.9723e24,
        MassUnit.GIGATONNE: 1e12,
        MassUnit.GRAIN: 6.479891e-5,
        MassUnit.GRAM: 1e-3,
        MassUnit.HECTOGRAM: 1e-1,
        MassUnit.KILOGRAM: 1e0,
        MassUnit.KILOPOUND: 4.53592370e2,
        MassUnit.KILOTONNE: 1e6,
        MassUnit.LONGHUNDREDWEIGHT: 50.80234544,
        MassUnit.LONGTON: 1016.0469088,
        MassUnit.MEGAPOUND: 4.53592370e5,
        MassUnit.MEGATONNE: 1e9,
        MassUnit.MICROGRAM: 1e-9,
        MassUnit.MILLIGRAM: 1e-6,
        MassUnit.NANOGRAM: 1e-12,
        MassUnit.OUNCE: 2.8349523125e-2,
        MassUnit.POUND: 4.53592370e-1,
        MassUnit.SHORTHUNDREDWEIGHT: 45.359237,
        MassUnit.SHORTTON: 907.18474,
        MassUnit.SOLARMASS: 1.98892e30,
        MassUnit.STONE: 6.35029318,
        MassUnit.TONNE: 1e3,
    }
    abbreviations = {
        MassUnit.CENTIGRAM: 'cg',
        MassUnit.DECAGRAM: 'dag',
        MassUnit.DECIGRAM: 'dg',
        MassUnit.EARTHMASS: 'M⊕',
        MassUnit.GIGATONNE: 'Gt',
        MassUnit.GRAIN: 'gr.',
        MassUnit.GRAM: 'g',
        MassUnit.HECTOGRAM: 'hg',
        MassUnit.KILOGRAM: 'kg',
        MassUnit.KILOPOUND: 'klb.',
        MassUnit.KILOTONNE: 'kt',
        MassUnit.LONGHUNDREDWEIGHT: 'cwt.',
        MassUnit.LONGTON: 'to.',
        MassUnit.MEGAPOUND: 'Mlb.',
        MassUnit.MEGATONNE: 'Mt',
        MassUnit.MICROGRAM: 'μg',
        MassUnit.MILLIGRAM: 'mg',
        MassUnit.NANOGRAM: 'ng',
        MassUnit.OUNCE: 'oz.',
        MassUnit.POUND: 'lb.',
        MassUnit.SHORTHUNDREDWEIGHT: 'cwt.',
        MassUnit.SHORTTON: 'to.',
        MassUnit.SOLARMASS: 'M☉',
        MassUnit.STONE: 'st.',
        MassUnit.TONNE: 't',
    }

    def __init__(self, value: float, unit: 'MassUnit') -> None:
        self._value = value
        self._unit = unit

    def __str__(self):
        return "{value} {unit}".format(
            value=str(self._value),
            unit=Mass.abbreviations[self._unit])

    def __repr__(self):
        return str(self)

    # Comparison operators
    def __eq__(self, other):
        return self._value == other.as_unit(self._unit)

    # Unary operators
    def __neg__(self):
        return Mass(-self._value, self._unit)

    # Arithmetic operators
    def __add__(self, other):
        if type(other) is Mass:
            return Mass(self._value + other.as_unit(self._unit), self._unit)

        self._raise_type_error_for_undefined_operator(other, '+')

    def __sub__(self, other):
        if type(other) is Mass:
            return Mass(self._value - other.as_unit(self._unit), self._unit)

        self._raise_type_error_for_undefined_operator(other, '-')

    def __mul__(self, other):

        if type(other) in (float, int):
            result = Mass(self._value * other, self._unit)
        else:
            self._raise_type_error_for_undefined_operator(other, '*')

        return result

    def __rmul__(self, other):

        if type(other) in (float, int, ):
            return self * other

        self._raise_type_error_for_undefined_operator(other, '*')

    def __truediv__(self, other):

        if type(other) is Mass:
            result = (self._get_value_in_base_unit()
                    / other.as_unit(other.base_unit))
        elif type(other) in (float, int):
            result = Mass(self._value / other, self._unit)
        else:
            self._raise_type_error_for_undefined_operator(other, '/')

        return result

    def __pow__(self, other):
        if type(other) in (float, int):
            result = 1
            for _ in range(other):
              result *= self

            return result
        else:
            self._raise_type_error_for_undefined_operator(other, '**')

    def _raise_type_error_for_undefined_operator(
            self, other, operator: str) -> None:
        raise TypeError(
            'unsupported operand type(s) for {0}: \'{1}\' and \'{2}\''
            .format(operator, type(self).__name__, type(other).__name__))

    @staticmethod
    def zero() -> 'Mass':
        return Mass(0, Mass.base_unit)

    @property
    def unit(self) -> MassUnit:
        return self._unit

    @property
    def value(self) -> float:
        return self._value

    def as_unit(self, unit: MassUnit) -> float:
        if unit == self._unit:
            return self._value

        return self._get_value_as(unit)

    def to_unit(self, unit: MassUnit) -> 'Mass':
        converted_value = self._get_value_as(unit)

        return Mass(converted_value, unit)

    # Generation shorthands
    @staticmethod
    def from_centigrams(value: float) -> 'Mass':
        return Mass(value, MassUnit.CENTIGRAM)

    @staticmethod
    def from_decagrams(value: float) -> 'Mass':
        return Mass(value, MassUnit.DECAGRAM)

    @staticmethod
    def from_decigrams(value: float) -> 'Mass':
        return Mass(value, MassUnit.DECIGRAM)

    @staticmethod
    def from_earth_masses(value: float) -> 'Mass':
        return Mass(value, MassUnit.EARTHMASS)

    @staticmethod
    def from_gigatonnes(value: float) -> 'Mass':
        return Mass(value, MassUnit.GIGATONNE)

    @staticmethod
    def from_grains(value: float) -> 'Mass':
        return Mass(value, MassUnit.GRAIN)

    @staticmethod
    def from_grams(value: float) -> 'Mass':
        return Mass(value, MassUnit.GRAM)

    @staticmethod
    def from_hectograms(value: float) -> 'Mass':
        return Mass(value, MassUnit.HECTOGRAM)

    @staticmethod
    def from_kilograms(value: float) -> 'Mass':
        return Mass(value, MassUnit.KILOGRAM)

    @staticmethod
    def from_kilopounds(value: float) -> 'Mass':
        return Mass(value, MassUnit.KILOPOUND)

    @staticmethod
    def from_kilotonnes(value: float) -> 'Mass':
        return Mass(value, MassUnit.KILOTONNE)

    @staticmethod
    def from_long_hundredweights(value: float) -> 'Mass':
        return Mass(value, MassUnit.LONGHUNDREDWEIGHT)

    @staticmethod
    def from_long_tons(value: float) -> 'Mass':
        return Mass(value, MassUnit.LONGTON)

    @staticmethod
    def from_megapounds(value: float) -> 'Mass':
        return Mass(value, MassUnit.MEGAPOUND)

    @staticmethod
    def from_megatonnes(value: float) -> 'Mass':
        return Mass(value, MassUnit.MEGATONNE)

    @staticmethod
    def from_micrograms(value: float) -> 'Mass':
        return Mass(value, MassUnit.MICROGRAM)

    @staticmethod
    def from_milligrams(value: float) -> 'Mass':
        return Mass(value, MassUnit.MILLIGRAM)

    @staticmethod
    def from_nanograms(value: float) -> 'Mass':
        return Mass(value, MassUnit.NANOGRAM)

    @staticmethod
    def from_ounces(value: float) -> 'Mass':
        return Mass(value, MassUnit.OUNCE)

    @staticmethod
    def from_pounds(value: float) -> 'Mass':
        return Mass(value, MassUnit.POUND)

    @staticmethod
    def from_short_hundredweights(value: float) -> 'Mass':
        return Mass(value, MassUnit.SHORTHUNDREDWEIGHT)

    @staticmethod
    def from_short_tons(value: float) -> 'Mass':
        return Mass(value, MassUnit.SHORTTON)

    @staticmethod
    def from_solar_masses(value: float) -> 'Mass':
        return Mass(value, MassUnit.SOLARMASS)

    @staticmethod
    def from_stones(value: float) -> 'Mass':
        return Mass(value, MassUnit.STONE)

    @staticmethod
    def from_tonnes(value: float) -> 'Mass':
        return Mass(value, MassUnit.TONNE)

    # Conversion shorthands
    @property
    def centigrams(self) -> float:
        return self.as_unit(MassUnit.CENTIGRAM)

    @property
    def decagrams(self) -> float:
        return self.as_unit(MassUnit.DECAGRAM)

    @property
    def decigrams(self) -> float:
        return self.as_unit(MassUnit.DECIGRAM)

    @property
    def earth_masses(self) -> float:
        return self.as_unit(MassUnit.EARTHMASS)

    @property
    def gigatonnes(self) -> float:
        return self.as_unit(MassUnit.GIGATONNE)

    @property
    def grains(self) -> float:
        return self.as_unit(MassUnit.GRAIN)

    @property
    def grams(self) -> float:
        return self.as_unit(MassUnit.GRAM)

    @property
    def hectograms(self) -> float:
        return self.as_unit(MassUnit.HECTOGRAM)

    @property
    def kilograms(self) -> float:
        return self.as_unit(MassUnit.KILOGRAM)

    @property
    def kilopounds(self) -> float:
        return self.as_unit(MassUnit.KILOPOUND)

    @property
    def kilotonnes(self) -> float:
        return self.as_unit(MassUnit.KILOTONNE)

    @property
    def long_hundredweights(self) -> float:
        return self.as_unit(MassUnit.LONGHUNDREDWEIGHT)

    @property
    def long_tons(self) -> float:
        return self.as_unit(MassUnit.LONGTON)

    @property
    def megapounds(self) -> float:
        return self.as_unit(MassUnit.MEGAPOUND)

    @property
    def megatonnes(self) -> float:
        return self.as_unit(MassUnit.MEGATONNE)

    @property
    def micrograms(self) -> float:
        return self.as_unit(MassUnit.MICROGRAM)

    @property
    def milligrams(self) -> float:
        return self.as_unit(MassUnit.MILLIGRAM)

    @property
    def nanograms(self) -> float:
        return self.as_unit(MassUnit.NANOGRAM)

    @property
    def ounces(self) -> float:
        return self.as_unit(MassUnit.OUNCE)

    @property
    def pounds(self) -> float:
        return self.as_unit(MassUnit.POUND)

    @property
    def short_hundredweights(self) -> float:
        return self.as_unit(MassUnit.SHORTHUNDREDWEIGHT)

    @property
    def short_tons(self) -> float:
        return self.as_unit(MassUnit.SHORTTON)

    @property
    def solar_masses(self) -> float:
        return self.as_unit(MassUnit.SOLARMASS)

    @property
    def stones(self) -> float:
        return self.as_unit(MassUnit.STONE)

    @property
    def tonnes(self) -> float:
        return self.as_unit(MassUnit.TONNE)

    def _to_base_unit(self) -> 'Mass':
        return self.to_unit(self.base_unit)

    def _get_value_in_base_unit(self) -> float:
        try:
            return self._value * Mass.factors[self._unit]
        except KeyError:
            raise NotImplementedError(
                'Can not convert {0} to base units.'.format(self._unit.name))

    def _get_value_as(self, unit: MassUnit) -> float:
        base_unit_value = self._get_value_in_base_unit()

        try:
            return base_unit_value / Mass.factors[unit]
        except KeyError:
            raise NotImplementedError(
                'Can not convert {0} to {1}.'.format(self._unit.name, unit))
