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

# (list) Source files to exclude (let empty to exclude none)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to exclude none)
source.exclude_dirs = bin, venv, .git, .github

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

# (str) Android SDK build tools version
android.build_tools_version = 33.0.2

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (list) Permissions
android.permissions = INTERNET

# (bool) Enable AndroidX support
android.androidx = True
