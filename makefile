up:
	@docker compose up

detach:
	@docker compose up -d

down:
	@docker compose down

logs:
	@tail -f ${PWD}/odoo-data/odoo-server.log