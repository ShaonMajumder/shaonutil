# Utility Functions for developers    Author: Shaon Majumder    Stable Version: 0.0.0.46.1## Utilities- stats- network- image- string- file## Installation	pip install shaonutil## Function Usages

### file

get_all_functions - shaonutil.file.get_all_functions(object/file/class)

package_exists - check if a python pcakage exists.

pipmain - This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    

read_file - Read File and return lines as list

read_json - Read JSON file and return dictionary

write_file - Write File from string

write_json - Write JSON file

### image

svg2rlg - Convert an SVG file to an RLG Drawing object.

### imgcode

actual_data - Returns data without checksum digit for EAN type

calculate_checksum - Calculates the checksum for EAN13-Code / EAN8-Code return type: Integer

decode - Decode barcode or qrcode

displayBarcode - Mark and show the detected barcode

encode - Encode the data as barcode or qrcode

make_barcode_matrix - Make barcode matrix image

read_live_barcode - Live read the barcode and returns data

reduce - reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.

verify_data - Verify the EAN encoded data

### mysqlDB

Entry - Entry widget which allows displaying simple text.

Label - Label widget which can display text and bitmaps.

MySQL - A class for all mysql actions

Tk - Toplevel widget of Tk which represents mostly the main window
    of an application. It has an associated Tcl interpreter.

create_configuration - Creating Configuration

generateCryptographicallySecureRandomString - Generate a random string in a UUID fromat which is crytographically secure and random

### network

MIMEMultipart - Base class for MIME multipart/* type messages.

MIMEText - Class for generating text/* type MIME documents.

StringIO - Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object.  The newline
argument is like the one of TextIOWrapper's constructor.

url_encoding_to_utf_8 - url_encoding_to_utf_8(url)

### os

PathLike - Abstract base class for implementing the file system path protocol.

_exit - Exit to the system with specified status, without normal exit processing.

_fspath - Return the path representation of a path-like object.

    If str or bytes is passed in, it is returned unchanged. Otherwise the
    os.PathLike interface is used to get the path representation. If the
    path representation is not str or bytes, TypeError is raised. If the
    provided path is not str, bytes, or os.PathLike, TypeError is raised.
    

_putenv - Change or add an environment variable.

abort - Abort the interpreter immediately.

This function 'dumps core' or otherwise fails in the hardest way possible
on the hosting operating system.  This function never returns.

access - Use the real uid/gid to test for access to a path.

  path
    Path to be tested; can be string, bytes, or a path-like object.
  mode
    Operating-system mode bitfield.  Can be F_OK to test existence,
    or the inclusive-OR of R_OK, W_OK, and X_OK.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  effective_ids
    If True, access will use the effective uid/gid instead of
    the real uid/gid.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    access will examine the symbolic link itself instead of the file
    the link points to.

dir_fd, effective_ids, and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

Note that most operations will use the effective uid/gid, therefore this
  routine can be used in a suid/sgid environment to test if the invoking user
  has the specified access to the path.

add_dll_directory - Add a path to the DLL search path.

        This search path is used when resolving dependencies for imported
        extension modules (the module itself is resolved through sys.path),
        and also by ctypes.

        Remove the directory by calling close() on the returned object or
        using it in a with statement.
        

chdir - Change the current working directory to the specified path.

path may always be specified as a string.
On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception.

chmod - Change the access permissions of a file.

  path
    Path to be modified.  May always be specified as a str, bytes, or a path-like object.
    On some platforms, path may also be specified as an open file descriptor.
    If this functionality is unavailable, using it raises an exception.
  mode
    Operating-system mode bitfield.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    chmod will modify the symbolic link itself instead of the file
    the link points to.

It is an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.
dir_fd and follow_symlinks may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.

close - Close a file descriptor.

closerange - Closes all file descriptors in [fd_low, fd_high), ignoring errors.

cpu_count - Return the number of CPUs in the system; return None if indeterminable.

This number is not equivalent to the number of CPUs the current process can
use.  The number of usable CPUs can be obtained with
``len(os.sched_getaffinity(0))``

device_encoding - Return a string describing the encoding of a terminal's file descriptor.

The file descriptor must be attached to a terminal.
If the device is not a terminal, return None.

dup - Return a duplicate of a file descriptor.

dup2 - Duplicate file descriptor.

error - Base class for I/O related errors.

execl - execl(file, *args)

    Execute the executable file with argument list args, replacing the
    current process. 

execle - execle(file, *args, env)

    Execute the executable file with argument list args and
    environment env, replacing the current process. 

execlp - execlp(file, *args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process. 

execlpe - execlpe(file, *args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the current
    process. 

execv - Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings.

execve - Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings.

execvp - execvp(file, args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. 

execvpe - execvpe(file, args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the
    current process.
    args may be a list or tuple of strings. 

fsdecode - Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        

fsencode - Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        

fspath - Return the file system path representation of the object.

If the object is str or bytes, then allow it to pass through as-is. If the
object defines __fspath__(), then return the result of that method. All other
types raise a TypeError.

fstat - Perform a stat system call on the given file descriptor.

Like stat(), but for an open file descriptor.
Equivalent to os.stat(fd).

fsync - Force write of fd to disk.

ftruncate - Truncate a file, specified by file descriptor, to a specific length.

get_exec_path - Returns the sequence of directories that will be searched for the
    named executable (similar to a shell) when launching a process.

    *env* must be an environment variable dict or None.  If *env* is None,
    os.environ will be used.
    

get_handle_inheritable - Get the close-on-exe flag of the specified file descriptor.

get_inheritable - Get the close-on-exe flag of the specified file descriptor.

get_terminal_size - Return the size of the terminal window as (columns, lines).

The optional argument fd (default standard output) specifies
which file descriptor should be queried.

If the file descriptor is not connected to a terminal, an OSError
is thrown.

This function will only be defined if an implementation is
available for this system.

shutil.get_terminal_size is the high-level function which should
normally be used, os.get_terminal_size is the low-level implementation.

getcwd - Return a unicode string representing the current working directory.

getcwdb - Return a bytes string representing the current working directory.

getenv - Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str.

getlogin - Return the actual login name.

getpid - Return the current process id.

getppid - Return the parent's process id.

If the parent process has already exited, Windows machines will still
return its id; others systems will return the id of the 'init' process (1).

isatty - Return True if the fd is connected to a terminal.

Return True if the file descriptor is an open file descriptor
connected to the slave end of a terminal.

kill - Kill a process with a signal.

link - Create a hard link to a file.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
If follow_symlinks is False, and the last element of src is a symbolic
  link, link will create a link to the symbolic link itself instead of the
  file the link points to.
src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
  platform.  If they are unavailable, using them will raise a
  NotImplementedError.

listdir - Return a list containing the names of the files in the directory.

path can be specified as either str, bytes, or a path-like object.  If path is bytes,
  the filenames returned will also be bytes; in all other circumstances
  the filenames returned will be str.
If path is None, uses the path='.'.
On some platforms, path may also be specified as an open file descriptor;\
  the file descriptor must refer to a directory.
  If this functionality is unavailable, using it raises NotImplementedError.

The list is in arbitrary order.  It does not include the special
entries '.' and '..' even if they are present in the directory.

lseek - Set the position of a file descriptor.  Return the new position.

Return the new cursor position in number of bytes
relative to the beginning of the file.

lstat - Perform a stat system call on the given path, without following symbolic links.

Like stat(), but do not follow symbolic links.
Equivalent to stat(path, follow_symlinks=False).

makedirs - makedirs(name [, mode=0o777][, exist_ok=False])

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like
    mkdir, except that any intermediate path segment (not just the rightmost)
    will be created if it does not exist. If the target directory already
    exists, raise an OSError if exist_ok is False. Otherwise no exception is
    raised.  This is recursive.

    

mkdir - Create a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

The mode argument is ignored on Windows.

open - Open a file for low level IO.  Returns a file descriptor (integer).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

pipe - Create a pipe.

Returns a tuple of two file descriptors:
  (read_fd, write_fd)

putenv - Change or add an environment variable.

read - Read from a file descriptor.  Returns a bytes object.

readlink - Return a string representing the path to which the symbolic link points.

If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

remove - Remove a file (same as unlink()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

removedirs - removedirs(name)

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    

rename - Rename a file or directory.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.

renames - renames(old, new)

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    

replace - Rename a file or directory, overwriting the destination.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.

rmdir - Remove a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

scandir - Return an iterator of DirEntry objects for given path.

path can be specified as either str, bytes, or a path-like object.  If path
is bytes, the names of yielded DirEntry objects will also be bytes; in
all other circumstances they will be str.

If path is None, uses the path='.'.

set_handle_inheritable - Set the inheritable flag of the specified handle.

set_inheritable - Set the inheritable flag of the specified file descriptor.

spawnl - spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. 

spawnle - spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. 

spawnv - Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings.

spawnve - Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings.

startfile - Start a file with its associated application.

When "operation" is not specified or "open", this acts like
double-clicking the file in Explorer, or giving the file name as an
argument to the DOS "start" command: the file is opened with whatever
application (if any) its extension is associated.
When another "operation" is given, it specifies what should be done with
the file.  A typical operation is "print".

startfile returns as soon as the associated application is launched.
There is no option to wait for the application to close, and no way
to retrieve the application's exit status.

The filepath is relative to the current directory.  If you want to use
an absolute path, make sure the first character is not a slash ("/");
the underlying Win32 ShellExecute function doesn't work if it is.

stat - Perform a stat system call on the given path.

  path
    Path to be examined; can be string, bytes, a path-like object or
    open-file-descriptor int.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be a relative string; path will then be relative to
    that directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    stat will examine the symbolic link itself instead of the file
    the link points to.

dir_fd and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

It's an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.

stat_result - stat_result: Result from stat, fstat, or lstat.

This object may be accessed either as a tuple of
  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.

Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
or st_flags, they are available as attributes only.

See os.stat for more information.

statvfs_result - statvfs_result: Result from statvfs or fstatvfs.

This object may be accessed either as a tuple of
  (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.

See os.statvfs for more information.

strerror - Translate an error code to a message string.

symlink - Create a symbolic link pointing to src named dst.

target_is_directory is required on Windows if the target is to be
  interpreted as a directory.  (On Windows, symlink requires
  Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
  target_is_directory is ignored on non-Windows platforms.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

system - Execute the command in a subshell.

terminal_size - A tuple of (columns, lines) for holding terminal window size

times - Return a collection containing process timing information.

The object returned behaves like a named tuple with these fields:
  (utime, stime, cutime, cstime, elapsed_time)
All fields are floating point numbers.

times_result - times_result: Result from os.times().

This object may be accessed either as a tuple of
  (user, system, children_user, children_system, elapsed),
or via the attributes user, system, children_user, children_system,
and elapsed.

See os.times for more information.

truncate - Truncate a file, specified by path, to a specific length.

On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception.

umask - Set the current numeric umask and return the previous umask.

uname_result - uname_result: Result from os.uname().

This object may be accessed either as a tuple of
  (sysname, nodename, release, version, machine),
or via the attributes sysname, nodename, release, version, and machine.

See os.uname for more information.

unlink - Remove a file (same as remove()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

urandom - Return a bytes object containing random bytes suitable for cryptographic use.

utime - Set the access and modified time of path.

path may always be specified as a string.
On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception.

If times is not None, it must be a tuple (atime, mtime);
    atime and mtime should be expressed as float seconds since the epoch.
If ns is specified, it must be a tuple (atime_ns, mtime_ns);
    atime_ns and mtime_ns should be expressed as integer nanoseconds
    since the epoch.
If times is None and ns is unspecified, utime uses the current time.
Specifying tuples for both times and ns is an error.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
If follow_symlinks is False, and the last element of the path is a symbolic
  link, utime will modify the symbolic link itself instead of the file the
  link points to.
It is an error to use dir_fd or follow_symlinks when specifying path
  as an open file descriptor.
dir_fd and follow_symlinks may not be available on your platform.
  If they are unavailable, using them will raise a NotImplementedError.

waitpid - Wait for completion of a given process.

Returns a tuple of information regarding the process:
    (pid, status << 8)

The options argument is ignored on Windows.

walk - Directory tree generator.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).

    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).

    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.

    By default errors from the os.scandir() call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.

    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.

    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.

    Example:

    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

    

write - Write a bytes object to a file descriptor.

### process

get_mysql_datadir - Get mysql data directory

kill_duplicate_process - Kill a process if there is more than one instance is running.

obj_details_dump - check dump

remove_aria_log - Removing aria_log.### files to in mysql data dir to restart mysql

start_mysql_server - Start mysql server

### stats

mean - Avearage or mean of elements - shaonutil.stats.mean(list of numbers)

median - Median of elements - shaonutil.stats.median(list of numbers)

mode - Mode of elements - shaonutil.stats.mode(list of numbers)

### strings

change_dic_key - Change dictionary key with new key

generateCryptographicallySecureRandomString - Generate a random string in a UUID fromat which is crytographically secure and random

generateSecureRandomString - Generate a secure random string of letters, digits and special characters 

nicely_print - Prints the nicely formatted dictionary - shaonutil.strings.nicely_print(object)

randomString - Generate a random string of fixed length 

### windows



Function Usages End## Versioning *major.minor[.maintenance[.build]]* (example: *1.4.3.5249*) adoption: major.minor.patch.maintenance.status.trials_for_successThe last position - 0 for alpha (status)- 1 for beta (status)- 2 for release candidate- 3 for (final) releaseFor instance: - 1.2.0.1 instead of 1.2-a1- 1.2.1.2 instead of 1.2-b2 (beta with some bug fixes)- 1.2.2.3 instead of 1.2-rc3 (release candidate)- 1.2.3.0 instead of 1.2-r (commercial distribution)- 1.2.3.5 instead of 1.2-r5 (commercial distribution with many bug fixes)