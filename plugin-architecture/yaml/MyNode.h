#ifndef MYNODE_H
#define MYNODE_H

#include <boost/iterator/transform_iterator.hpp>
#include <yaml-cpp/yaml.h>

#include <string>

class MyNode
{
public:
    MyNode(YAML::Node node);
    MyNode getNode(std::string key);
    std::string getString(std::string key);

    struct getMyNodes
    {
        MyNode operator()(YAML::Node node) const
        {
            return MyNode(node);
        }
    };

    typedef boost::transform_iterator<getMyNodes, YAML::Node::iterator> iterator;
    typedef iterator const_iterator;

    iterator begin()
    {
        return boost::make_transform_iterator(node.begin(), getMyNodes());
    }

    iterator end()
    {
        return boost::make_transform_iterator(node.end(), getMyNodes());
    }

private:
    YAML::Node node;
};

#endif // MYNODE_H
