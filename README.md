# password_manager
A terminal password manager.

## NOTE

The generator in this manager doesn't generate a 
truly random password each time the function is
called. When generator.py is run independently, 
the seed is reset and the random.choice() function
selects different characters. I haven't yet figured
out how to manage this issue yet. Ideally, don't use this
manager for anything that needs to be truly secure until
the issue is resolved.
