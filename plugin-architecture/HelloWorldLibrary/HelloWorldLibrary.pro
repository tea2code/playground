#-------------------------------------------------
#
# Project created by QtCreator 2014-03-02T12:13:10
#
#-------------------------------------------------

QT       -= core gui

TARGET = HelloWorldLibrary
TEMPLATE = lib

DEFINES += HELLOWORLDLIBRARY_LIBRARY

SOURCES += helloworldlibrary.cpp

HEADERS += helloworldlibrary.h\
        helloworldlibrary_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}
