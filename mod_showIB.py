import game
import BigWorld
from adisp import process
from helpers import dependency
from skeletons.gui.game_control import IBrowserController
import Keys
import ResMgr
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.app_loader import g_appLoader

class MOD:
    AUTHOR = 'Chirimen , alphasave1'
    NAME = 'HideHangarUI'
    VERSION = '1.0'
    DESCRIPTION = 'If You Push F11 Key, Hangar UI Will Hide.'
    SUPPORT_URL = 'http://www.twitter.com/alphasave1'


class BrowserWindow(object):
                       
    @process
    def browser(self, url, title, browserID, browserSize): 
        browserCtrl = dependency.instance(IBrowserController) 
        yield browserCtrl.load(url=url, title=title, browserID=browserID, browserSize=browserSize, showActionBtn=True, showCloseBtn=True, showWaiting=True)

g_browserWindow = BrowserWindow()

hangar = None

def toggleHangarUI():
    g_browserWindow.browser('http://sky.geocities.jp/soviet_is_3/index__.html', 'COIN', 'Pack', [990, 550])


def handleKeyEvent(event):
    ret = wg_handleKeyEvent(event)
    try:
        if event.isKeyDown() and not event.isRepeatedEvent():
            if event.key == Keys.KEY_F11:
                toggleHangarUI()
    except:
        LOG_CURRENT_EXCEPTION()

    return ret


wg_handleKeyEvent = game.handleKeyEvent
game.handleKeyEvent = handleKeyEvent
