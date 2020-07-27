import os
import subprocess
import tarfile
import wget

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def package_to_name(package):
    #remove marvin_ substring
    return package[len("marvin_"):]

def generate_engine_package(package):
    subprocess.run(['python', 'setup.py', 'sdist'])
    filename = package + "-" + get_version(package) + ".tar.gz"
    origin = os.path.join(os.getcwd(), "dist", filename)
    dest = os.path.join(os.getcwd(), "docker", "develop" ,"daemon", filename)
    os.rename(origin, dest)

def get_version(package):
    with open(os.path.join(os.getcwd(), package ,"VERSION"), 'rb') as f:
        version = f.read().decode('ascii').strip()
    return version

def package_folder(input, output):
    with tarfile.open(output, "w:gz") as tar:
        tar.add(input, arcname=os.path.basename(input))

def extract_folder(input, output):
    tf = tarfile.open(input)
    tf.extractall(output)

def call_logs(package):
    container_name = 'marvin-cont-' + package_to_name(package)
    subprocess.Popen(['xterm', '-e', 'docker', 'logs', '-f', container_name])
    
def get_executor_path_or_download(executor_url):
    #get filename from url
    _executor_name = executor_url.split('/').pop(-1)

    executor_path = os.path.join(os.environ['MARVIN_DATA_PATH'], _executor_name)

    if not os.path.exists(executor_path):
        wget(executor_url, out=executor_path)

    return executor_path