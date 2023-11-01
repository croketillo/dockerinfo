import docker

class GetDockerContainers:
    def __init__(self):
        self.client = docker.from_env()

    def list_containers(self, all_containers=False):
        return self.client.containers.list(all=all_containers)


    def get_container_by_name(self,container_name):
        containers = self.list_containers(all_containers=True) #Obtener todos los contenedores
        for container in containers:
            if container.name == container_name:
                return container# Retorna el contenedor si se encuentra
            else:
                return None #Retorna None si el contenedor no se encuentra



class DockerContainerInfo:
    def __init__(self,container):
        self.container=container

    @property
    def id(self):
        return self.container.id

    @property
    def name(self):
        return self.container.name

    @property
    def status(self):
        return self.container.status

    @property
    def config_all(self):
        return self.container.attrs['Config']

    @property
    def config_hostname(self):
        info=self.container.attrs['Config']['Hostname']
        if info == '':
            return None
        else:
            return info

    @property
    def config_domainname(self):
        info=self.container.attrs['Config']['Domainname']
        if info == '':
            return None
        return info

    @property
    def config_user(self):
        info=self.container.attrs['Config']['User']
        if info == '':
            return None
        return info

    @property
    def config_stdin(self):
        info=self.container.attrs['Config']['AttachStdin']
        if info == '':
            return None
        return info

    @property
    def config_stdout(self):
        info=self.container.attrs['Config']['AttachStdout']
        if info == '':
            return None
        return info

    @property
    def config_stderr(self):
        info=self.container.attrs['Config']['AttachStderr']
        if info == '':
            return None
        return info

    @property
    def config_ports(self):
        info=self.container.attrs['Config']['ExposedPorts']
        if info == '':
            return None
        for ports in info:
            return ports

    @property
    def config_tty(self):
        info=self.container.attrs['Config']['Tty']
        if info == '':
            return None
        return info

    @property
    def config_tty(self):
        info=self.container.attrs['Config']['Tty']
        if info == '':
            return None
        return info

    @property
    def config_openstdin(self):
        info=self.container.attrs['Config']['OpenStdin']
        if info == '':
            return None
        return info

    @property
    def config_stdinonce(self):
        info=self.container.attrs['Config']['StdinOnce']
        if info == '':
            return None
        return info

    @property
    def config_env(self):
        info=self.container.attrs['Config']['Env']
        if info == '':
            return None
        return info

    @property
    def config_onbuild(self):
        info=self.container.attrs['Config']['OnBuild']
        if info == '':
            return None
        return info

    @property
    def cmd(self):
        info=self.container.attrs['Config']['Cmd']
        if info == '':
            return None
        return info

    @property
    def image(self):
        info=self.container.attrs['Config']['Image']
        if info == '':
            return None
        return info

    @property
    def volumes(self):
        info=self.container.attrs['Config']['Volumes']
        if info == '':
            return None
        return info

    @property
    def workdir(self):
        info=self.container.attrs['Config']['WorkingDir']
        if info == '':
            return None
        return info

    @property
    def entrypoint(self):
        info=self.container.attrs['Config']['Entrypoint'][0]
        if info == '':
            return None
        return info

    @property
    def labels(self):
        info=self.container.attrs['Config']['Labels']
        if info == '':
            return None
        return info

    @property
    def config_stopsignal(self):
        info=self.container.attrs['Config']['StopSignal']
        if info == '':
            return None
        return info

    @property
    def networks_all(self):
        return self.container.attrs['NetworkSettings']['Networks']

    def network_config(self,network):
        net=self.container.attrs['NetworkSettings']['Networks'][network]
        return net

    def net_attribute(self,network,att):
        #ATTRIBUTES:
        #'IPAMConfig','Links','Aliases','NetworkID','EndpointID','Gateway','IPAddress',IPPrefixLen',
        #'IPv6Gateway','GlobalIPv6Address', 'GlobalIPv6PrefixLen','MacAddress','DriverOpts'
        att=self.container.attrs['NetworkSettings']['Networks'][network][att]
        return att

    @property
    def environment(self):
        return self.container.attrs['Config']['Env']

    @property
    def volumes(self):
        return self.container.attrs['Mounts']
        