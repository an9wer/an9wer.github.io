Invoking Tcl in C
=================

:published: 2023-12-08

.. meta::
        :tags: Tcl

In my pervious post, I was going to utilize a command-line tool - rsstail - into
a script to notify me of Slashdot news, but I finally changed my mind to writing
my own tool for monitoring and detecting new entries from Slashdot's RSS feeds.
I also decided to use the Tcl programming language for this task because of its
simplicity and portability.

The only challange is that Tcl doesn't support running itself as a daemon
service in the background, unless using extra libraries (e.g. tcllauncher) or
TclX (Extended Tcl), but Tcl is written in C and provides C APIs for calling it
from C, in which I can fork a service in daemon mode.

Writing C codes to invoke a Tcl script file
-------------------------------------------

I have implemented my tool in a Tcl script file, the next is to invoke the
script file from C, in which several key APIs are supposed to be called.

The first API is to create a Tcl interpreter structure, which is taken as a
parameter for the most C APIs: ::

	Tcl_Interp *interp = Tcl_CreateInterp();

After creating the Tcl interpreter, call ``Tcl_Init`` to read "init.tcl" from
the Tcl script library to set up the script library facility, such that you are
able to import packages properly from your Tcl script file (e.g. ``package
require http``): ::

	Tcl_Init(interp);

Lastly, reads the given Tcl script file and evaluates its contents: ::

	Tcl_EvalFile(interp, <FILENAME>);

Compiling C codes
-----------------

To compile C code, it is supposed to specify the include path, where the
"tcl.h" locates (i.e. "/usr/local/include/tcl8.6" in my case), and the library
path, where the "libtcl.so" file locates (i.e. "/usr/local/lib" in my case).
Also, some Tcl packages (e.g. http) relies on the pthread library, otherwise
an error ``undefined symbol 'pthread_attr_init'`` will raise: ::

	cc -Wl,-L,/usr/local/lib,-l,tcl86,-l,pthread -I/usr/local/include/tcl8.6 <C FILES>

Thanks for reading :)
