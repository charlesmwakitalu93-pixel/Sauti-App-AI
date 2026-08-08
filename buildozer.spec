[app]

# (str) Title of your application
title = Sauti App AI

# (str) Package name
package.name = sautiappai

# (str) Package domain (needed for android packaging)
package.domain = org.sauti.ai

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude all files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude all directories)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,pillow,urllib3,certifi,charset-normalizer,idna,requests

# (str) Custom source folders for requirements
#requirements.source.dir = ../kivy

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Architectural build to support
android.archs = arm64-v8a

# (list) Graphics
#android.graphics = glesv2

# (str) Orientations to support
orientation = portrait

# (list) The format used to package the app for store
android.formats = apk,aab

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
