#include "MyNode.h"

MyNode::MyNode(YAML::Node node)
    : node(node)
{
}

MyNode MyNode::getNode(std::string key)
{
    return MyNode(node[key]);
}

std::string MyNode::getString(std::string key)
{
    return node[key].as<std::string>();
}
