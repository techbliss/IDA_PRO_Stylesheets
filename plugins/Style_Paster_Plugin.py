# Created by: Storm Shadow http://www.techbliss.org
import os
import ida_idaapi, ida_kernwin
from ida_diskio import *
import idc
from idc import *
from ida_idaapi import *
import sys
sys.path.insert(0 , ida_diskio.idadir("plugins\\Style_Paster")) #change path to the icon
import ico
from ico import *

PLUGIN_VERSION = "1.0" #change Plugin Version
IDAVERISONS    = "IDA PRO 7.0+" #change Ida version
AUTHORS        = "Storm Shadow" #change author
DATE           = "2017" #change date
TWITTER        = "Twitter @zadow28" #change social media

def banner():
    banner_options = (PLUGIN_VERSION, AUTHORS, DATE, TWITTER, IDAVERISONS)
    banner_titles = "StyleSheet Paster v%s - (c) %s - %s - %s - %s" % banner_options #change Python editor

# print plugin banner
    print("---[" + banner_titles + "]---\n")

banner()

# 1) Create the handler class
class MyEditorHandlerPaste(ida_kernwin.action_handler_t): # the class name must be unique for each plugin nb same as line (53)
    def __init__(self):
        ida_kernwin.action_handler_t.__init__(self)

    # Run editor when invoked.
    def activate(self, ctx):
        g = globals()
        idahome = ida_diskio.idadir("plugins\\Style_Paster") #change to set plguin path where the main plguin script is
        ida_idaapi.IDAPython_ExecScript(idahome + "\\Style_Paste_main.py", globals()) #change for the main plugin script

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_ALWAYS

class ripeyePaste(ida_idaapi.plugin_t): #change class to unique name for each plugin , also change line (103)
    flags = ida_idaapi.PLUGIN_FIX #different flags this is for plugin visible at startup
    comment = "Run me" #help me text
    help = "StyleSheet Paster" #help text
    wanted_name = "StyleSheet Paster" #change the plugins name
    wanted_hotkey = "" #the tooltip goes away in menu when setting it here ,DONT DO it! and only is shown in File/Plugins menu


    def editor_menuactionPaste(self): #change for something unique.also change line (90)
        action_desc = ida_idaapi.action_desc_t(
            'my:editoractionPaste',  # The action name. This acts like an ID and must be unique same as line (64), (68)
            'StyleSheet Paster',  # The action text.
            MyEditorHandlerPaste(),  # The action handler must be unique , also change line (99)
            'Ctrl+P',  # Optional: the action shortcut DO IT  HERE!
            'Paste and test your custom styles',  # Optional: the action tooltip (available in menus/toolbar)
            ida_idaapi.load_custom_icon(idaapi.idadir("plugins\\Style_Paster")+"\\iconss.png")  # hackish load action icon , if no custom icon use number from 1-150 from internal ida
        )

        # 3) Register the action
        ida_idaapi.register_action(action_desc)

        ida_idaapi.attach_action_to_menu(
            'File/StyleSheet Paster...',  # The relative path of where to add the action
            'my:editoractionPaste',  # The action ID (see line(51))
            ida_idaapi.SETMENU_APP)  # We want to append the action after the 'Manual instruction...

        form = idaapi.get_current_tform()
        ida_idaapi.attach_action_to_popup(form, None, "my:editoractionPaste", None) # The action ID (see line(51)

    def init(self):
        """
        This is called by IDA when it is loading the plugin.
        """
        #self._icon_id_file = idaapi.BADADDR
        # attempt plugin initialization
        try:
            self._install_plugin()

        # failed to initialize or integrate the plugin, log and skip loading
        except Exception as e:
            form = ida_kernwin.get_current_tform()
            pass

        return PLUGIN_KEEP

    def _install_plugin(self):
        """
        Initialize & integrate the plugin into IDA.
        """
        self.editor_menuactionPaste() #same as line (49)
        self._init()

    def term(self):
        pass

    def run(self, arg = 0):
        #we need the calls again if we wanna load it via File/Plugins/editor
        ida_kernwin.msg("StyleSheet Paster Loaded to menu \n use Alt+P hot key to quick load ")
        hackish = MyEditorHandlerPaste() #must be the same as line (53) change also hackish =  must be unique also line (100)
        hackish.activate(self)  #hackish must the same as line hackish = (99)

def PLUGIN_ENTRY():
    return ripeyePaste() #must be unique for each plugin and same as line 43