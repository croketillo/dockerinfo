DOCKERINFO
==========

Extract docker container info module

Example:
--------

::

   from dockerinfo import *



   docker_info = GetDockerContainers()

   container = docker_info.get_container_by_name('test01') #container example 'test01'

   if container:
       container_info = DockerContainerInfo(container)
       # Imprime información del contenedor
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
