#ifndef PLUGINAPI_H
#define PLUGINAPI_H

#if defined(__GNUC__)

    #if defined(PLUGIN_LIBRARY)
        // Prevent problems with visibility in GCC.
        // See http://gcc.gnu.org/wiki/Visibility
        #define PLUGIN_API __attribute__ ((visibility ("default")))
    #endif

#elif defined(_MSC_VER)

    #if defined(PLUGIN_LIBRARY)
        // Building the library.
        #define PLUGIN_API __declspec(dllexport)
    #else
        // Building a client application which should use a library.
        #define PLUGIN_API __declspec(dllimport)
    #endif

#else

    #error Unknown compiler, please implement shared library macros.

#endif

#include "DataInterface.h"

class PluginApi
{
public:
    virtual ~PluginApi() {}
    virtual void greet(DataInterface* data) = 0;
};

#if defined(PLUGIN_API)

//    #include "PluginManager.h"

    #include <memory>

/*
    #define REGISTER_PLUGIN(className) extern "C" PLUGIN_API void registerPlugin(PluginManager &pluginManager)\
    {\
        auto plugin = std::make_shared<className>();\
        pluginManager.addPlugin(plugin);\
    }\
*/

    #define REGISTER_PLUGIN(pluginClass) extern "C" PLUGIN_API std::shared_ptr<PluginApi> registerPlugin()\
    {\
        return std::make_shared<pluginClass>();\
    }\

    extern "C" PLUGIN_API int getEngineVersion()
    {
      return 5;
    }

#endif

#endif // PLUGINAPI_H
