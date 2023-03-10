#!/usr/bin/python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager
json = """{"argv":["python","-m","janssqlitekernel", "-f", "{connection_file}"],
 "display_name":"SQLite3"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   version="1.1"
   width="300"
   height="300"
   id="svg2985"
   xml:space="preserve"
   sodipodi:docname="SQLite370.svg"
   inkscape:version="1.2.2 (732a01da63, 2022-12-09)"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/"><sodipodi:namedview
     id="namedview16"
     pagecolor="#505050"
     bordercolor="#ffffff"
     borderopacity="1"
     inkscape:showpageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="1"
     inkscape:deskcolor="#505050"
     showgrid="false"
     inkscape:zoom="1.5791479"
     inkscape:cx="211.8231"
     inkscape:cy="189.34262"
     inkscape:window-width="1920"
     inkscape:window-height="1009"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     inkscape:current-layer="svg2985" /><title
     id="title2998">SQLite</title><metadata
     id="metadata2991"><rdf:RDF><cc:Work
         rdf:about=""><dc:format>image/svg+xml</dc:format><dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" /><dc:title>SQLite</dc:title></cc:Work></rdf:RDF></metadata><defs
     id="defs2989"><linearGradient
       x1="0"
       y1="0"
       x2="1"
       y2="0"
       id="linearGradient3027"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(-4.02e-6,-91.8907,-91.8907,4.02e-6,85.8809,161.434)"
       spreadMethod="pad"><stop
         id="stop3029"
         style="stop-color:#97d9f6;stop-opacity:1"
         offset="0" /><stop
         id="stop3031"
         style="stop-color:#0f80cc;stop-opacity:1"
         offset="0.92024499" /><stop
         id="stop3033"
         style="stop-color:#0f80cc;stop-opacity:1"
         offset="1" /></linearGradient><linearGradient
       x1="-15.614694"
       y1="-9.1082983"
       x2="-6.7410073"
       y2="-9.1082983"
       id="linearGradient5421"
       xlink:href="#linearGradient3027"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(-4.02e-7,-9.18907,-9.18907,4.02e-7,8.58809,16.1434)"
       spreadMethod="pad" /><linearGradient
       x1="-15.614694"
       y1="-9.1082983"
       x2="-6.7410073"
       y2="-9.1082983"
       id="linearGradient2995"
       xlink:href="#linearGradient3027"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(-5.025e-7,11.486337,-11.486337,-5.025e-7,-30.839638,202.18698)"
       spreadMethod="pad" /></defs><g
     id="g409"
     transform="matrix(1.8665262,0,0,1.8665262,-0.99492966,-16.664441)"><rect
       style="fill:#faf8ea;stroke-width:37.7953;stroke-linecap:round;stroke-miterlimit:7"
       id="rect351"
       width="131.39999"
       height="132.98309"
       x="12.031805"
       y="18.047709"
       ry="12.830343" /><path
       d="M 121.6315,17.03623 H 22.1255 C 15.4565,17.03623 10,22.49373 10,29.16248 v 109.7365 c 0,6.66837 5.4565,12.125 12.1255,12.125 H 87.66275 C 86.918884,118.41477 98.054499,55.130402 121.6315,17.03623 Z"
       id="solid-background"
       style="fill:#0f80cc;fill-opacity:1;fill-rule:nonzero;stroke:none" /><path
       d="m 118.0165,20.57373 h -95.891 c -4.735375,0 -8.588875,3.8525 -8.588875,8.58875 v 101.73013 c 21.71725,-8.335 54.31221,-15.5269 76.849585,-15.20027 4.52893,-23.680901 17.83941,-70.090424 27.63029,-95.11861 z"
       id="gradient-background"
       style="fill:url(#linearGradient2995);fill-opacity:1;fill-rule:nonzero;stroke:none" /><path
       d="m 144.8415,13.44498 c -6.815,-6.0775 -15.06625,-3.63625 -23.21,3.59125 -1.20875,1.07375 -2.415,2.265 -3.615,3.5375 -13.93125,14.77875 -26.8625,42.15375 -30.88,63.06 1.565,3.17375 2.7875,7.22375 3.5925,10.3175 0.20625,0.79375 0.3925,1.53875 0.54125,2.1725 0.35375,1.499875 0.54375,2.4725 0.54375,2.4725 0,0 -0.125,-0.472625 -0.6375,-1.95875 -0.0975,-0.285 -0.20625,-0.59625 -0.335,-0.9625 -0.055,-0.15125 -0.13125,-0.335 -0.215,-0.53125 -0.90875,-2.1125 -3.4225,-6.57125 -4.52875,-8.5125 -0.94625,2.79125 -1.7825,5.4025 -2.4825,7.765 3.19375,5.8435 5.14,15.85775 5.14,15.85775 0,0 -0.16875,-0.649 -0.97125,-2.91412 -0.7125,-2.00338 -4.26125,-8.22113 -5.101875,-9.674755 -1.438,5.308505 -2.009375,8.892505 -1.494125,9.765125 1.000375,1.69088 1.953125,4.60838 2.78975,7.83488 1.89,7.26862 3.20375,16.11725 3.20375,16.11725 0,0 0.0425,0.58637 0.11375,1.48875 -0.2625,6.104 -0.105,12.43262 0.3675,18.15287 0.62625,7.57225 1.805,14.07713 3.3075,17.5585 l 1.02,-0.55612 c -2.20625,-6.85888 -3.1025,-15.84763 -2.71,-26.21388 0.59375,-15.84512 4.24,-34.95362 10.9775,-54.87 11.3825,-30.065 27.175,-54.1875 41.62875,-65.7075 -13.17375,11.8975 -31.00375,50.40875 -36.34125,64.67 -5.97625,15.97 -10.21125,30.95638 -12.76375,45.31475 4.40375,-13.46087 18.6425,-19.247 18.6425,-19.247 0,0 6.98375,-8.61287 15.145,-20.91775 -4.88875,1.115 -12.91625,3.02375 -15.605,4.15375 -3.96625,1.66375 -5.035,2.23125 -5.035,2.23125 0,0 12.8475,-7.82375 23.87,-11.36625 15.15875,-23.875 31.67375,-57.7925 15.0425,-72.62875"
       id="feather"
       style="fill:#003b57;fill-opacity:1;fill-rule:nonzero;stroke:none" /></g></svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/janssqlitekernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janssqlitekernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janssqlitekernel')