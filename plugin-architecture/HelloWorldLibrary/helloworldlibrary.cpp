#include "helloworldlibrary.h"

#include <iostream>

HelloWorldLibrary::HelloWorldLibrary()
{}

void HelloWorldLibrary::greet(DataInterface* data)
{
    data->greet("Lalalalala");
}

REGISTER_PLUGIN(HelloWorldLibrary)
