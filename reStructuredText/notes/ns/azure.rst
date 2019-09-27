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

    ./azure_cr_create_service_principal.sh gifttasks "nutstore_acr_gifttasks_sp"
        service principal ID:
        service principal password:

About protal sfappgateway:
    Listeners (frontend)

    HTTP setting (backend)

    Rules   (map frontend to backend)
