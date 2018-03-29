from adisp import process
from helpers import dependency
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IBrowserController
from skeletons.connection_mgr import IConnectionManager

connectionManager = dependency.instance(IConnectionManager)
class BrowserWindow(object):
                       
    @process
    def browser(self, url, title, browserID, browserSize): 
        browserCtrl = dependency.instance(IBrowserController) 
        yield browserCtrl.load(url=url, title=title, browserID=browserID, browserSize=browserSize, showActionBtn=True, showCloseBtn=True, showWaiting=False, useBrowserWindow=True)

g_browserWindow = BrowserWindow()

def onAccountShowGUI(ctx): 
    print 'mod_testbrowser:onAccountBecomePlayer'
    g_browserWindow.browser('http://www.yahoo.co.jp', 'Example', 'ExampleID', [990,550])
