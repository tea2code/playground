TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    MyNode.cpp

QMAKE_CXXFLAGS += -std=c++11

INCLUDEPATH += $$PWD/../../../libraries/boost_1_55_0
INCLUDEPATH += $$PWD/../../../libraries/yaml-cpp/include

unix|win32: LIBS += -L$$PWD/../../../libraries/yaml-cpp -lyaml-cpp

HEADERS += \
    MyNode.h
