## Init
1 - Create scaffold
```sh
docker exec -it calyx-odoo /usr/bin/odoo scaffold calyx_technical_test /mnt/extra-addons
```
2 - Fix permissions
```sh
cd addons
sudo chown -R $USER:$USER calyx_technical_test/
```