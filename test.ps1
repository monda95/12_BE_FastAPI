poetry run black .
if(!$?) { throw }
poetry run ruff check --select I --fix
if(!$?) { throw }
poetry run ruff check --fix
if(!$?) { throw }
poetry run mypy .
if(!$?) { throw }
poetry run coverage run -m pytest .
if(!$?) { throw }
poetry run coverage report -m
poetry run coverage html
if(!$?) { throw }
Write-Host "Done" -ForegroundColor Green

# refer: https://stackoverflow.com/questions/47032005/why-does-a-powershell-script-not-end-when-there-is-a-non-zero-exit-code-using-th