Openssl
=======


Display the content of certificate: ::

    $ openssl x509 -in <certificate> -text


Download certificate from a website: ::

    $ echo -n | openssl s_client -connect <HOST:PORT> \
        | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' >
        <certificate>


Display fingerprint of certificate: ::

    $ openssl x509 -in <certificate> -fingerprint -noout 

Display serial of certificate: ::

    $ openssl x509 -in <certificate> -serial -noout 


References
----------

`Wikipedia: public key fingerprint <https://en.wikipedia.org/wiki/Public_key_fingerprint>`_
