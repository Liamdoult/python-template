# python-template
A template project for quickly generating python project boilerplate code.

This is not a beginners project sturcture guide, for that see [pypa/sampleproject](https://github.com/pypa/sampleproject). This is more of a quick setup tool for starting projects according to my favourite best practices.


## Testing

All tests are written in with pytest. You can simply run the test suite with tox:

    $ tox

    GLOB sdist-make: /mnt/c/Users/Liam/Documents/projects/python-template/setup.py
    py37 inst-nodeps: /mnt/c/Users/Liam/Documents/projects/python-template/.tox/.tmp/package/1/python-template-0.0.1.zip
    py37 installed: attrs==19.3.0,importlib-metadata==1.6.0,more-itertools==8.2.0,packaging==20.3,pluggy==0.13.1,py==1.8.1,pyparsing==2.4.7,pytest==5.4.2,python-template @ file:///mnt/c/Users/Liam/Documents/projects/python-template/.tox/.tmp/package/1/python-template-0.0.1.zip,six==1.14.0,wcwidth==0.1.9,zipp==3.1.0
    py37 run-test-pre: PYTHONHASHSEED='1671923677'
    py37 run-test: commands[0] | pytest
    ======================================================================================================== test session starts =========================================================================================================
    platform linux -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    cachedir: .tox/py37/.pytest_cache
    rootdir: /mnt/c/Users/Liam/Documents/projects/python-template
    collected 1 item

    test/test_simple.py .                                                                                                                                                                                                          [100%]

    ========================================================================================================= 1 passed in 0.03s ==========================================================================================================
    ______________________________________________________________________________________________________________ summary _______________________________________________________________________________________________________________
      py37: commands succeeded
      congratulations :)
