FreezeDry Documentation
======================

FreezeDry is a Python package that provides a simple way to create compressed copies of code repositories with customizable filtering options. It's designed to help you preserve exact versions of code used for specific tasks, such as generating figures or running analysis jobs.

Installation
------------

.. code-block:: bash

   pip install freezedry

Quick Start
----------

Here's a simple example showing how to use FreezeDry:

.. code-block:: python

   from freezedry import freezedry

   # Create a compressed copy of your code directory
   freezedry(
       directory_path="path/to/your/code",
       output_path="path/to/output.zip",
       ignore_git=True,
       use_gitignore=True,
       verbose=True
   )

User Guide
----------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   api_reference
   examples

Use Cases
---------

- 📊 **Research Reproducibility**: Save exact code versions used for analyses
- 🔬 **Project Snapshots**: Create lightweight archives of project states
- 📦 **Code Distribution**: Share filtered versions of repositories
- 🔄 **Version Tracking**: Keep track of code used for specific results

Contributing
-----------

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.