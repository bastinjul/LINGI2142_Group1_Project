# lingi2142 - Computer networks: configuration and management

This repository contains:

  * TODO complete

# Virtual machine

A sample virtual machine definition to run the script is provided and managed
using [Vagrant](https://www.vagrantup.com), using a
[VirtualBox](https://www.virtualbox.org) provider. 

You *need* to install *both* of these softwares on your machine in order to
run an emulated network.

## Commands summary

  * [./build_vm.sh](build_vm.sh) will create and provision the virtual machine.
  * `vagrant up` will boot the VM (once it has been built).
  * `vagrant ssh` (from this directory) will create an ssh connection to the
      VM.
  * `vagrant halt` will stop the VM (i.e. shutdown properly the guest OS).

# Virtual network

The main directory of this repository contains the set of scripts to start a
virtual network as well as loads and apply its configuration files.
You _should_ only run such a network within the VM.

## Description

  * TODO explain how to create the network and how to connect to a machine

## Our topology

TODO where is our topology

### Description

TODO describe our topology

### Scripts

The routers all define a boot script, which reloads the sysctl configuration
in every net NS (in this case: Enable IPv6 and IPv6 forwarding). Their startup
script then assign IPv6 addresses to the interfaces and/or start a routing
daemon.

More specifically:
  - TODO describing the nodes

### Example test

  - TODO describing how to launch the tests and whats tests are available

