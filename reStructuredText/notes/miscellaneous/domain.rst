.. meta::
    :robots: noindex

Domain
======

TLD and SLD
    `TLD <https://en.wikipedia.org/wiki/Top-level_domain>`_

    `SLD <https://en.wikipedia.org/wiki/Second-level_domain>`_

    `Types of domain name <https://www.domainregistration.com.au/infocentre/info-domain-type.php>`_

Certbot
-------

List all installed certificates: ::

    # certbot certificates

Remove an installed certificat: ::

    # certbot delete

Create a certificat for multiple domains: ::

    # certbot certonly -d <domain1> -d <domain2> [-d <domain3> ...]

Create wildcard ssl certificate: ::

    # certbot --server https://acme-v02.api.letsencrypt.org/directory \
        -d <*.example.com> --manual --preferred-challenges dns-01 certonly

    Add a DNS record of your domain:
        Type : TXT
        Name : _acme-challenge
        Value: <acme-challenge-value> (get from the command above)


