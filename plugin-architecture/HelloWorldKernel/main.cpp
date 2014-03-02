#include "PluginLoader.h"
#include "pluginmanager.h"

#include <string>

typedef void RegisterPluginFunction(PluginManager &);

int main()
{
    std::string path = "F:/Programmieren/playground/plugin-architecture/"
                       "build-HelloWorldLibrary-Desktop_Qt_5_2_1_MinGW_32bit-Release/"
                       "release/HelloWorldLibrary";
    PluginLoader::HandleType handleType = PluginLoader::load(path);
    PluginManager pluginManager;
    RegisterPluginFunction *registerPluginFunction = PluginLoader::getFunctionPointer<RegisterPluginFunction>(handleType, "registerPlugin");
    registerPluginFunction(pluginManager);
    return 0;
}

