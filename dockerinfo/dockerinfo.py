"""
DOCKERINFO v1.3.2

Author: croketillo <croketillo@gmail.com> <https://github.com/croketillo>
Description: Extract information from docker containers
License: GNU(GPL)-3

Example usage:
=============

docker_helper = GetDockerContainers()
containers_list = docker_helper.list_containers(all_containers=True)
my_container = docker_helper.get_container_by_name("my_container_name")
"""
import docker
from datetime import datetime

class GetDockerContainers:
    def __init__(self):
        # Initialize a Docker client using the default environment settings
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
        :return: The Docker container object if it exists, otherwise return None.
        """
        containers = self.list_containers(all_containers=True)  # Get all containers

        for container in containers:
            if container.name == container_name:
                # Return the container if it exists
                return container
            else:
                # Return None if the container doesn't exist
                return None

class DockerContainerInfo:
    """
    A class that provides information and operations related to a Docker container.

    :param container: Docker container object.
    """

    def __init__(self, container):
        self.container = container

    @property
    def get_id(self):
        """Get the ID of the Docker container."""
        return self.container.id

    @property
    def get_name(self):
        """Get the name of the Docker container."""
        return self.container.name

    @property
    def get_status(self):
        """Get the status of the Docker container."""
        return self.container.status

    @property
    def get_config_all(self):
        """Get the complete configuration of the Docker container."""
        return self.container.attrs['Config']

    @property
    def get_hostname(self):
        """Get the hostname of the Docker container."""
        info = self.container.attrs['Config']['Hostname']
        if info == '':
            return None
        else:
            return info

    @property
    def get_domainname(self):
        """Get the domain name of the Docker container."""
        info = self.container.attrs['Config']['Domainname']
        if info == '':
            return None
        return info

    # ... (Similar property methods for other configuration attributes)

    @property
    def get_stopsignal(self):
        """Get the stop signal of the Docker container."""
        info = self.container.attrs['Config']['StopSignal']
        if info == '':
            return None
        return info

    @property
    def get_networks_all(self):
        """Get information about all networks associated with the Docker container."""
        return self.container.attrs['NetworkSettings']['Networks']

    def get_network_config(self, network):
        """Get the configuration of a specific network associated with the Docker container."""
        net = self.container.attrs['NetworkSettings']['Networks'][network]
        return net

    def get_network_attribute(self, network, att):
        """
        Get a specific attribute of a network associated with the Docker container.

        :param network: The name of the network.
        :param att: The attribute to retrieve.
        :return: The value of the specified attribute.
        """
        att = self.container.attrs['NetworkSettings']['Networks'][network][att]
        return att

    @property
    def mount_volumes(self):
        """Get information about mounted volumes for the Docker container."""
        return self.container.attrs['Mounts']

    def get_logs(self):
        """Get the logs of the Docker container."""
        logs = self.container.logs().decode('utf-8').split('\n')
        return logs

    def get_logs_since(self, timestamp):
        """
        Get the logs of the Docker container since a specified timestamp.

        :param timestamp: The timestamp in seconds.
        :return: The logs since the specified timestamp.
        """
        logs = self.container.logs(since=timestamp).decode('utf-8').split('\n')
        return logs
    
    def get_logs_format_date(self, date_string):
        """
        Get the logs of the Docker container since a specified date.

        :param date_string: The date in MM/DD/YYYY format.
        :return: The logs since the specified date.
        """
        # Convert the date string to a datetime object
        date_format = "%m/%d/%Y"
        date_object = datetime.strptime(date_string, date_format)

        # Convert datetime object to timestamp
        timestamp = int(date_object.timestamp())

        # Get the logs since the specified timestamp
        logs = self.container.logs(since=timestamp).decode('utf-8').split('\n')
        return logs

    def get_logs_tail(self, lines):
        """
        Get the last specified number of lines from the logs of the Docker container.

        :param lines: The number of lines to retrieve.
        :return: The last specified number of lines from the logs.
        """
        logs = self.container.logs(tail=lines).decode('utf-8').split('\n')
        return logs
