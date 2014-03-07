#include "PluginManager.h"

#include "data.h"

#include <iostream>
#include <string>

int main()
{
    Data data;
    data.greet("Main");

    std::string path = "C:/My/Projects/playground/plugin-architecture/build-HelloWorldLibrary-Desktop_Qt_5_2_1_MinGW_32bit-Debug/debug/HelloWorldLibrary";
    PluginManager pluginManager;
    pluginManager.loadPlugin(path);
    pluginManager.plugin->greet(&data);
    return 0;
}

