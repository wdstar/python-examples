# python-examples
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wdstar_python-examples&metric=alert_status)](https://sonarcloud.io/dashboard?id=wdstar_python-examples)

## Development

1. Install dependencies and tools.
    ```bash
    $ pip install pipenv
    $ pipenv install --dev
    ```
1. Format and test.
    ```bash
    $ pipenv run format
    $ pipenv run test
    $ pipenv run pytest tests/sample.py
    ```

## Examples

```bash
$ pipenv run src/examples/cli.py log sample
$ pipenv run src/examples/closure_sample.py
$ pipenv run src/examples/logging_sample.py
```