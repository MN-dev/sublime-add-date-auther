import datetime, getpass
import sublime, sublime_plugin

class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, args):
        content = self.view.substr(sublime.Region(0, self.view.size()))
        begin = content.find(' * @date')
        if begin == -1:
            return
        end = begin + 19
        target_region = sublime.Region(begin, end)
        self.view.sel().clear()
        self.view.sel().add(target_region)

        self.view.run_command("insert_snippet", { "contents": " * @date %s" %  datetime.date.today().strftime("%Y %m %d") } )

class DateAndSaveCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("add_date")
        self.window.run_command("save")
