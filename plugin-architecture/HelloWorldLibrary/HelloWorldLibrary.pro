#-------------------------------------------------
#
# Project created by QtCreator 2014-03-02T12:13:10
#
#-------------------------------------------------

TARGET = HelloWorldLibrary
TEMPLATE = lib

DEFINES += PLUGIN_LIBRARY

SOURCES += helloworldlibrary.cpp

HEADERS += helloworldlibrary.h

# Compiler features.
QMAKE_CXXFLAGS += -std=c++11

# Activate warnings.
QMAKE_CXXFLAGS += -pedantic -Wall -Wextra -Werror

# Deactivate some unnecessary warnings. Best to use "-Wno-error=..." and keep warnings.
QMAKE_CXXFLAGS += -Wno-error=unused-parameter

unix {
    target.path = /usr/lib
    INSTALLS += target
}
