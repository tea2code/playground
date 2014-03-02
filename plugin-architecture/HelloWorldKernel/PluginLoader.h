#ifndef PLUGINLOADER_H
#define PLUGINLOADER_H

#include <stdexcept>
#include <string>
#include <windows.h>

class PluginLoader
{
public:
    typedef HMODULE HandleType;

public:
    static HandleType load(const std::string &path)
    {
        std::string pathWithExtension = path + ".dll";

        HMODULE moduleHandle = ::LoadLibraryA(pathWithExtension.c_str());
        if(moduleHandle == NULL)
        {
            throw std::runtime_error("Could not load DLL");
        }

        return moduleHandle;
    }

    static void unload(HandleType sharedLibraryHandle)
    {
        BOOL result = ::FreeLibrary(sharedLibraryHandle);
        if(result == FALSE)
        {
            throw std::runtime_error("Could not unload DLL");
        }
    }

    template<typename TSignature>
    static TSignature *getFunctionPointer(HandleType sharedLibraryHandle,
                                          const std::string &functionName)
    {
        FARPROC functionAddress = ::GetProcAddress(sharedLibraryHandle,
                                                   functionName.c_str());
        if(functionAddress == NULL)
        {
            throw std::runtime_error("Could not find exported function");
        }

        return reinterpret_cast<TSignature *>(functionAddress);
    }
};

#endif // PLUGINLOADER_H
