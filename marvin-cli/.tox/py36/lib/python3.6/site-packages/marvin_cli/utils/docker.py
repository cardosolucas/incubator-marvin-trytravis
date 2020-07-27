import os
from docker import DockerClient
from docker.errors import ImageNotFound, NotFound
from .misc import package_to_name, generate_engine_package
from ..utils.log import get_logger

logger = get_logger('docker')

def _get_client(env=True, url=None):
    if env:
        return DockerClient.from_env()
    return DockerClient(base_url=url)

def _search_docker_image(name):
    client = _get_client()
    try:
        client.images.get(name)
        return True
    except ImageNotFound:
        return False

def _search_docker_container(name):
    client = _get_client()
    try:
        client.containers.get(name)
        return True
    except NotFound:
        return False

def search_engine_container(engine_package):
    container_name = "marvin-cont-" + package_to_name(engine_package)
    return _search_docker_container(container_name)

def search_engine_images(engine_package):
    image_name = "marvin-" + package_to_name(engine_package)
    return _search_docker_image(image_name)

def create_engine_image(engine_package):
    logger.info("Creating engine docker image ...")
    dockerfile_path = os.path.join(os.getcwd(), "docker", 
                        "develop", "daemon")
    generate_engine_package(engine_package)
    client = _get_client()
    client.images.build(
        path=dockerfile_path,
        tag="marvin-" + package_to_name(engine_package)
    )
    logger.info("Creating engine docker image ... Done!")

def create_daemon_container(engine_package, engine_name):
    logger.info("Creating engine docker container ...")
    client = _get_client()
    _engine_path = os.path.join(os.environ['MARVIN_HOME'], engine_name)
    client.containers.run(
        image="marvin-" + engine_name,
        name="marvin-cont-" + engine_name,
        volumes={
            _engine_path: {
                'bind': '/opt/marvin/engine',
                'mode': 'rw'
            },
            os.environ['MARVIN_DATA_PATH']: {
                'bind': '/opt/marvin/data',
                'mode': 'rw'
            },
            os.environ['MARVIN_LOG']: {
                'bind': '/opt/marvin/log',
                'mode': 'rw'
            }
        },
        ports={
            '50051/tcp': 50051,
            '50052/tcp': 50052,
            '50053/tcp': 50053,
            '50054/tcp': 50054,
            '50055/tcp': 50055,
            '50056/tcp': 50056,
            '50057/tcp': 50057,
            '8888/tcp': 8888
        },
        detach=True
    )

    logger.info("Creating engine docker container ... Done!")