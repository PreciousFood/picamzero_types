
# PICAMZERO TYPES

Since picamera2 and picamzero do not support directly installing with pip, usage with virtual environments is trick. And while there are workarounds, the easy ones do not allow code editors such as vs code to provide type hinting and auto complete. This is a simple fix, simply put the `picamzero` folder in your directory, and type hints will be provided. 

> Note: This is not technically complete, but it is pleanty for average use. Contributions are welcome.

You will still need to install and setup picamzero, but once you have a working virtual environment, this folder will tell your editor the structure of the picamzero library. 

I use the following command (I have an alias in my .bashrc) to create a venv, add the types, and then activate the venv.
```bash
python -m venv --system-site-packages .venv && git clone https://github.com/PreciousFood/picamzero_types.git && mv picamzero_types/picamzero ./ && rm -rf picamzero_types && source .venv/bin/activate
```
