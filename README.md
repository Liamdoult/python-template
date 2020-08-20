# python-template

![Python tests](https://github.com/Liamdoult/python-template/workflows/Python%20tests/badge.svg)

A template project for quickly generating python project boilerplate code.

This is not a beginners project sturcture guide, for that see [pypa/sampleproject](https://github.com/pypa/sampleproject). This is more of a quick setup tool for starting projects according to my favourite best practices.

[//]: <> (This section bellow should be deleted as it only provids information on how to get started with this template repository)
[//]: <> (======================= Delete Me when complete =====================)

## Checklist

Use this checklist below to get started:

- [ ] Rename modules and package
    - [ ] name in `setup.py`: `name="<package_name>"`
    - [ ] package name in the source folder: `src/<package_name>`
    - [ ] name in tox.ini: `--cov=<package_name>`
- [ ] Configure your python versions:
    - [ ] Select your python versions in the tox.ini
    - [ ] Select your python versions in the `.github/workflows/standards.yaml`
- [ ] Setup local environment:
    - [ ] (ubuntu) Run `sh .scripts/setup.py` to install template related tools.
    - [ ] (Optional) Setup development install `python setup.py develop`
- [ ] (Optional) Test that everything is working
    - [ ] Run `tox`
    - [ ] Run `python -m template`

[//]: <> (=====================================================================)

## Testing

All tests are written in with pytest. You can simply run the test suite with tox:

    $ tox
