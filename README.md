# List of scripts
- bin_upper_edges.ipynb
- FESRConfigGenerator.py 

## bin_upper_edges.ipynb
Calculates and prints right corner of bins, which we use as fitting s0s. Bins bigger than m_\tau^2 (3.157) are not used.

## FESRConfigGenerator.py
Has two modes:
- normal-mode
- sparseS0s-mode
The *sparseS0s* mode can be activated by setting the variable `sparseS0s=True`. In every mode one has to configure the **configTemplate.thMomContribs**.

### normal-mode
In the *normal-mode* one defines a **weight** and the **maximum amount of s0s** manually. The script then generates every possible s0s variation.
#### Usage
Change *variables*, *s0s*, *weight* and *configTemplate* (*thMomContribs*). Then execute `python ../.../FESRConfigGenerator.py` from the directory, in which the *configuration.json* files should be created.

### sparseS0s-mode
In the *sparceS0s-mode* we do not use every s0s, but every **nth s0s**. It is helpful because Fits with more than ten s0s have problems in converging. E.g. if we have a list of `s0s = [3, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8]` and want only every 2nd element => `s0s = [3, 2.6, 2.2, 1.8]`.
#### Usage
Change `sparseS0s=True` and **variables**. Then in the lower part change the *range* for loop 
```
else:
    for i in range(1,9): # change range for different sparse settings
        s0sNum = 10
        weights = [1, 14, 15]
```
, the `s0SNum` and  the `weights`.
