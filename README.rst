DOCKERINFO
==========


.. image:: https://img.shields.io/pypi/dm/dockerinfo
   :alt: PyPI - Downloads per month

.. image:: https://img.shields.io/pepy/dt/dockerinfo
   :alt: Pepy Total Downlods


Easily extract information from docker containers

Since version 1.2 can extract containers logs.

Example:
--------

.. code:: python

   from dockerinfo import DockerContainerInfo, GetDockerContainers

   # Create an instance of the GetDockerContainers class and list the existing containers.
   # Use all_containers=True/False to list inactive containers.
   docker_info = GetDockerContainers()
   container_list = docker_info.list_containers(all_containers=True)

   # Iterate through all found containers and extract information.
   print(">>> ITERATING THROUGH ALL EXISTING CONTAINERS AND EXTRACTING INFORMATION")
   for container in container_list:
       container_info = DockerContainerInfo(container)
       print(f"Container ID: {container_info.get_id}")
       print(f"Container Name: {container_info.get_name}")
       print(f"Container Status: {container_info.get_status}")
       print(f"Container Log (last 5 lines):")
       for log_line in container_info.get_logs_tail(5):
         print(log_line)

   # Extract information from a specific container (in this case, 'test01').
   print("\n>>> LOOKING FOR A SPECIFIC CONTAINER (test01)")
   container = docker_info.get_container_by_name('test01')

   if container:
       # If the container is found, create an instance of the DockerContainerInfo class.
       container_info = DockerContainerInfo(container)
       
       # Print container information.
       print(f"Container ID: {container_info.get_id}")
       print(f"Container Name: {container_info.get_name}")
       print(f"Container Status: {container_info.get_status}")

       # Test other methods of the DockerContainerInfo class as needed.
       print(f"Networks (all): {container_info.get_networks_all}")
       
       network_name = 'bridge'  # Change the network name as needed.
       network_info = container_info.get_network_config(network_name)
       print(f"Network Info for {network_name}: {network_info}")

       ip_address = container_info.get_network_attribute(network_name, 'IPAddress')
       mac_address = container_info.get_network_attribute(network_name, 'MacAddress')
       print(f"IP Address: {ip_address}, Mac Address: {mac_address}")

       # Print more container information as needed.
   else:
       print(f"Container not found: {container}")

Aviable options:
----------------

-  **get_id**

Returns the container ID.

-  **get_name**

Returns the container name.

-  **get_status**

Returns the current status of the container.

-  **get_config_all**

Returns the entire configuration of the container.

-  **get_hostname**

Returns the container’s hostname.

-  **get_domainname**

Returns the container’s domain name.

-  **get_user**

Returns the user of the container.

-  **get_stdin**

Returns information about the container’s standard input connection.

-  **get_stdout**

Returns information about the container’s standard output connection.

-  **get_stderr**

Returns information about the container’s standard error connection.

-  **get_ports**

Returns information about the ports exposed by the container.

-  **get_tty**

Returns information about the TTY allocation of the container.

-  **get_openstdin**

Returns information about whether the container’s standard input is
open.

-  **get_stdinonce**

Returns information about whether the container’s standard input is a
one-time use.

-  **get_env**

Returns the container’s environment configuration.

-  **get_onbuild**

Returns information about the ONBUILD instructions of the container.

-  **get_cmd**

Returns the starting command of the container.

-  **get_image**

Returns the image of the container.

-  **get_volumes**

Returns the configuration of volumes in the container.

-  **get_workdir**

Returns the working directory of the container.

-  **get_entrypoint**

Returns the entry point of the container.

-  **get_labels**

Returns the labels of the container.

-  **get_stopsignal**

Returns the stop signal of the container.

-  **get_networks_all**

Returns the configuration of all networks of the container.

-  **get_network_config(network)**

Returns the configuration of a specific network of the container.

-  **get_network_attribute(network, att)**

Returns a specific attribute of a network of the container.

-  **mount_volumes**

Returns the configuration of volumes mounted in the container.

-  **get_logs** Get the logs of the container, split into lines. Return
   a list containing each line of the container’s logs as a string.

-  **get_logs_since(timestamp)** Get the logs of the container since a
   specified timestamp, split into lines.

Args:

timestamp (int): The Unix timestamp from which to start fetching logs.

Return a list containing each line of the container’s logs as a string.

-  **get_logs_tail(lines)**

Get the last N lines of the container’s logs, split into lines.

Args:

lines (int): The number of lines to retrieve from the end of the logs.
Returns:

Returs a list containing each line of the container’s logs as a string.

.. |PyPI| image:: https://img.shields.io/pypi/v/dockerinfo
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dm/dockerinfo?color=%2360EE59
.. |Total Downloads| image:: https://static.pepy.tech/badge/dockerinfo
