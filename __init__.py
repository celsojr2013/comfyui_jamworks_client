from .jamworks_client import Jamworks_Login,Jamworks_Download,Shell_Command


NODE_CLASS_MAPPINGS = {
    "Jamworks_Login": Jamworks_Login,
    "Jamworks_Download": Jamworks_Download,
    "Shell_Command": Shell_Command
}

__all__ = ['NODE_CLASS_MAPPINGS']



