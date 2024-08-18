
# CmdInterface Class Documentation

## CmdInterface Class

### Constructor: `__init__`

**Parameters:**
- `nude` (bool, optional): If `True`, removes command signals from the command output. Defaults to `True`.
- `rm_boilerplate` (bool, optional): If `True`, sends an initial command to clear unnecessary startup text from the command line interface. Defaults to `True`.
- `end_signal` (str, optional): A unique string used to indicate the end of a command's output. It helps to ensure the command output does not mix with regular output. Defaults to a random string unlikely to occur in normal output.
- `log_mode` (bool, optional): If `True`, logs all terminal text internally. Useful for debugging or tracking command history. Defaults to `False`.

**Behavior:**
- Initializes an instance of the `CmdInterface` class.
- Creates a subprocess that runs the command line interface (`cmd`).
- Sets up basic properties and manages an initial empty command if `rm_boilerplate` is `True`.

### Destructor: `__del__`

**Behavior:**
- Ensures the subprocess is properly closed and terminated when the `CmdInterface` instance is destroyed.

### Method: `kill`

**Behavior:**
- Similar to `__del__`, this method explicitly closes and terminates the associated subprocess.

### Method: `send_command`

**Parameters:**
- `command` (str): The command string to be executed in the command line interface.

**Behavior:**
- Sends a command to the command line interface.
- Appends a unique end signal to the command to detect when the output ends.
- Waits and collects the output until the end signal is detected.
- Optionally strips the command end signal from the output if `nude` is `True`.
- If `log_mode` is `True`, adds the output to the internal log.
- Handles concurrent command sending using a thread locking mechanism but no ordered queue.

**Returns:**
- `output` (list of str): The output lines in a list produced by the command, optionally cleaned of command signals.

### Method: `get_log`

**Returns:**
- A copy of the log list containing all command outputs logged so far.

### Method: `turn_on_logging`

**Behavior:**
- Enables logging mode, which causes all outputs to be saved to the internal log.

### Method: `turn_off_logging`

**Behavior:**
- Disables logging mode, stopping the accumulation of outputs in the internal log.

### Method: `get_command_count`

**Returns:**
- The total number of commands sent since the instance was created. Minus the optional starting command that clears boilerplate.
