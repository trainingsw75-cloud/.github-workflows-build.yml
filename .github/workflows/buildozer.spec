[app]
title = My App
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk = 25b
sdk = 33

# Разрешения для Android
android.permissions = INTERNET

# Иконка приложения (если есть)
# icon.filename = %(source.dir)s/icon.png
