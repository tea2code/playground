#include "PluginManager.h"

#include <iostream>
#include <string>

int main()
{
    std::string path = "F:/Programmieren/playground/plugin-architecture/"
                       "build-HelloWorldLibrary-Desktop_Qt_5_2_1_MinGW_32bit-Release/"
                       "release/HelloWorldLibrary";
    PluginManager pluginManager;
    pluginManager.loadPlugin(path);
    pluginManager.plugin->greet();
    return 0;
}

