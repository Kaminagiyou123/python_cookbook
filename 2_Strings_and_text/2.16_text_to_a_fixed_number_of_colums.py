s = "Look into my eyes, look into my eyes, the eyes, the eyes, \ the eyes, not around the eyes, don't look around the eyes, \ look into my eyes, you're under."
import textwrap
print(textwrap.fill(s,40,initial_indent="  "))

import os
a=os.get_terminal_size().columns
print(a)