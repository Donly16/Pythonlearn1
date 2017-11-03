import os
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

print(PATH('E:\\apk\\app-release.apk'))
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.join('E:\workspace\Pythonlearn1\src\test','E:\\apk\\app-release.apk')))