Azure
=====

Switch subscription

::

    $ az account list --output table
    $ az account set --subscription <subscription id or name>

Upload docker image:

::

    $ az acr login --name sftest21199
    $ docker tag <old tag> <new tag>
    $ docker push sftest21199.azurecr.cn/httpserver:1.0.1

Upload service:

::

    $ sfctl cluster select --endpoint https://sftest99699.chinaeast.cloudapp.chinacloudapi.cn:19080/Explorer \
    > --key /home/wuxinrun/workpace/sftest99699/sftest99699.pem \
    > --cert /home/wuxinrun/workpace/sftest99699/sftest99699.crt --no-verify

    $ ./install.sh


Generate id and password:

::

    ./azure_cr_create_service_principal.sh gifttasks gifttasksSP
        service principal ID:
        service principal password:

About protal sfappgateway:
    Listeners (frontend)

    HTTP setting (backend)

    Rules   (map frontend to backend)

Service principal ID: 9a0392c5-0453-414a-aa0e-738719d7af34
Service principal password: 60dc6b80-061e-451d-bfaa-c1130bc51eba

Storage
-------

Generate container sas:

::

    az storage container generate-sas \
        --account-name $scriptstorageaccount \
        --name $containername \
        --expiry $(date -u -d "60 minutes" '+%Y-%m-%dT%H:%MZ') \
        --https-only \
        -o tsv \
        --permissions acdlrw

VM Custom Extension
-------------------

Related files:
    /var/lib/waagent/custom-script/download/<num>/
    /var/log/waagent.log 
    /var/log/azure/custom-script/handler.log

Run extension:

::

    az vmss extension set  \
        --resource-group nutstoresfstaging3 \
        --vmss-name nt1vm \
        --publisher Microsoft.Azure.Extensions \
        --name customScript \
        --settings ./script.json
