# QGIS Algorithms (version 3.12)

Execute QGIS algorithms outside of QGIS GUI

## Requirements

- python 3.6+
- QGIS 3.12+

## Installation

Ubuntu 18.04    
- `python3`
```
sudo apt-get install python3
```

- `QGIS 3.12`   
1. add the following to **/etc/apt/sources.list**
```
deb https://qgis.org/ubuntu bionic main
```

2. add qgis.org repository public key to your apt keyring
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 51F523511C7028C3
```

3. install QGIS - see QGIS official [installation](https://qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu) page
```
sudo apt-get update
sudo apt-get install qgis qgis-plugin-grass
```

4. add to your **.bashrc** or **.bash_profile**
```
export PYTHON_PATH=/usr/share/qgis/python

# for GPU-less machines
export QT_QPA_PLATFORM='offscreen'
```

## Modules

### Help
- [display algorithm usage](READMEs/display_algorithm_usage.py.md)      
(`opened an issue on Github for character encoding related crash`)
- [list algorithms](READMEs/list_algorithms.py.md)

### Algorithms
- [add autoincremental field](READMEs/add_autoincremental_field.py.md)
- [create grid](READMEs/create_grid.py.md)
- [join attributes by location](READMEs/join_attributes_by_location.py.md)
- [polygon from layer extent](READMEs/polygon_from_layer_extent.py.md)
- [simplify geometries](READMEs/simplify_geometries.py.md)
- [split with lines](READMEs/split_with_lines.py.md)

## TODOs

- Use argparse.ArgumentParser
