#include <boost/iterator/transform_iterator.hpp>

#include <iostream>
#include <iterator>
#include <string>
#include <vector>

class BaseIterator;

class Base
{
public:
    virtual BaseIterator* begin() = 0;
    virtual BaseIterator* end() = 0;

    virtual std::string name() = 0;
};

class BaseIterator
{
public:
    typedef BaseIterator self_type;
    typedef Base value_type;
    typedef Base& reference;
    typedef Base* pointer;
    typedef std::forward_iterator_tag iterator_category;
    typedef int difference_type;

    virtual self_type* operator++() = 0;
    virtual self_type* operator++(int junk) = 0;
    virtual reference operator*() = 0;
    virtual pointer operator->() = 0;
    virtual bool operator==(self_type* rhs) = 0;
    virtual bool operator!=( self_type* rhs) = 0;
};

class Derived;

class DerivedIterator : public BaseIterator
{
public:
    DerivedIterator(std::vector<Derived*>::iterator iterator) : iterator(iterator) { }
    self_type* operator++() { self_type* i = new DerivedIterator(iterator); iterator++; return i; }
    self_type* operator++(int junk) { iterator++; return new DerivedIterator(iterator); }
    reference operator*();
    pointer operator->();
    bool operator==(self_type* rhs);
    bool operator!=(self_type* rhs);

private:
    std::vector<Derived*>::iterator iterator;
};

class Derived : public Base
{
public:
    Derived(std::string name) : n(name) {}

    BaseIterator* begin()
    {
        return new DerivedIterator(v.begin());
    }

    BaseIterator* end()
    {
        return new DerivedIterator(v.end());
    }

    std::string name()
    {
        return n;
    }

    std::vector<Derived*> v;
    std::string n;
};

BaseIterator::reference DerivedIterator::operator*() { return *(*iterator); }
BaseIterator::pointer DerivedIterator::operator->() { return *iterator; }
bool DerivedIterator::operator==(BaseIterator::self_type* rhs) { return iterator == dynamic_cast<DerivedIterator*>(rhs)->iterator; }
bool DerivedIterator::operator!=(BaseIterator::self_type* rhs) { return iterator != dynamic_cast<DerivedIterator*>(rhs)->iterator; }

int main()
{
    Derived* d = new Derived("1");
    d->v.push_back(new Derived("2"));
    d->v.push_back(new Derived("3"));

    Base* obj = d;
    for(auto& value : *obj)
    {
        std::cout << value->name() << std::endl;
    }

    return 0;
}

