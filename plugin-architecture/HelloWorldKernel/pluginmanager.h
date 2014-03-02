#ifndef PLUGINMANAGER_H
#define PLUGINMANAGER_H

#include "PluginApi.h"

#include <map>
#include <memory>
#include <string>

class PluginManager
{
public:
    PluginManager();
    void loadPlugin(const std::string &path);

private:
    typedef std::shared_ptr<PluginApi> RegisterPluginFunction();
    typedef int GetEngineVersionFunction();

public:
    std::shared_ptr<PluginApi> plugin;
};

#endif // PLUGINMANAGER_H
