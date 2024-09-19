## Init
1 - Create scaffold
```sh
docker exec -it calyx-odoo /usr/bin/odoo scaffold xxxxx_company /mnt/extra-addons
```
2 - Fix permissions
```sh
cd addons
sudo chown -R $USER:$USER xxxxx_company/
```