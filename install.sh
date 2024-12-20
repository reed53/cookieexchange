#!/bin/bash

# Cleanup in case previous execution failed
rm -r target >/dev/null 2>/dev/null
rm cookieExchange.zip >/dev/null 2>/dev/null

mkdir target || exit 1
pip3 install -r requirements.txt --target target
cd target || exit 1
zip -r ../cookieExchange.zip . || exit 1
cd ../cookieexchangebackend || exit 1
zip -r ../cookieExchange.zip *.py || exit 1
cd ..
aws --profile personal lambda update-function-code --function-name cookieexchangelambda --zip-file fileb://cookieExchange.zip >/dev/null || exit 1
rm -r target
rm cookieExchange.zip

aws --profile personal s3 cp --recursive frontend/ s3://cookie-webapp/