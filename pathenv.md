## pathenv API Documentation

This document describes the API for the `pathenv` Python package.

### Functions

#### `add_to_path(new_path)`

Adds a new directory to the `PATH` environment variable.

**Arguments:**

- `new_path`: The path to the directory to add to the `PATH`.

**Returns:**

None

**Raises:**

- `NotImplementedError`: If the platform is not supported.
- `FileNotFoundError`: If the shell configuration file cannot be found.


#### `remove_from_path(new_path)`

Removes a directory from the `PATH` environment variable.

**Arguments:**

- `new_path`: The path to the directory to remove from the `PATH`.

**Returns:**

None

**Raises:**

- `NotImplementedError`: If the platform is not supported.
- `FileNotFoundError`: If the shell configuration file cannot be found.


#### `refresh_path()`

Refreshes the `PATH` environment variable.

**Arguments:**

None

**Returns:**

None

**Raises:**

- `NotImplementedError`: If the platform is not supported.
- `FileNotFoundError`: If the shell configuration file cannot be found.


### Examples

#### Adding a directory to the `PATH`

```python
from pathenv import add_to_path

add_to_path("/usr/local/bin")
```

#### Removing a directory from the `PATH`

```python
from pathenv import remove_from_path

remove_from_path("/usr/local/bin")
```

#### Refreshing the `PATH`

```python
from pathenv import refresh_path

refresh_path()
```

### Supported Platforms

`pathenv` supports the following platforms:

- Windows
- Linux
- macOS

### Unix Shell Support

`pathenv` supports the following shells on unix-like systems:

- Bash
- ZSh
- Sh

### Notes

- `pathenv.remove_frome_path()` doesn't handle every cases on Linux & macOS.
- `pathenv` is designed to work with the user's `PATH` environment variable.
- `pathenv` is safe and does not modify the system `PATH` without your consent.
- `pathenv` is well-tested and reliable.