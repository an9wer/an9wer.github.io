Portable Shell Scripts are Unachievable (Draft)
===============================================

:Published: 2023-10-10

.. meta::
	:tags: thought
	:description: Bash is the most common shell on Linux, and I have been
		using it since my early days of learning Linux, but when I get
		into the world of BSD system, things are changed. The default
		shell is ash for FreeBSD, and ksh for OpenBSD. Although they all
		belong to Bourne family their syntax differs a lot. That means
		many of my Bash scripts that utilize features specific to Bash
		are not compatible to BSD system if I want to insist on BSD's
		default shell.

Bash is the most common shell on Linux, and I have been using it since my
early days of learning Linux, but when I get into the world of BSD system,
things are changed. The default shell is ash for FreeBSD, and ksh for
OpenBSD. Although they all belong to Bourne family (shown as the below picture),
their syntax differs a lot. That means many of my Bash scripts that utilize
features specific to Bash are not compatible to BSD system if I want to insist
on BSD's default shell.

.. image:: /statics/images/2023/10/shell-varieties.webp
       :width: 560px

If I only talk about the portability of the shell language itself, it still can
be achievable by following the POSIX (Portable Operating System Interface)
shell specifications, as most Bourne-family shells are compatible with POSIX.
Even though the POSIX shell has some limitations, it is still featured enough,
and syntatic sugar in Bash can be rewritten in the POSIX style.

For example, in Bash, for condition expressions quoted by ``[[``, there is no
need to use doube quotation for variables whose value include whitespaces.
That can be implemented in the POSIX shell, using ``[`` and quoting any
variables including whitespaces: ::

	$ v="a b"

	# in Bash
	$ [[ $v = "a b" ]]

	# in POSIX
	$ [ "$v" = "a b" ]

Another example is the rediction symbol ``|&`` in Bash, which pipes both
standard output and standard error, is just a shorthand for ``2>&1 |``: ::

	# in Bash
	$ MOZ_LOG="PlatformDecoderModule:5" firefox |& grep VA-VAPI

	# in POSIX
	$ MOZ_LOG="PlatformDecoderModule:5" firefox 2>&1 | grep VA-API"

However, portable shell scripts do not only mean using the shell language
compatible over different shell varieties, but also involve the portability of
programs external to the shell. Most shell scripts need to use a number of
programs other than the shell itself to achieve their ends. Compared to the
divergence in the functions and options offered by programs, the variance
of all the shell languages is relatively trivial.

In fact, the portability of external programs in shell scripts is the real
difficulty that I can not cope with in an easy way. Although POSIX has
specifications for various basic programs, such as ``find``, ``sed``, and so on,
I still got some programs not included in POSIX, or some limitations using only
POSIX defined options of a program.
