#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janssqlitekernel
IPKernelApp.launch_instance(kernel_class=janssqlitekernel)