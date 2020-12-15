# AllYourUnitAreBelongToUs

## Installation

```
pip install ayuabtu
```

## Using
### Creating quantities
Creating a quantity with a given unit:
```python
>>> from ayuabtu.quantities import Length
>>> from ayuabtu.units import LengthUnit
>>> Length(2, LengthUnit.METER)
2 m
```
or you can use the unit specific factory method:
```python
>>> from ayuabtu.quantities import Length
>>> Length.FromMeters(2)
2 m
```

### Converting units
```python
>>> from ayuabtu.quantities import Length
>>> from ayuabtu.units import LengthUnit
>>> Length(2, LengthUnit.METER)
>>> distance_metric = Length.FromMeters(2)
>>> distance_metric.to_unit(LengthUnit.FOOT)
6.561679790026246 ft
```

## Custom Units
