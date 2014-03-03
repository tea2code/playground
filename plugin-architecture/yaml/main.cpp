#include <yaml-cpp/yaml.h>

#include <iostream>

int main()
{
    YAML::Node node = YAML::Load("helloworld: 42");
    std::cout << node["helloworld"] << std::endl;
    return 0;
}

