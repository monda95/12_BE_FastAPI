# PowerShell에서 오류 발생 시 스크립트 중단 (bash의 set -eo pipefail와 동일)
$ErrorActionPreference = "Stop"

# 색상 설정 (bash의 COLOR_GREEN과 COLOR_NC와 동일)
$COLOR_GREEN = "Green"

Write-Host "Starting black"
poetry run black .
if(!$?) { throw }  # 기존 코드 유지
Write-Host "OK"

Write-Host "Starting ruff"
poetry run ruff check --select I --fix
if(!$?) { throw }  # 기존 코드 유지
poetry run ruff check --fix
if(!$?) { throw }  # 기존 코드 유지
Write-Host "OK"

Write-Host "Starting dmypy"  # mypy에서 dmypy로 변경
poetry run dmypy run -- .     # mypy . 에서 dmypy run -- . 로 변경
if(!$?) { throw }  # 기존 코드 유지
Write-Host "OK"

Write-Host "Starting pytest with coverage"
poetry run coverage run -m pytest  # 기존 코드에 누락된 부분 추가
if(!$?) { throw }  # 기존 코드 유지
poetry run coverage report -m       # 기존 코드에 누락된 부분 추가
if(!$?) { throw }  # 오류 체크 추가
poetry run coverage html            # 기존 코드에 누락된 부분 추가
if(!$?) { throw }  # 오류 체크 추가

# bash의 echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"와 동일
Write-Host "All tests passed successfully!" -ForegroundColor $COLOR_GREEN

# refer: https://stackoverflow.com/questions/47032005/why-does-a-powershell-script-not-end-when-there-is-a-non-zero-exit-code-using-th