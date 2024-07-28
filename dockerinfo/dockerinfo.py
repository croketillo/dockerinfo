"""
DOCKERINFO v1.4

Author: croketillo <croketillo@gmail.com> <https://github.com/croketillo>
Description: Extract information from Docker containers
License: GNU(GPL)-3

Example usage:
=============

docker_helper = DockerHelper()
containers_list = docker_helper.list_containers(all_containers=True)
my_container = docker_helper.get_container_by_name("my_container_name")
"""

import docker
from datetime import datetime

class DockerHelper:
    def __init__(self):
        self.client = docker.from_env()

    def list_containers(self, all_containers=False):
        """
        Get a list of Docker containers.

        :param all_containers: If True, include stopped containers in the list.
        :return: List of Docker containers.
        """
        return self.client.containers.list(all=all_containers)

    def get_container_by_name(self, container_name):
        """
        Get a Docker container by its name.

        :param container_name: The name of the Docker container to retrieve.
        :return: The Docker container object if it exists, otherwise None.
        """
        containers = self.list_containers(all_containers=True)
        for container in containers:
            if container.name == container_name:
                return container
        return None

class DockerContainerInfo:
    """
    Provides information and operations related to a Docker container.

    :param container: Docker container object.
    """

    def __init__(self, container):
        self.container = container

    @property
    def id(self):
        """Get the ID of the Docker container."""
        return self.container.id

    @property
    def name(self):
        """Get the name of the Docker container."""
        return self.container.name

    @property
    def status(self):
        """Get the status of the Docker container."""
        return self.container.status

    @property
    def config(self):
        """Get the complete configuration of the Docker container."""
        return self.container.attrs['Config']

    @property
    def hostname(self):
        """Get the hostname of the Docker container."""
        return self.container.attrs['Config'].get('Hostname') or None

    @property
    def domainname(self):
        """Get the domain name of the Docker container."""
        return self.container.attrs['Config'].get('Domainname') or None

    @property
    def stopsignal(self):
        """Get the stop signal of the Docker container."""
        return self.container.attrs['Config'].get('StopSignal') or None

    @property
    def networks(self):
        """Get information about all networks associated with the Docker container."""
        return self.container.attrs['NetworkSettings']['Networks']

    def get_network_config(self, network):
        """Get the configuration of a specific network associated with the Docker container."""
        return self.networks.get(network)

    def get_network_attribute(self, network, attribute):
        """
        Get a specific attribute of a network associated with the Docker container.

        :param network: The name of the network.
        :param attribute: The attribute to retrieve.
        :return: The value of the specified attribute.
        """
        network_info = self.networks.get(network, {})
        return network_info.get(attribute)

    @property
    def mounted_volumes(self):
        """Get information about mounted volumes for the Docker container."""
        return self.container.attrs['Mounts']

    def get_logs(self):
        """Get the logs of the Docker container."""
        return self.container.logs().decode('utf-8').split('\n')

    def get_logs_since(self, timestamp):
        """
        Get the logs of the Docker container since a specified timestamp.

        :param timestamp: The timestamp in seconds.
        :return: The logs since the specified timestamp.
        """
        return self.container.logs(since=timestamp).decode('utf-8').split('\n')

    def get_logs_since_date(self, date_string):
        """
        Get the logs of the Docker container since a specified date.

        :param date_string: The date in MM/DD/YYYY format.
        :return: The logs since the specified date.
        """
        date_format = "%m/%d/%Y"
        date_object = datetime.strptime(date_string, date_format)
        timestamp = int(date_object.timestamp())
        return self.get_logs_since(timestamp)

    def get_logs_tail(self, lines):
        """
        Get the last specified number of lines from the logs of the Docker container.

        :param lines: The number of lines to retrieve.
        :return: The last specified number of lines from the logs.
        """
        return self.container.logs(tail=lines).decode('utf-8').split('\n')
