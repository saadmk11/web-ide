import json

from channels.generic.websocket import WebsocketConsumer

from ide.docker_containers import DockerContainer


class WebIDEConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope["user"]
        self.docker_container = DockerContainer(self.user)
        self.accept()

    def disconnect(self, close_code):
        self.docker_container.remove()

    def receive(self, text_data):
        if self.user.is_authenticated:
            data = json.loads(text_data)
            user_input = data.get('command')
            input_type = data.get('type')

            if not user_input or not input_type:
                self.send_message('Invalid Input.')
                return

            if user_input.lower() == 'exit' or user_input.lower() == 'exit()':
                return self.close()

            output = self.docker_container.run(user_input, input_type)

            for line in output:
                message = (
                    line.decode("utf-8").strip()
                    if hasattr(line, 'decode')
                    else line.strip()
                )
                self.send_message(message)
        else:
            self.send_message('Please login to use the IDE.....')

    def send_message(self, message):
        self.send(
            text_data=json.dumps(
                {'message': message}
            )
        )
