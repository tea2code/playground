#include "PluginManager.h"

#include "PluginLoader.h"

PluginManager::PluginManager()
{
}

void PluginManager::loadPlugin(const std::string &path)
{
    PluginLoader::HandleType handleType = PluginLoader::load(path);
    RegisterPluginFunction *registerPluginFunction = PluginLoader::getFunctionPointer<RegisterPluginFunction>(handleType, "registerPlugin");
    plugin = registerPluginFunction();
}
