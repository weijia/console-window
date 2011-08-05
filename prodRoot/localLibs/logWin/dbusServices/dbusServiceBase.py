import dbus.service

################################################################
#Required !!! Override the following interface name
INTERFACE_NAME = 'com.wwjufsdatabase.dbusServiceBaseInterface'


class dbusServiceBase(dbus.service.Object):
    #The following function declaration is just a sample of overiding __init__ of class dbus.service.Object
    '''
    def __init__(self, sessionBus, objectPath):
        dbus.service.Object.__init__(self, sessionBus, objectPath)
    '''
    #The following function declaration is just a sample of dbus method
    '''
    @dbus.service.method(dbus_interface=INTERFACE_NAME,
                         in_signature='s', out_signature='s')
    def register(self, taskName):
        if (self.taskList.has_key(taskName)) and (self.taskList[taskName]["status"] ==
                "started"):
            return 'Already registered'
        else:
            self.taskList[taskName] = {"status":"started"}
        return 'Task created'
    '''
    pass
    