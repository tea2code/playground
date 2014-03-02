#include "helloworldlibrary.h"

#include "helloworldlibrary_global.h"

#include "../HelloWorldKernel/pluginmanager.h"

#include <iostream>

HelloWorldLibrary::HelloWorldLibrary()
{
    std::cout << "Hello Library" << std::endl;
}

extern "C" HELLOWORLDLIBRARY_API void registerPlugin(PluginManager &pluginManager)
{
    HelloWorldLibrary test;
}
