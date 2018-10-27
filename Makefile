all: clean create

create:
	sudo python3 scripts/config_service.py
	sudo python3 scripts/config_router.py
	sudo python3 scripts/config_host.py
	sudo ./create_network.sh ucl_topo

connect:
	sudo ./connect_to.sh ucl_minimal_cfg ${ROUTER}

clean:
	sudo ./cleanup.sh

