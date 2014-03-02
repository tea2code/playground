#ifndef HELLOWORLDLIBRARY_H
#define HELLOWORLDLIBRARY_H

#include "../HelloWorldKernel/PluginApi.h"

class HelloWorldLibrary : public PluginApi
{
public:
    HelloWorldLibrary();
    void greet();
};

#endif // HELLOWORLDLIBRARY_H
