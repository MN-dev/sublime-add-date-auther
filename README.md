# sublime-add-date-auther
automatic update date in sublime

  /** 
 *@auther 
 *@huntereyes93@gmail.com 
 *2016-11-18 16:56:47 
  **/


# Preferences > Key Bindings- User

[
    {"keys": ["ctrl+s"], "command": "date_and_save" }
]


#  add_date.py

import datetime, getpass
import sublime, sublime_plugin

class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") } )

class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime(" /** \n@auther \n@huntereyes93@gmail.com \n %Y-%m-%d %H:%M:%S \n **/") } )

class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.datetime.now().strftime(" ") } )


