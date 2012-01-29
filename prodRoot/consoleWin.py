import localLibs.logWin.advScriptRunnerV3 as scriptRunner
import localLibs.logWin.advScriptRunnerXmlRpcServer as advScriptRunnerXmlRpcServer


gAutoStartapp = []

def main():
    scriptRunner.startApplicationsNoReturn(gAutoStartapp, 
                                            advScriptRunnerXmlRpcServer.launcherXmlRpcThread)

if __name__ == "__main__":
    main()
