from adisp import process
from helpers import dependency
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IBrowserController

def init():
    g_playerEvents.onGuiCacheSyncCompleted += __showBrowser
class BrowserWindow(object):
                       
    @process
    def browser(self, url, title, browserID, browserSize): 
        browserCtrl = dependency.instance(IBrowserController)
        yield browserCtrl.load(url=url, title=title, browserID=browserID, browserSize=browserSize, showActionBtn=True, showCloseBtn=True, showWaiting=False, useBrowserWindow=True)

g_browserWindow = BrowserWindow()

def __showBrowser(*args): 
    print 'mod_testbrowser2:onGuiCacheSyncCompleted'
    g_browserWindow.browser('http://www.yahoo.co.jp', 'Example', 'ExampleID', [990,550])
