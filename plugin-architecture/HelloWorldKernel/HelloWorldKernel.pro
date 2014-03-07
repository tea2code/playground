TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    PluginManager.cpp \
    data.cpp

HEADERS += \
    PluginLoader.h \
    PluginApi.h \
    PluginManager.h \
    data.h \
    DataInterface.h

# Compiler features.
QMAKE_CXXFLAGS += -std=c++11

# Activate warnings.
QMAKE_CXXFLAGS += -pedantic -Wall -Wextra -Werror

# Deactivate some unnecessary warnings. Best to use "-Wno-error=..." and keep warnings.
QMAKE_CXXFLAGS += -Wno-error=unused-parameter
