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

   from dockerinfo.docker_info import DockerContainerInfo, DockerHelper

   # Create an instance of the DockerHelper class and list the existing containers.
   # Use all_containers=True/False to list inactive containers.
   docker_info = DockerHelper()
   container_list = docker_info.list_containers(all_containers=True)

   # Iterate through all found containers and extract information.
   print(">>> ITERATING THROUGH ALL EXISTING CONTAINERS AND EXTRACTING INFORMATION")
   for container in container_list:
       container_info = DockerContainerInfo(container)
       print(f"Container ID: {container_info.id}")
       print(f"Container Name: {container_info.name}")
       print(f"Container Status: {container_info.status}")
       print(f"Container Log (last 5 lines):")
       for log_line in container_info.get_logs_tail(5):
           print(log_line)

   # Extract information from a specific container (in this case, 'test01').
   print("
   >>> LOOKING FOR A SPECIFIC CONTAINER (test01)")
   container = docker_info.get_container_by_name('test01')

   if container:
       # If the container is found, create an instance of the DockerContainerInfo class.
       container_info = DockerContainerInfo(container)
       
       # Print container information.
       print(f"Container ID: {container_info.id}")
       print(f"Container Name: {container_info.name}")
       print(f"Container Status: {container_info.status}")

       # Test other methods of the DockerContainerInfo class as needed.
       print(f"Networks (all): {container_info.networks}")
       
       network_name = 'bridge'  # Change the network name as needed.
       network_info = container_info.get_network_config(network_name)
       print(f"Network Info for {network_name}: {network_info}")

       ip_address = container_info.get_network_attribute(network_name, 'IPAddress')
       mac_address = container_info.get_network_attribute(network_name, 'MacAddress')
       print(f"IP Address: {ip_address}, Mac Address: {mac_address}")

       # Print more container information as needed.
   else:
       print("Container not found: test01")

Available options:
------------------

-  **id**

Returns the container ID.

-  **name**

Returns the container name.

-  **status**

Returns the current status of the container.

-  **config**

Returns the entire configuration of the container.

-  **hostname**

Returns the container’s hostname.

-  **domainname**

Returns the container’s domain name.

-  **stopsignal**

Returns the stop signal of the container.

-  **networks**

Returns the configuration of all networks of the container.

-  **get_network_config(network)**

Returns the configuration of a specific network of the container.

-  **get_network_attribute(network, attribute)**

Returns a specific attribute of a network of the container.

-  **mounted_volumes**

Returns the configuration of volumes mounted in the container.

-  **get_logs** Get the logs of the container, split into lines. Return
   a list containing each line of the container’s logs as a string.

-  **get_logs_since(timestamp)** Get the logs of the container since a
   specified timestamp, split into lines.

Args:

timestamp (int): The Unix timestamp from which to start fetching logs.

Return a list containing each line of the container’s logs as a string.

-  **get_logs_since_date(date_string)** Get the logs of the Docker
   container since a specified date.

Args: date_string: A string representing the date in MM/DD/YYYY format.

Returns the logs since the specified date.

Example:

::

   logs_since_date = instance.get_logs_since_date("01/15/2023")

**Note:** The date string must be in the correct format to avoid
conversion errors

-  **get_logs_tail(lines)**

Get the last N lines of the container’s logs, split into lines.

Args:

lines (int): The number of lines to retrieve from the end of the logs.

Returns:

Returns a list containing each line of the container’s logs as a string.

.. |PyPI| image:: https://img.shields.io/pypi/v/dockerinfo
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dm/dockerinfo?color=%2360EE59
.. |Pepy Total Downlods| image:: https://img.shields.io/pepy/dt/dockerinfo
