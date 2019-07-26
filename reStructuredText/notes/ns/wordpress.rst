Wordpress
=========

::

    # systemctl start nginx

::

    # docker cp wp-file-manager <container>:/var/www/html/wp-content/plugins/wp-file-manager

::

    # docker exec -it <container> bash
        chown -R www-data:www-data wp-content/plugins/wp-file-manager
        echo 'upload_max_filesize = 2048M' >> /usr/local/etc/php/conf.d/upload.ini
        echo 'post_max_size = 2048M' >> /usr/local/etc/php/conf.d/upload.ini
    # docker restart <container>
        
