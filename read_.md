# Utility Functions for developersAuthor: Shaon MajumderStable Version: 0.0.0.46.1## Utilities- stats- network- image- string- file## Installation	pip install shaonutil## Function Usages

### setup

setup - The gateway to the Distutils: do everything your setup script needs
    to do, in a highly flexible and user-driven way.  Briefly: create a
    Distribution instance; find and parse config files; parse the command
    line; run each Distutils command found there, customized by the options
    supplied to 'setup()' (as keyword arguments), in config files, and on
    the command line.

    The Distribution instance might be an instance of a class supplied via
    the 'distclass' keyword argument to 'setup'; if no such class is
    supplied, then the Distribution class (in dist.py) is instantiated.
    All other arguments to 'setup' (except for 'cmdclass') are used to set
    attributes of the Distribution instance.

    The 'cmdclass' argument, if supplied, is a dictionary mapping command
    names to command classes.  Each command encountered on the command line
    will be turned into a command class, which is in turn instantiated; any
    class found in 'cmdclass' is used in place of the default, which is
    (for command 'foo_bar') class 'foo_bar' in module
    'distutils.command.foo_bar'.  The command class must provide a
    'user_options' attribute which is a list of option specifiers for
    'distutils.fancy_getopt'.  Any command-line options between the current
    and the next command are used to set attributes of the current command
    object.

    When the entire command-line has been successfully parsed, calls the
    'run()' method on each command object in turn.  This method will be
    driven entirely by the Distribution object (which each command object
    has a reference to, thanks to its constructor), and the
    command-specific options that became attributes of each command
    object.
    



Function Usages End## Versioning *major.minor[.maintenance[.build]]* (example: *1.4.3.5249*) adoption: major.minor.patch.maintenance.status.trials_for_successThe last position - 0 for alpha (status)- 1 for beta (status)- 2 for release candidate- 3 for (final) releaseFor instance: - 1.2.0.1 instead of 1.2-a1- 1.2.1.2 instead of 1.2-b2 (beta with some bug fixes)- 1.2.2.3 instead of 1.2-rc3 (release candidate)- 1.2.3.0 instead of 1.2-r (commercial distribution)- 1.2.3.5 instead of 1.2-r5 (commercial distribution with many bug fixes)