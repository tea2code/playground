#include <boost/iterator/transform_iterator.hpp>

#include <algorithm>
#include <iostream>
#include <iterator>
#include <memory>
#include <string>
#include <vector>

class BaseIterator;

template<class IteratorImpl, class Value, class Reference, class Pointer>
class Iterator
{
public:
    typedef Iterator self_type;
    typedef Value value_type;
    typedef Reference reference;
    typedef Pointer pointer;
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
    using BaseItr = Iterator<BaseIterator, std::shared_ptr<Base>, std::shared_ptr<Base>, std::shared_ptr<Base>>;

    virtual BaseItr begin() = 0;
    virtual BaseItr end() = 0;

    virtual std::string name() = 0;
};

class BaseIterator
{
public:
    typedef BaseIterator self_type;
    typedef std::shared_ptr<Base> value_type;
    typedef std::shared_ptr<Base> reference;
    typedef std::shared_ptr<Base> pointer;
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
    DerivedIterator(std::vector<std::shared_ptr<Derived>>::iterator iterator) : iterator(iterator) {}

    self_type* operator++();
    self_type* operator++(int junk);
    reference operator*();
    pointer operator->();
    bool operator==(const self_type& rhs);
    bool operator!=(const self_type& rhs);

private:
    std::vector<std::shared_ptr<Derived>>::iterator iterator;
};

class Derived : public Base
{
public:
    Derived(std::string name) : n(name) {}

    Base::BaseItr begin()
    {
        return Base::BaseItr(new DerivedIterator(v.begin()));
    }

    Base::BaseItr end()
    {
        return Base::BaseItr(new DerivedIterator(v.end()));
    }

    std::string name()
    {
        return n;
    }

    std::vector<std::shared_ptr<Derived>> v;
    std::string n;
};

DerivedIterator::self_type* DerivedIterator::operator++() { self_type* i = this; iterator++; return i; }
DerivedIterator::self_type* DerivedIterator::operator++(int) { iterator++; return this; }
DerivedIterator::reference DerivedIterator::operator*() { return *iterator; }
DerivedIterator::pointer DerivedIterator::operator->() { return *iterator; }
bool DerivedIterator::operator==(const BaseIterator::self_type& rhs) { return iterator == dynamic_cast<const DerivedIterator&>(rhs).iterator; }
bool DerivedIterator::operator!=(const BaseIterator::self_type& rhs) { return iterator != dynamic_cast<const DerivedIterator&>(rhs).iterator; }

int main()
{
    // Our

    std::shared_ptr<Derived> derived = std::make_shared<Derived>("1");
    derived->v.push_back(std::make_shared<Derived>("2"));
    derived->v.push_back(std::make_shared<Derived>("4"));
    derived->v.push_back(std::make_shared<Derived>("3"));
    derived->v.push_back(std::make_shared<Derived>("1"));

    std::shared_ptr<Base> base = derived;
    for(const auto& value : *base)
    {
        std::cout << value->name() << std::endl;
    }

    std::cout << std::distance(base->begin(), base->end()) << std::endl;
    std::cout << std::endl;

    // Vector

    std::vector<std::shared_ptr<Derived>> v = derived->v;

    for(const auto& value : v)
    {
        std::cout << value->name() << std::endl;
    }

    std::cout << std::distance(v.begin(), v.end()) << std::endl;
    std::cout << std::endl;

    // Vector sorted

    std::sort(v.begin(), v.end());

    for(const auto& value : v)
    {
        std::cout << value->name() << std::endl;
    }

    std::cout << std::distance(v.begin(), v.end()) << std::endl;
    std::cout << std::endl;

    return 0;
}

