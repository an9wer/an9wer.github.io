.. meta::
    :robots: noindex

Nginx
=====


FQA:

Q: Do not allow access to a website by using ip address

A:
    ::

        if ($host !~* ^(.+\.)?domain\.com$) {
            return 444;
        }

R:
    `Disable direct access (via http and https) to a website using IP address
    <https://blog.knoldus.com/nginx-disable-direct-access-via-http-and-https-to-a-website-using-ip/>`_

    `Nginx domain regex
    <https://stackoverflow.com/questions/39110609/nginx-domain-regex-to-include-wildcards>`_


Client side certification
-------------------------

https://fardog.io/blog/2017/12/30/client-side-certificate-authentication-with-nginx/


