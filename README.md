# python-template

![Python tests](https://github.com/Liamdoult/python-template/workflows/Python%20tests/badge.svg)

A template project for quickly generating python project boilerplate code.

This is not a beginners project sturcture guide, for that see [pypa/sampleproject](https://github.com/pypa/sampleproject). This is more of a quick setup tool for starting projects according to my favourite best practices.

[//]: <> (This section bellow should be deleted as it only provids information on how to get started with this template repository)
[//]: <> (======================= Delete Me when complete =====================)
## Checklist

This is a list of things you need to do when you first clone or base a new repository off of this template.

- [ ] Rename modules and package
    - [ ] name in `setup.py`: `name="<package_name>"`
    - [ ] package name in the source folder: `src/<package_name>`
    - [ ] name in tox.ini: `--cov=<package_name>`


[//]: <> (=====================================================================)

## Testing

All tests are written in with pytest. You can simply run the test suite with tox:

    $ tox
