# vscode-debug-mixed-python-cpp

Based on (this blog post)[https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code/]

## Setup

```
conda create --name myadd python=3.10
conda activate myadd
export CPATH=$CONDA_PREFIX/include/python3.10
```

```
cd src
python setup.py install
python myscript.py
```

```
code .
```

In VS code set Python interpreter to the `myadd` interpreter with
`Ctrl + Shift P` and then `Select Python Interpreter`.
