#include "data.h"

#include <iostream>

Data::Data()
{

}

void Data::greet(std::string text)
{
    this->text = text;
    std::cout << text << "25345" << std::endl;
}
