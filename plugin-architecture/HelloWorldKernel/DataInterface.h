#ifndef DATAINTERFACE_H
#define DATAINTERFACE_H

#include <string>

class DataInterface
{
public:
    virtual ~DataInterface() {}
    virtual void greet(std::string text) = 0;
};

#endif // DATAINTERFACE_H
