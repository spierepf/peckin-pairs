import time
from pathlib import Path

import docker

from features.layers.behave_layer import BehaveLayer


class DockerLayer(BehaveLayer):
    def before_all(self, context):
        context.docker_image_tag = f"peckin-pairs:tmp-{int(time.time())}"
        docker.from_env().images.build(
            path=str(Path(__file__).resolve().parent.parent.parent),
            tag=context.docker_image_tag,
            rm=True
        )
        context.docker_container = docker.from_env().containers.run(context.docker_image_tag, detach=True,
                                                                    auto_remove=True, ports={'8000/tcp': 8000})

    def after_all(self, context):
        context.docker_container.stop()
        docker.from_env().images.remove(image=context.docker_image_tag)
