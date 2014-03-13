#include <boost/iterator/transform_iterator.hpp>

#include <iostream>
#include <iterator>
#include <string>
#include <vector>

class BaseIterator;

template<class IteratorImpl, class Value>
class Iterator
{
public:
    typedef Iterator self_type;
    typedef Value value_type;
    typedef Value& reference;
    typedef Value* pointer;
    typedef std::forward_iterator_tag iterator_category;
    typedef int difference_type;

    Iterator(IteratorImpl *iterator) : iterator(iterator) {}

    self_type operator++() { self_type i = *this; (*iterator)++; return i; }
    self_type operator++(int junk) { (*iterator)++; return *this; }
    reference operator*() { return *(*iterator); }
    pointer operator->() { return &(*(*iterator)); }
    bool operator==(const self_type& rhs) { return *iterator == *rhs.iterator; }
    bool operator!=(const self_type& rhs) { return *iterator != *rhs.iterator; }

private:
    IteratorImpl *iterator;
};

class Base
{
public:
    virtual Iterator<BaseIterator, Base> begin() = 0;
    virtual Iterator<BaseIterator, Base> end() = 0;

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
    virtual bool operator==(const self_type& rhs) = 0;
    virtual bool operator!=(const self_type& rhs) = 0;
};

class Derived;

class DerivedIterator : public BaseIterator
{
public:
    DerivedIterator(std::vector<Derived*>::iterator iterator) : iterator(iterator) {}

    self_type* operator++();
    self_type* operator++(int junk);
    reference operator*();
    pointer operator->();
    bool operator==(const self_type& rhs);
    bool operator!=(const self_type& rhs);

private:
    std::vector<Derived*>::iterator iterator;
};

class Derived : public Base
{
public:
    Derived(std::string name) : n(name) {}

    Iterator<BaseIterator, Base> begin()
    {
        return Iterator<BaseIterator, Base>(new DerivedIterator(v.begin()));
    }

    Iterator<BaseIterator, Base> end()
    {
        return Iterator<BaseIterator, Base>(new DerivedIterator(v.end()));
    }

    std::string name()
    {
        return n;
    }

    std::vector<Derived*> v;
    std::string n;
};

DerivedIterator::self_type* DerivedIterator::operator++() { self_type* i = this; iterator++; return i; }
DerivedIterator::self_type* DerivedIterator::operator++(int) { iterator++; return this; }
DerivedIterator::reference DerivedIterator::operator*() { return *(*iterator); }
DerivedIterator::pointer DerivedIterator::operator->() { return *iterator; }
bool DerivedIterator::operator==(const BaseIterator::self_type& rhs) { return iterator == dynamic_cast<const DerivedIterator&>(rhs).iterator; }
bool DerivedIterator::operator!=(const BaseIterator::self_type& rhs) { return iterator != dynamic_cast<const DerivedIterator&>(rhs).iterator; }

int main()
{
    Derived* derived = new Derived("1");
    derived->v.push_back(new Derived("2"));
    derived->v.push_back(new Derived("4"));
    derived->v.push_back(new Derived("3"));
    derived->v.push_back(new Derived("1"));

    Base* base = derived;
    for(auto& value : *base)
    {
        std::cout << value.name() << std::endl;
    }

    std::cout << std::distance(base->begin(), base->end()) << std::endl;

    return 0;
}

