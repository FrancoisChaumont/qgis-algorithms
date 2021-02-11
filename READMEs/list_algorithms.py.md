# List algorithms

List all QGIS algorithms available from their libraries

## Requirements & Installation

See [README.md](../README.md)

## Usage

### Examples

```
python3 list_algorithms.py
python3 list_algorithms.py | grep '^gdal:'
python3 list_algorithms.py | grep '^grass7:'
python3 list_algorithms.py | grep '^native:'
python3 list_algorithms.py | grep '^qgis:'
```

### Output

Display a list of algorithms ID and name
```
gdal:aspect -> Aspect
grass7:i.albedo -> i.albedo
native:addautoincrementalfield -> Add autoincremental field
qgis:advancedpythonfieldcalculator -> Advanced Python field calculator
...
```

