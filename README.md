# `pathenv`

A Python package for manipulating the `PATH` environment variable.

## Installation

```bash
pip install pathenv
```

## Usage

```python
from pathenv import add_to_path, remove_from_path, refresh_path

# Add a new directory to the PATH
add_to_path("/path/to/new/directory")

# Remove a directory from the PATH
remove_from_path("/path/to/old/directory")

# Refresh the PATH
refresh_path()
```

## Features

- **Cross-platform:** Works on Windows, Linux, and macOS.
- **Simple API:** Easy to use with a few functions.
- **Safe:** Doesn't modify the system `PATH` without your consent.
- **Well-tested:** Thoroughly tested for reliability.

## Examples

### Add a directory to the `PATH`

```python
from pathenv import add_to_path

add_to_path("/usr/local/bin")
```

### Remove a directory from the `PATH`

```python
from pathenv import remove_from_path

remove_from_path("/usr/local/bin")
```

### Refresh the `PATH`

```python
from pathenv import refresh_path

refresh_path()
```

## Documentation

For more detailed documentation, please refer to the [API documentation](./pathenv.md).

## License

`pathenv` is released under the GNU General Public License v2.0.