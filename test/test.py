from dockerinfo import DockerContainerInfo, DockerHelper

def main():
    # Crear una instancia de la clase DockerHelper y listar los contenedores existentes.
    # Usar all_containers=True/False para listar contenedores inactivos.
    docker_info = DockerHelper()
    container_list = docker_info.list_containers(all_containers=True)

    # Iterar a través de todos los contenedores encontrados y extraer información.
    print(">>> ITERANDO A TRAVÉS DE TODOS LOS CONTENEDORES EXISTENTES Y EXTRAYENDO INFORMACIÓN")
    for container in container_list:
        container_info = DockerContainerInfo(container)
        print(f"Container ID: {container_info.id}")
        print(f"Container Name: {container_info.name}")
        print(f"Container Status: {container_info.status}")
        print(f"Container Log (last 5 lines):")
        for log_line in container_info.get_logs_tail(5):
            print(log_line)

    # Extraer información de un contenedor específico (en este caso, 'test01').
    print("\n>>> BUSCANDO UN CONTENEDOR ESPECÍFICO (test01)")
    container = docker_info.get_container_by_name('test01')

    if container:
        # Si se encuentra el contenedor, crear una instancia de la clase DockerContainerInfo.
        container_info = DockerContainerInfo(container)

        # Imprimir información del contenedor.
        print(f"Container ID: {container_info.id}")
        print(f"Container Name: {container_info.name}")
        print(f"Container Status: {container_info.status}")

        # Probar otros métodos de la clase DockerContainerInfo según sea necesario.
        print(f"Networks (all): {container_info.networks}")

        network_name = 'bridge'  # Cambiar el nombre de la red según sea necesario.
        network_info = container_info.get_network_config(network_name)
        print(f"Network Info for {network_name}: {network_info}")

        ip_address = container_info.get_network_attribute(network_name, 'IPAddress')
        mac_address = container_info.get_network_attribute(network_name, 'MacAddress')
        print(f"IP Address: {ip_address}, Mac Address: {mac_address}")

        # Imprimir más información del contenedor según sea necesario.
    else:
        print("Container not found: test01")

if __name__ == "__main__":
    main()