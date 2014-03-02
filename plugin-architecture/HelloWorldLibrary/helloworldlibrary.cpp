#include "helloworldlibrary.h"

#include <iostream>

HelloWorldLibrary::HelloWorldLibrary()
{}

void HelloWorldLibrary::greet()
{
    std::cout << "Greetings" << std::endl;
}

REGISTER_PLUGIN()
{
    return std::make_shared<HelloWorldLibrary>();
}
