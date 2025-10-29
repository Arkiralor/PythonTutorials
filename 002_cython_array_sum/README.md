# CYthon Implementations


## Setup

### Prequisites

1. `sudo apt-get install python3-dev` (for Debian-based systems)
2. `../scripts/install.sh` to install required Python packages.

To run the setup, do not depend on the script.
Instead, run the following command from inside the `002_cython_array_sum` directory:

```bash
python setup.py build_ext --inplace
```