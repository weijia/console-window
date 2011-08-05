import scriptRunnerV2 as scriptRunner
import gobject
import threading
import gtk
import appStarterForDbusV2 as appStarterForDbus



class scriptLauncherDbusTherd(threading.Thread):
    def __init__(self, target):
        self.target = target
        threading.Thread.__init__(self)
    def run(self):
        #Connect to server
        appStarterForDbus.startAppRunnerService(self.target)
        print 'quit running appStarterForDbus.startAppRunnerService(self.target)'


class advScriptRunner(scriptRunner.dropRunWnd):
    def startScriptRunnerApp(self):
        scriptRunner.dropRunWnd.startScriptRunnerApp(self)
        self.dbusThread = scriptLauncherDbusTherd(self)
        self.dbusThread.start()
    def quitAll(self):
        appStarterForDbus.stopAllService()
        
    def addAppToIdleRunner(self, param):
        print 'callback called'
        gobject.idle_add(self.lauchServerLaunch, param)
        import time
        time.sleep(0.1)

    def lauchServerLaunch(self, param):
        self.startAppWithParam(param)
    

def startApplicationsNoReturn(l):
    '''
    from dbus.mainloop.glib import threads_init
    threads_init()
    '''
    d = advScriptRunner()
    d.initialApps = l
    d.startScriptRunnerApp()
    gtk.gdk.threads_enter()
    gtk.main()
    gtk.gdk.threads_leave()
    print 'after gtk.gdk.threads_leave()'
    d.quitAll()
    print 'final quit'
    return 0
    
  
def main():
    startApplicationsNoReturn([])

if __name__ == "__main__":
    main()
