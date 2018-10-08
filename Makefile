all: clean create

create:
	sudo ./create_network.sh ucl_topo

clean:
	sudo ./cleanup.sh

