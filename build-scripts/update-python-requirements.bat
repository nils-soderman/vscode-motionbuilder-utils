REM Install / Upgrade the python requirements used to generate stub files & documentation content files

pip install --target="%~dp0/python/site-packages/" --upgrade https://github.com/nils-soderman/pyfbsdk-stub-generator/zipball/master