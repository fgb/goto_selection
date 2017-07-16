import sublime_plugin

class GotoSelectionCommand( sublime_plugin.WindowCommand ):

  def run( self, select_word_under_cursor = False ):

    view         = self.window.active_view()
    selection    = view.sel()[0]
    overlay_args = { "overlay"    : "goto",
                     "show_files" : True }

    if not selection.empty():
      overlay_args["text"] = view.substr( selection )
    elif select_word_under_cursor:
      overlay_args["text"] = view.substr( view.word( selection ) )

    self.window.run_command( "show_overlay", overlay_args )
