# janssqlitekernel

![Logo](https://raw.githubusercontent.com/jans-code/janssqlitekernel/main/janssqlitekernel/logo-svg.svg)

A simple SQLite3 kernel for jupyter.
Created using IPython's kernel and pexpect's REPLWrapper subclasses.
You cannot span commands over multiple inputs.
If you forget a semicolon at the end, the kernel will append it for you.
This feature is disabled for the SQLite dot-commands.

## Installation

- install SQLite3 from your distro's package manager
- get the kernel module via pip
- `pip install janssqlitekernel`
- then install kernelspec
- `janssqlitekernel`

## Dev Installation

- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user janssqlitekernel`

## Uninstall

- `jupyter kernelspec uninstall janssqlitekernel`
- `pip uninstall janssqlitekernel`
