"""
DOCKERINFO v1.2

Author: croketillo <croketillo@gmail.com> <https://github.com/croketillo>
Description: Extract information from docker containers
License: GNU(GPL)-3
"""
import docker

class GetDockerContainers:
    def __init__(self):
        self.client = docker.from_env()

    def list_containers(self, all_containers=False):
        return self.client.containers.list(all=all_containers)


    def get_container_by_name(self,container_name):
        containers = self.list_containers(all_containers=True) #Get all containers
        for container in containers:
            if container.name == container_name:
                return container #Return the container if exist
            else:
                return None #Return None if container dont exist 

class DockerContainerInfo:
    def __init__(self,container):
        self.container=container

    @property
    def get_id(self):
        return self.container.id

    @property
    def get_name(self):
        return self.container.name

    @property
    def get_status(self):
        return self.container.status

    @property
    def get_config_all(self):
        return self.container.attrs['Config']

    @property
    def get_hostname(self):
        info=self.container.attrs['Config']['Hostname']
        if info == '':
            return None
        else:
            return info

    @property
    def get_domainname(self):
        info=self.container.attrs['Config']['Domainname']
        if info == '':
            return None
        return info

    @property
    def get_user(self):
        info=self.container.attrs['Config']['User']
        if info == '':
            return None
        return info

    @property
    def get_stdin(self):
        info=self.container.attrs['Config']['AttachStdin']
        if info == '':
            return None
        return info

    @property
    def get_stdout(self):
        info=self.container.attrs['Config']['AttachStdout']
        if info == '':
            return None
        return info

    @property
    def get_stderr(self):
        info=self.container.attrs['Config']['AttachStderr']
        if info == '':
            return None
        return info

    @property
    def get_ports(self):
        info=self.container.attrs['Config']['ExposedPorts']
        if info == '':
            return None
        for ports in info:
            return ports

    @property
    def get_tty(self):
        info=self.container.attrs['Config']['Tty']
        if info == '':
            return None
        return info

    @property
    def get_openstdin(self):
        info=self.container.attrs['Config']['OpenStdin']
        if info == '':
            return None
        return info

    @property
    def get_stdinonce(self):
        info=self.container.attrs['Config']['StdinOnce']
        if info == '':
            return None
        return info

    @property
    def get_env(self):
        info=self.container.attrs['Config']['Env']
        if info == '':
            return None
        return info

    @property
    def get_onbuild(self):
        info=self.container.attrs['Config']['OnBuild']
        if info == '':
            return None
        return info

    @property
    def get_cmd(self):
        info=self.container.attrs['Config']['Cmd']
        if info == '':
            return None
        return info

    @property
    def get_image(self):
        info=self.container.attrs['Config']['Image']
        if info == '':
            return None
        return info

    @property
    def get_volumes(self):
        info=self.container.attrs['Config']['Volumes']
        if info == '':
            return None
        return info

    @property
    def get_workdir(self):
        info=self.container.attrs['Config']['WorkingDir']
        if info == '':
            return None
        return info

    @property
    def get_entrypoint(self):
        info=self.container.attrs['Config']['Entrypoint'][0]
        if info == '':
            return None
        return info

    @property
    def get_labels(self):
        info=self.container.attrs['Config']['Labels']
        if info == '':
            return None
        return info

    @property
    def get_stopsignal(self):
        info=self.container.attrs['Config']['StopSignal']
        if info == '':
            return None
        return info

    @property
    def get_networks_all(self):
        return self.container.attrs['NetworkSettings']['Networks']

    def get_network_config(self,network):
        net=self.container.attrs['NetworkSettings']['Networks'][network]
        return net

    def get_network_attribute(self,network,att):
        #ATTRIBUTES:
        #'IPAMConfig','Links','Aliases','NetworkID','EndpointID','Gateway','IPAddress',IPPrefixLen',
        #'IPv6Gateway','GlobalIPv6Address', 'GlobalIPv6PrefixLen','MacAddress','DriverOpts'
        att=self.container.attrs['NetworkSettings']['Networks'][network][att]
        return att

    @property
    def mount_volumes(self):
        return self.container.attrs['Mounts']

    def get_logs(self):
        logs = self.container.logs().decode('utf-8').split('\n')

    def get_logs_since(self, timestamp):
        logs = self.container.logs(since=timestamp).decode('utf-8').split('\n')

    def get_logs_tail(self, lines):
        logs = self.container.logs(tail=lines).decode('utf-8').split('\n')
        return logs
