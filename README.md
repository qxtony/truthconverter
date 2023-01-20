<h1 align="center" name="name">TruthConverter</h1>
<p align="center">
    <em>
        TruthConverter — a library for creating truth tables.<br>
        With Truth Converter, you can create truth tables with all available logical operations.
    </em>
</p>



Install and go to the folder:

```bash
git clone https://github.com/qxtony/truthconverter.git
cd truthconverter
```

To start the program, enter the following:
```sh
python -m truthtable
```

The following operations are supported:</br>
& - and</br>
| - or</br>
! - not</br>
_ - following</br>

## Example:

This program is to compile a truth table by the expression:
```python
from app import Truth

truth: Truth = Truth("(X | Y) & (Y == Z) & !W")
print(str(truth))
```
