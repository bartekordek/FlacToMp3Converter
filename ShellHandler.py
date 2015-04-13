import os.path

class ShellOp:
    @staticmethod
    def ExecuteShellCommand(command):
        os.system(command)