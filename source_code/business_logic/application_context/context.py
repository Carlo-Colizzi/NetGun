from source_code.persistence.storage_manager import Storage_manager

"""@author: Carlo Colizzi"""
class Context:
    """This class represents the Entire Application Context, using a Singleton Design Pattern"""
    __istance = None

    class __impl:
        """Singleton of Context class"""

        def start(self):
            """This method is executed in the starting point of the application, here are loaded all the persistence data in RAM"""
            self.misconfiguration = Storage_manager.load_misconfigurations()
            self.tip = Storage_manager.load_tips()
    def __getattr__(self, attr):
        return getattr(self.__istance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__istance,attr,value)

    def __init__(self):
        if Context.__istance is None:
            Context.__istance = Context.__impl()

        self.__dict__['_Singleton__instance'] = Context.__istance

if __name__ == "__main__":
    context = Context()
    context.start()
    print(vars(context))