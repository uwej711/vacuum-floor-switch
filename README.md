# Vacuum floor switcher

Simple webapp to select different maps on a rooted Dreame Z10 (if you have the app, you don't need this).

## Configuration

Create a file .env with 

```dotenv
TOKEN=*****************
IP=<ip of your robot>
DEVICE_ID=***************
LOWER_FLOOR_ID=3
UPPER_FLOOR_ID=4
```

The value for TOKEN can be found as outlined here: https://python-miio.readthedocs.io/en/latest/legacy_token_extraction.html.

The device id can be any random number.

LOWER_FLOOR_ID and UPPER_FLOOR_ID have to be found on the device.

## Known issues

The UI is the bare minimum ...
