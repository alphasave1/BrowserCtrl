import BigWorld
from notification.NotificationListView import NotificationListView
from notification.settings import NOTIFICATION_BUTTON_STATE
from gui.SystemMessages import SM_TYPE
from adisp import process



def messages():
    return {'typeID': 1,
     'message': {'bgIcon': '',
                 'defaultIcon': '',
                 'savedData': 0,
                 'timestamp': -1,
                 'filters': [],
                 'buttonsLayout': [{'action': 'action_1',
                                    'type': 'submit',
                                    'label': 'WGMODS',
                                    'width': 65},
                                    {'action': 'action_2',
                                    'type': 'submit',
                                    'label': 'KoreanRandom',
                                    'width': 65}, 
                                    {'action': 'action_3',
                                    'type': 'submit',
                                    'label': 'GoogleJP',
                                    'width':65}],
                 'message': 'InternalBrowser',
                 'type': 'black',
                 'icon': ''},
     'entityID': 99999,
     'auxData': ['GameGreeting']}


def new_getMessagesList(self):
    result = old_getMessagesList(self)
    if self._NotificationListView__currentGroup in 'info':
        result.append(messages())
    return result


old_getMessagesList = NotificationListView._NotificationListView__getMessagesList
NotificationListView._NotificationListView__getMessagesList = new_getMessagesList

import BigWorld

from adisp import process
from helpers import dependency
from skeletons.gui.game_control import IBrowserController

class BrowserWindow(object):
                       
    @process
    def browser(self, url, title, browserID, browserSize): 
        browserCtrl = dependency.instance(IBrowserController) 
        yield browserCtrl.load(url=url, title=title, browserID=browserID, browserSize=browserSize, showActionBtn=True, showCloseBtn=True, showWaiting=True)

g_browserWindow = BrowserWindow()



def new_onClickAction(self, typeID, entityID, action):
    if action == 'action_1':
        g_browserWindow.browser('http://www.wgmods.net', 'WGMODS', 'Pack', [990, 550])
    elif action == 'action_2':
        g_browserWindow.browser('http://koreanrandom.com', 'Mod-Dev', 'Pack_', [990, 550])
    elif action == 'action_3':
        g_browserWindow.browser('http://www.google.co.jp', 'Google-JP', 'Pack__', [990, 550])
    else:
        old_onClickAction(self, typeID, entityID, action)


old_onClickAction = NotificationListView.onClickAction
NotificationListView.onClickAction = new_onClickAction
