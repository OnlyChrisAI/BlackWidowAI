[app]
title = BlackWidow
package.name = blackwidow
package.domain = com.fatherchris.blackwidow
source.dir = .
source.include_exts = py,png,jpg,kv,wav,mp3
version = 37
requirements = python3,kivy,pygame,edge-tts,aiohttp
orientation = portrait
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,RECORD_AUDIO
android.api = 33
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2