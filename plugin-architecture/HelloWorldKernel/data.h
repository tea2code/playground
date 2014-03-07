#ifndef DATA_H
#define DATA_H

#include "DataInterface.h"

class Data : public DataInterface
{
public:
    Data();
    virtual void greet(std::string text);

private:
    std::string text;
};

#endif // DATA_H
