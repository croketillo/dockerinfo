DOCKERINFO
==========

Extract information from docker containers.

Example:
--------

.. code::

   from dockerinfo import *



   docker_info = GetDockerContainers()

   container = docker_info.get_container_by_name('test01') #container example 'test01'

   if container:
       container_info = DockerContainerInfo(container)
       # Print container info
       print(f"Container ID: {container_info.get_id}")
       print(f"Container Name: {container_info.get_name}")
       print(f"Container Status: {container_info.get_status}")

       print(f"Networks (all): {container_info.get_networks_all}")
       
       network_name = 'bridge' #network example 'bridge' 
       network_info = container_info.get_network_config(network_name)
       print(f"Network Info for {network_name}: {network_info}")

       ip_address = container_info.get_network_attribute(network_name, 'IPAddress')
       mac_address = container_info.get_network_attribute(network_name, 'MacAddress')
       print(f"IP Address: {ip_address}, Mac Address: {mac_address}")

   else:
       print(f"Container not found: {container_name}")

Aviable options:
----------------

-  ‘get_id’

Returns the container ID.

-  ‘get_name’

Returns the container name.

-  ‘get_status’

Returns the current status of the container.

-  ‘get_config_all’

Returns the entire configuration of the container.

-  ‘get_hostname’

Returns the container’s hostname.

-  ‘get_domainname’

Returns the container’s domain name.

-  ‘get_user’

Returns the user of the container.

-  ‘get_stdin’

Returns information about the container’s standard input connection.

-  ‘get_stdout’

Returns information about the container’s standard output connection.

-  ‘get_stderr’

Returns information about the container’s standard error connection.

-  ‘get_ports’

Returns information about the ports exposed by the container.

-  ‘get_tty’

Returns information about the TTY allocation of the container.

-  ‘get_openstdin’

Returns information about whether the container’s standard input is
open.

-  ‘get_stdinonce’

Returns information about whether the container’s standard input is a
one-time use.

-  ‘get_env’

Returns the container’s environment configuration.

-  ‘get_onbuild’

Returns information about the ONBUILD instructions of the container.

-  ‘get_cmd’

Returns the starting command of the container.

-  ‘get_image’

Returns the image of the container.

-  ‘get_volumes’

Returns the configuration of volumes in the container.

-  ‘get_workdir’

Returns the working directory of the container.

-  ‘get_entrypoint’

Returns the entry point of the container.

-  ‘get_labels’

Returns the labels of the container.

-  ‘get_stopsignal’

Returns the stop signal of the container.

-  ‘get_networks_all’

Returns the configuration of all networks of the container.

-  ‘get_network_config(network)’

Returns the configuration of a specific network of the container.

-  ‘get_network_attribute(network, att)’

Returns a specific attribute of a network of the container.

-  ‘mount_volumes’

Returns the configuration of volumes mounted in the container.
