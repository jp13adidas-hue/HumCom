[app]

# (str) Title of your application
title = Ventas Dulces

# (str) Package name
package.name = ventasdulces

# (str) Package domain (needed for android packaging)
package.domain = org.jesus

# (str) Source where the main.py file resides
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET
