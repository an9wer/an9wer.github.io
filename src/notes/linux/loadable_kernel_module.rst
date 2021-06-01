.. meta::
    :robots: noindex

Linux loadable kernel module
============================

Linux kernel modules can be loaded/unloaded in runtime, which allows for
smaller core kernel images and more flexibles systems.

Normally, kernel modules are located at `/usr/modules/$(uname -r)/kernel``
directory.

Built-in vs module
------------------

Built-in:
    Building a function into the kernel directly ensures that that function
    will be available at all times. The downside is that it makes your kernel
    bigger, increasing boot time, and ultimately using that much more memory to
    hold the kernel. If you are compiling a kernel to fit on a floppy so that
    you can boot Linux off a rescue floppy, space will become an issue.

Modules:
    Building a function as a module allows that function to be loaded into
    memory as needed and unloaded when it is no longer needed. This helps keep
    your kernel small. It is very useful if, say, you are swapping hardware in
    and out of your system frequently. You could compile support for a variety
    of, say, sound cards as modules, and your Linux system will theoretically
    only load the driver that is appropriate for the hardware setup at the
    time.

    Another benefit of building functions as modules is that parameters can be
    passed to the modules which can be useful in debugging your system if
    problems occur.

There are some considerations to be made when deciding if a kernel function
should be modularized. A small performance penalty is paid as it takes a little
time to get the module loaded and unloaded. There are some functions that are
needed at boot time and these cannot be compiled as modules -- they need to be
present in the kernel so your system can be loaded. For example,
ext2/ext3/reiserfs file system support needs to be built into the kernel so
that your partitions can be read, as you need to be able to read the filesystem
to load modules. In my case, if I have PCMCIA support built into the kernel,
then metworking works. If PCMCIA support is modularized, networking fails to
start, probably because the PCMCIA support needs to be available very early in
the boot process to set up networking.

References
----------

`Wikipedia: loadable kernel module
<https://en.wikipedia.org/wiki/Loadable_kernel_module>`_

`Built-in or module
<https://www.linuxquestions.org/questions/linux-software-2/built-in-or-module-any-difference-243255/>`_
