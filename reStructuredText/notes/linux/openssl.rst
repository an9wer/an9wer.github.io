.. meta::
    :robots: noindex

Openssl
=======


Display the content of certificate: ::

    $ openssl x509 -in <certificate> -text


Download certificate from a website: ::

    $ echo -n | openssl s_client -servername <NAME> -connect <HOST:PORT> \
        | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > <certificate>

    -connect <HOST:PORT>  The host and port to connect to.
    -servername <NAME>    The TLS SNI (Server Name Indication) extension (website).

Check certificate expire date: ::

    $ echo -n | openssl s_client -servername <NAME> -connect <HOST:PORT> 2>/dev/null | openssl x509 -noout -dates
    
Display fingerprint of certificate: ::

    $ openssl x509 -in <certificate> -fingerprint -noout 

Display serial of certificate: ::

    $ openssl x509 -in <certificate> -serial -noout 

Create pfx file from certificate and private key: ::

    $ openssl pkcs12 -export -out <pfx> -inkey <key> -in <certificate>


References
----------

`Wikipedia: public key fingerprint <https://en.wikipedia.org/wiki/Public_key_fingerprint>`_
