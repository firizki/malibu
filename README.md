# Malibu
You are on leave. But people keep messages you.
You don't want to uninstall Telegram. But You don't want to make them sad by your 'Read-Only' message.
So, use this Auto-Reply for Telegram.

## Requirement
- Python 3
- [Telethon](https://github.com/LonamiWebs/Telethon) Library
- Telegram [client](https://core.telegram.org/api/obtaining_api_id) API & Hash

## Installation
1. Install Telethon Library
```
pip3 install telethon
```
2. Duplicate env file
```
cp env.sample .env
```
3. Fill the needed env variable
```
API_ID #Your telegram client API
API_HASH #Your telegram client hash
TELEGRAM_PHONE_NUMBER #Your telegram account phone number
TELEGRAM_USERNAME #Just for file session name
TELEGRAM_PASSWORD #Not necessary, only if you have TFA
```
## How To Use
Run the application
```
python3 malibu.py
```
First time application running, It will ask for verification code and create a session login file.
The toggle auto reply feature is default set disable, to enable the auto reply, you need to send message `#toggle` on the saved message.
