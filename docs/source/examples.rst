Examples
========

Basic Directory Compression
---------------------------
The simplest use case is to create a compressed copy of a directory:

.. code-block:: python

    from freezedry import freezedry
    
    # Create a basic compressed copy
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip"
    )

After running this code, you'll have a ZIP file containing all files from your directory.

Ignoring Git-Related Files
--------------------------
When working with code repositories, you often want to exclude Git-related files:

.. code-block:: python

    from freezedry import freezedry
    
    # Compress directory while ignoring Git files
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip",
        ignore_git=True,
        verbose=True  # See which files are included
    )

This will exclude any files or directories containing `.git` in their path.

Using .gitignore Patterns
-------------------------
You can leverage your existing .gitignore file to filter files:

.. code-block:: python

    from freezedry import freezedry
    
    # Use .gitignore patterns for filtering
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip",
        use_gitignore=True,
        verbose=True
    )

This example will respect your .gitignore patterns, excluding files like __pycache__, .pyc files, etc.

Custom String Pattern Filtering
-------------------------------
You can specify custom patterns to ignore:

.. code-block:: python

    from freezedry import freezedry
    
    # Ignore files containing specific strings
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip",
        extra_ignore=["temp", "draft", "old"],
        verbose=True
    )

This will ignore any files or directories containing "temp", "draft", or "old" in their paths.

Advanced Regular Expression Filtering
-------------------------------------
For more complex filtering needs, use regular expressions:

.. code-block:: python

    from freezedry import freezedry
    
    # Use regular expressions for precise filtering
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip",
        regexp_ignore=[
            r"\.txt$",           # Ignore .txt files
            r"test_.*\.py$",     # Ignore test files
            r"v\d+/.*"           # Ignore version directories
        ],
        verbose=True
    )

Regular expressions provide powerful pattern matching for specific file naming conventions.

Combining Multiple Filters
--------------------------
You can combine all filtering methods for comprehensive control:

.. code-block:: python

    from freezedry import freezedry
    
    # Combine multiple filtering methods
    freezedry(
        directory_path="path/to/your/code",
        output_path="output.zip",
        ignore_git=True,
        use_gitignore=True,
        extra_ignore=["backup"],
        regexp_ignore=[r"\.log$"],
        verbose=True
    )

This example shows how to combine Git-related filtering, .gitignore patterns, string matching, and regular expressions for precise control over which files are included in your archive.

Research Project Example
------------------------
A practical example for research code preservation:

.. code-block:: python

    from freezedry import freezedry
    from datetime import datetime
    
    # Save code state for a research project
    project_dir = "path/to/research/code"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"code_snapshot_{timestamp}.zip"
    
    freezedry(
        directory_path=project_dir,
        output_path=output_path,
        ignore_git=True,
        use_gitignore=True,
        extra_ignore=["data", "results"],  # Ignore large data directories
        regexp_ignore=[r"\.ipynb$"],       # Ignore Jupyter notebooks
        verbose=True
    )

This example shows how to create a timestamped snapshot of research code while excluding data files, results, and notebooks. It's especially useful when you are running experiments, making graphs, or training models, and want to save the exact code used at each endpoint.
