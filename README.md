# freezedry
A simple method to store a compressed copy of a code repository with customizable filtering of files.

[![PyPI version](https://badge.fury.io/py/freezedry.svg)](https://badge.fury.io/py/freezedry)

Do you ever wish you knew exactly which version of code you used when you made a figure, ran a job
on a HPC cluster, or anything else? Freezedry is the solution! 

With freezedry, you can easily save a compressed copy of an entire file directory that is designed
to focus on _code_. Freezedry is a very simple package-- it only has one method you need to use
(``freezedry``) that takes as input a path to a directory and a path to an output file, along with
a few customizable optional input arguments. 

What does freezedry include? Everything, if you don't specify. However, it's very easy to ignore:
- git related files (i.e. anything with the pattern ``.git`` in the file path)
- anything specified in a ``.gitignore`` file (thank you to [Michael Herrmann](https://github.com/mherrmann))
for the useful [gitignore_parser](https://github.com/mherrmann/gitignore_parser) package.
- anything else you want (including exact string matches and regular expressions).

## Installation
It's on PyPI. If there's any issues, please raise one on this GitHub repo to let me know.
```
pip install freezedry
```

## Usage
Suppose that ``/..dirs../GitHub/your_repo`` contains some code you've been working on. And say you
use the code in ``your_repo`` to do some analyses that are saved to ``/..dirs../results``. Then,
the following block of code will save a copy of your repo to the ``/results`` directory, ignoring
any ``.git`` related files and ignoring anything in your ``.gitignore``. 

```python
from freezedry import freezedry
directory_path = '/..dirs../GitHub/your_repo'
output_path = '/..dirs../results'
freezedry(directory_path, output_path=output_path, ignore_git=True, use_gitignore=True, verbose=True)
```

## Contributing
I'm happy to take issues or pull requests, let me know if you have any ideas on how to make this
better or requests for fixes. 
