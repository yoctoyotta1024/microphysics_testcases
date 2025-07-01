Our Tests
=========

This project uses pytest for executing the Python tests in the `./tests` directory. These tests are
included in the CI.yaml and can be used to test both Python and C++ code.

.. _python-test:

Testing Python Code
###################

Easily done with pytest!

Simply import the code you want to test (e.g. module, function, class etc.)
within a script called ``./tests/test_[name].py`` with a "name" of your choosing in the `./tests`
directory.

Then run pytest on the entire tests directory or on your test. For example, ``pytest ./tests`` would test
every test in the `./tests` directory, whereas ``pytest test_[name].py`` runs just your test.

Testing C++ Code
################

For testing C++ code, we first make a Python module out of it using pybind11.

C++ Demo Package
----------------
The mock_bindcxx library shows a demonstration of making python bindings assuming pybind11 is
already installed in the `./extern` directory (see `./CMakeLists.txt`). It's no problem if for
some reason you don't have pybind11 already in `./extern` (Maybe you didn't clone this repository
with the ``--recursive`` flag?), we recommend you simply install it using git submodule, e.g.

.. code-block:: console

  $ git submodule add https://github.com/pybind/pybind11.git extern/pybind11
  $ git submodule update --init

You can then build and compile the python module for this C++ code.

Creating The Python Bindings
----------------------------

To build the python bindings for the C++ Demo Package and CLEO you can simply do
`` cmake -S ./ -B ./build && cd build && make mock_cxx pycleo``. However, you need to have certain
:ref:`requirements <requirements>` fulfilled first (compiler versions etc.). On Levante, we
therefore reccomend you use the bash helper script ``scripts/compile_bindings_levante.sh`` instead
of directly calling cmake.

First activate the python environment you want to use, e.g. ``micromamba activate microtestsenv``.
Then call the helper script with the source and build directories you want to use, e.g.

.. code-block:: console

  $ ./scripts/compile_bindings_levante.sh $HOME/microphysics_testcases $HOME/microphysics_testcases/build

After making the bindings, the Python modules can then tested using
pytest just :ref:`like an ordinary python module <python-test>`.

You can find out more about pybind11 by visiting
`their repository <https://github.com/pybind/pybind11/>`_
