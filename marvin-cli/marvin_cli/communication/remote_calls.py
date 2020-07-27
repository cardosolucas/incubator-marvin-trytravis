import grpc
import time
from ..utils.log import get_logger
from .stubs import daemon_pb2
from .stubs import daemon_pb2_grpc

logger = get_logger('communication')

class RemoteError(Exception):
    pass

COMMANDS = {
    'DRYRUN': daemon_pb2.Command.CommandType.DRYRUN,
    'TEST': daemon_pb2.Command.CommandType.TEST,
    'GRPC': daemon_pb2.Command.CommandType.GRPC,
    'TDD': daemon_pb2.Command.CommandType.TDD,
    'TOX': daemon_pb2.Command.CommandType.TOX,
    'NOTEBOOK': daemon_pb2.Command.CommandType.NOTEBOOK,
    'LAB': daemon_pb2.Command.CommandType.LAB
}

class RemoteCalls:

    stub = None

    def __init__(self, host='localhost', port=50057):
        channel = grpc.insecure_channel("{}:{}".format(host, port))
        self.stub = daemon_pb2_grpc.CommandCallStub(channel)

    def call_command(self, name, parameters):
        call = daemon_pb2.Command(command=COMMANDS[name], parameters=parameters)
        response = self.stub.callCommand(call)
        if response.status == daemon_pb2.Status.NOK:
            raise RemoteError("Error during {}.".format(name))
        else:
            logger.info("{} triggered!".format(name))

    def stop_command(self, name):
        call = daemon_pb2.Interruption()
        response = self.stub.stopCommand(call)
        if response.status == daemon_pb2.Status.NOK:
            raise RemoteError("Error during stop {}.".format(name))
        else:
            logger.info("{} stopped!".format(name))

    def run_dryrun(self, actions, profiling):
        parameters = {
            'action': actions,
            'profiling': str(profiling)
        }

        self.call_command('DRYRUN', parameters)

    def run_grpc(self, actions, max_workers, max_rpc_workers):
        parameters = {
            'action': actions
        }
        self.call_command('GRPC', parameters)

    def stop_grpc(self):
        self.stop_command('GRPC')

    def run_notebook(self, port, enable_security):
        parameters = {
            'port': port,
            'enable_security': str(enable_security)
        }
        self.call_command('NOTEBOOK', parameters)

    def run_lab(self, port, enable_security):
        parameters = {
            'port': port,
            'enable_security': str(enable_security)
        }
        self.call_command('LAB', parameters)

    def run_test(self, cov, no_capture, pdb, args):
        parameters = {
            'cov': str(cov),
            'no_capture': str(no_capture),
            'pdb': str(pdb),
            'args': args
        }

        self.call_command('TEST', parameters)

    def run_tdd(self, cov, no_capture, pdb, partial, args):
        parameters = {
            'cov': str(cov),
            'no_capture': str(no_capture),
            'pdb': str(pdb),
            'partial': str(partial),
            'args': args
        }

        self.call_command('TDD', parameters)

    def run_tox(self, args):
        parameters = {
            'args': args
        }

        self.call_command('TOX', parameters)