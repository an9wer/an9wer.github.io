Video Acceleration on Gentoo
============================

:Published: 2023/09/27

.. meta::
	:description: At least for the recent months, I have been used to
		spending my free time watching videos on my laptop, and since my
		laptop has an integrated GPU, AMD Radeon Vega 8, I was thinking
		about what if I can accelerate video processing using GPU and
		reduce the load of CPU.

At least for the recent months, I have been used to spending my free time
watching videos on my laptop, and since my laptop has an integrated GPU, AMD
Radeon Vega 8, I was thinking about what if I can accelerate video processing
using GPU and reduce the load of CPU.

The media players that I mostly use to watch videos are Firefox (for online
videos) and `MPV`_ (for offline videos), and referring to the list of video
acceleration support between different applications [#]_, the only method
that is supported by both Firefox and MPV is VA-API, which is

	an open source application programming interface that allows
	applications such as VLC media player or GStreamer to use hardware video
	acceleration capabilities, usually provided by the graphics processing
	unit (GPU). [#]_

In order to enable VA-API for my ADM GPU, the driver "radeonsi" should be added
[#]_: ::

	$ nano /etc/portage/make.conf
		VIDEO_CARDS="amdgpu radeonsi"

Also, for applications that support VA-VAP, the USE flag "vaapi" should be
included [#]_: ::

	$ nano /etc/portage/make.conf
		USE="vaapi"

After that, update the whole system to apply these changes. However, we still
need to do additional settings inside MPV and Firefox respectively to make them
work with VA-API while playing videos.

MPV Settings
------------

Simply add the below line to MPV's configuration file, Or use the option
``--hwdec=vaapi`` while opening it: ::

	$ nano ~/.config/mpv/mpv.conf
		hwdec=vaapi

To verify if MPV have VA-API enabled, play a video in MPV and hit the key "i" to
get its running details:

.. image:: /statics/images/2023/09/vaapi-mpv.webp
       :width: 360px

Firefox Settings
----------------

Open the page ``about:config`` in Firefox, make sure the below two options are
set to true: ::

	gfx.webrender.all             true
	media.ffmpeg.vaapi.enabled    true

However, I was not able to find the option ``media.ffmpeg.vaapi.enable`` in my
Firefox, then I channelled my Google-fu and found out:

	115esr needs "hwcaccel" and "wayland" USE flags enabled to get hardware
	acceleration for Firefox. X and wayland can be enabled simultaneously.
	>116 was fixed to have hardware acceleration without wayland support.
	[#]_

According to that, since my firefox version was 102esr, I had to add additional
USE flags ``hwaccel`` and ``wayland`` (note that even for Xorg, the USE flag
``wayland`` is needed): ::

	$ nano /etc/portage/package.use/firefox
		www-client/firefox hwaccel wayland

To verify if Firefox works fine with VA-API enabled, execute the following
command and check out the output: ::

	$ MOZ_LOG="PlatformDecoderModule:5" firefox 2>&1 | grep "VA-API"

.. image:: /statics/images/2023/09/vaapi-firefox.webp
       :width: 720px

Thanks for reading :)


Further Readings
----------------

.. [#] `Arch Wiki: Hardware Video Acceleration <https://wiki.archlinux.org/title/Hardware_video_acceleration#Application_support>`_
.. [#] `Wikipedia: Video Acceleration API <https://en.wikipedia.org/wiki/Video_Acceleration_API>`_
.. [#] `Gentoo Wiki: VAAPI <https://wiki.gentoo.org/wiki/VAAPI>`_
.. [#] `Gentoo Wiki: AMDGPU <https://wiki.gentoo.org/wiki/AMDGPU#Feature_support>`_
.. [#] `Gentoo Wiki: Firefox <https://wiki.gentoo.org/wiki/Firefox#ESR>`_


.. _MPV: https://mpv.io/
