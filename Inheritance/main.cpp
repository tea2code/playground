#include <boost/iterator/transform_iterator.hpp>

#include <iostream>
#include <string>
#include <vector>

template<class Iterator>
class Base
{
public:
    virtual Iterator begin() = 0;
    virtual Iterator end() = 0;
};

struct toString
{
    std::string operator()(int number) const
    {
        return std::to_string(number);
    }
};

typedef boost::transform_iterator<toString, std::vector<int>::iterator> TransformIterator;

class Derived : public Base<TransformIterator>
{
public:
    Derived() : ints{132, 3, 6451, 12, 5} {}

    TransformIterator begin()
    {
        return boost::make_transform_iterator(ints.begin(), toString());
    }

    TransformIterator end()
    {
        return boost::make_transform_iterator(ints.end(), toString());
    }

private:
    std::vector<int> ints;
};

int main()
{
    Base<TransformIterator>* obj = new Derived();
    for(const auto& value : *obj)
    {
        std::cout << value.size() << std::endl;
    }
    return 0;
}

