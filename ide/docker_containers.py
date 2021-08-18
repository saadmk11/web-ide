import docker
from docker.errors import NotFound as DockerContainerNotFound

from ide.models import Container


class DockerContainer:

    def __init__(self, user):
        self.user = user
        self.client = docker.from_env()

    def create(self):
        container = self.client.containers.run(
            'python:3.8-slim',
            tty=True,
            stdin_open=True,
            detach=True
        )
        obj, _ = Container.objects.get_or_create(user=self.user)
        obj.container_id = container.id
        obj.save()
        return container

    def get(self):
        try:
            user_container_id = self.user.container.container_id
            container = self.client.containers.get(user_container_id)

            if container.status != 'running':
                container.start()
        except (Container.DoesNotExist, DockerContainerNotFound):
            container = self.create()

        return container

    def run(self, input, input_type):
        container = self.get()

        if input_type == 'code':
            command = ['python', '-c', input]
        else:
            command = ['/bin/sh', '-c', input]
        
        try:
            return container.exec_run(
                command, stdin=True, tty=True, stream=True
            ).output
        except Exception:
            return [
                f'An Error Occurred While Running "{input}".',
                'Please Restart The Container'
            ]

    def remove(self):
        try:
            user_container_id = self.user.container.container_id
            container = self.client.containers.get(user_container_id)
            container.remove(v=True, force=True)
            self.user.container.delete()
        except (Container.DoesNotExist, DockerContainerNotFound):
            pass
