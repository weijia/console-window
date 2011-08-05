import dbus.mainloop.glib
import dbus
import localLibSys
import localLibs.logWin.dbusServices.dirMonitorService as dirMonitorService
import localLibs.logWin.appStarterForDbusV2 as appStarterForDbus
import gobject

#BUS_NAME_NAME = 'com.wwjufsdatabase.appStarterService'
BUS_NAME_NAME = 'com.wwjufsdatabase.dirMonitorService'

class dbusServiceApp:
    def startAppRunnerService(self, serviceObjName = '/appStarter', serviceClass = appStarterForDbus.appStarter):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        session_bus = dbus.SessionBus()
        name = dbus.service.BusName(BUS_NAME_NAME, session_bus)
        mainloop = gobject.MainLoop()
        
        ############################
        #Start app starter service
        ############################
        #Set message target so start app message can be sent to the GTK desktop application. And the GTK desktop
        #application will start the real application and add entry to task bar icon menu.
        object = serviceClass(session_bus, serviceObjName)

        ############################
        #Start main message loop for DBus services
        ############################
        mainloop.run()
        '''
        if not (processObj is None):
            print 'processing:', processObj.pid, int(processObj._handle)
            processManager.killChildProcessTree(processObj.pid)
            win32api.TerminateProcess(int(processObj._handle), -1)
        '''
        print 'quitting mainloop.run()'


if __name__ == "__main__":
    a = dbusServiceApp()
    a.startAppRunnerService('/dirMonitor', dirMonitorService.dirMonitorService)
