#ifndef HELLOWORLDLIBRARY_H
#define HELLOWORLDLIBRARY_H

#include "../HelloWorldKernel/DataInterface.h"
#include "../HelloWorldKernel/PluginApi.h"

class HelloWorldLibrary : public PluginApi
{
public:
    HelloWorldLibrary();
    void greet(DataInterface* data);
};

#endif // HELLOWORLDLIBRARY_H
