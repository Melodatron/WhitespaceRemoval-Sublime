import sublime
import sublime_plugin

class RemoveSelectedWhitespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel();
		for region in selection:
			selStr = self.view.substr(region);
			newStr = "".join(selStr.split());
			self.view.replace(edit, region, newStr);
