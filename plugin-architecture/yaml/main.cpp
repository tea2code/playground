#include "MyNode.h"

#include <yaml-cpp/yaml.h>

#include <iostream>
#include <string>
#include <map>


int main()
{
    YAML::Node node = YAML::LoadFile("F:/Programmieren/playground/plugin-architecture/yaml/test.yaml");

    MyNode myNode(node);
    std::cout << myNode.getString("test") << std::endl;

    MyNode myListNode = myNode.getNode("list");
    for(MyNode listNodeItem : myListNode)
    {
        std::cout << listNodeItem.getString("key") << std::endl;
    }

    return 0;
}

