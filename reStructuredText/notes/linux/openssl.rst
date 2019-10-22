Openssl
=======


Display the content of certificate: ::

    $ openssl x509 -in <certificate.crt> -text


Download certificate from a website: ::

    $ echo -n | openssl s_client -connect <HOST:PORT> \
        | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' >
        <certificate.crt>

