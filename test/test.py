from dockerinfo.dockerinfo import DockerContainerInfo, GetDockerContainers

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
