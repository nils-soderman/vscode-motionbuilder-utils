cd "%~dp0../"
rmdir /S /Q "./out/"

set OutDir="./dist/"

if not exist %OutDir% (
    mkdir %OutDir%
)

vsce package --out %OutDir%