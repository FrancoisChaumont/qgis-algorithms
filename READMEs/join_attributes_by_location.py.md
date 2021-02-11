# Join attributes by location

Join attributes from a location layer to matching/non-matching location of a shape layer

## Requirements & Installation

See [README.md](../README.md)

## Usage

### Arguments

|Argument|Summary|Description|Optional|Default|Type|
|-|-|-|-|-|-|
|`-h/--help`|display help|display detailed usage and examples|✔|||
|`--layer`|join layer file path (absolute)|layer to join input attributes with (format `gpkg`, `geojson`, `kml`, `shp`)|||string|
|`--layername`|join layer name|join layer name used in the output file name|||string|
|`--layerfields`|join layer fields|join layer fields (`space separated`) to join append to input file (e.g.: 'fid name')|||string|
|`--indir`|input directory (absolute)|input data directory path|||string|
|`--inpat`|input files pattern|input data files pattern to process several files|||string|
|`--indel`|input data delimiter|input data file delimiter|✔|,|string|
|`--inxfield`|input X field column|input data `X` field column (`longitude`)|||string|
|||column name when headers present (lng) or 'field_#' (field_3)||||
|`--inyfield`|input Y field column|input data `Y` field column (`latitude`)|||string|
|||column name when headers present (lat) or 'field_#' (field_2)||||
|`--incrs`|input CRS|input data CRS|✔|4326|integer|
|`--innoheaders`|input has no headers|input data files have no headers|✔|||
|`--outdir`|output directory (absolute)|output data directory path|||string|
|`--jointype`|join type|type of the final joined layer:|✔|1|integer|
|||0 - Create separate feature for each matching feature (one-to-many)||||
|||1 - Take attributes of the first matching feature only (one-to-one)||||
|`--nonmatching`|non matching|output non matching only|✔|||
|`--geopredicate`|geometric predicate|geometric predicate criteria (`space separated`):|✔|5|integer|
|||0 - intersect||||
|||1 - contain||||
|||2 - equal||||
|||3 - touch||||
|||4 - overlap||||
|||5 - within (similar to 0 but seems faster)||||
|||6 - cross|||

### Examples

See [tests.tar.gz](../tests/tests.tar.gz) for sample files to run tests on

`Join no-header location with highways appending attribute fid`
```
python3 join_attributes_by_location.py \
    --layer $PWD/../tests/highways-buffered.gpkg \
    --layername highways-no-headers \
    --layerfields fid \
    --indir $PWD/../tests \
    --inpat test.no-headers.csv \
    --indel , \
    --inxfield field_2 \
    --inyfield field_1 \
    --incrs 4326 \
    --innoheaders \
    --outdir $PWD/../tests \
    --jointype 1 \
    --geopredicate 0
```

`Same example with headers using default values`
```
python3 join_attributes_by_location.py \
    --layer $PWD/../tests/highways-buffered.geojson \
    --layername highways-headers \
    --layerfields fid \
    --indir $PWD/../tests \
    --inpat test.headers.csv \
    --inxfield lng \
    --inyfield lat \
    --outdir $PWD/../tests
```

### Output

Write matching or non-matching lines to a `csv` file under the `output directory` named after the `input file` with a `suffix` based on the `layer name`

Using input file `tests.csv` and layer name `highways`
- `matching`: tests.highways.csv
- `non-matching`: tests.highways.non-matching.csv

## Documentation

https://docs.qgis.org/3.10/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location

## TODOs

- allow multiple join layers
- parallelization??
