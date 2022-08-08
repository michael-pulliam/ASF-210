from collections import ChainMap
from email.policy import default


# ----------------------------------------------------------------------------------------------------------------------------
# Chain Maps
# -----------------------------------------------------------------------------------------------------------------------------


default = {'theme':'Default', 'language':'eng', 'show_index':True, 'show_footer':True}

cm = ChainMap(default) # Creates a chainmap with the dault configuration

cm2 = cm.new_child({'theme':'bluesky'}) # Creates a new chainmap with a child that ovberides the parent

cm2['theme'] # Returns the overidden theme

cm2.pop('theme') # Returns and removes child theme value

cm2['theme'] # Returns the default theme

cm2.maps[0] = {'theme':'desert', 'show_index':False} # adds a 'root context" same as new_child

cm2['show_index'] # Returns the overridden show_index value

cm2.parents # Returns Defaults

""" ChainMap({'theme', 'language':'eng', 'show_index':True, 'show_footer':True}) """