detach:
	@docker compose up -d

up:
	@docker compose up

down:
	@docker compose down

logs:
	@tail -f ${PWD}/odoo-data/odoo-server.log

shell:
	@docker exec -it calyx-odoo /usr/bin/odoo shell --db_host db -d odoo -r odoo -w odoo

ssh:
	@docker exec -it calyx-odoo bash