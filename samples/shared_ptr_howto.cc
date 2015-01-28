#include <boost/smart_ptr.hpp>
#include <iostream>

class A {
	int num;
public:
	typedef boost::shared_ptr<A> Ptr; //note here, this typedef is 

	A(int p_num) : num(p_num) {}

	void hello() {
		std::cout << "hey" << std::endl;
	}

	virtual ~A() {
		std::cout << "--> A's destructor is called" << std::endl;
	}
};

class B {
	boost::shared_ptr<A> a;
public:
	void useA() {
		a->hello();
	}

	virtual ~B() {
		std::cout << "--> B's destructor is called" << std::endl;
	}

	B(boost::shared_ptr<A> p_a) : a(p_a) {}
};

int main(int arc, char** argv) {
	A::Ptr shared_a(new A(42)); //instantiation of a shared pointer by a pointer(which is necessery)

	{ //scope 
		std::cout << "new scope" << std::endl;

		B b(shared_a); //instantiation of a B using shared_a (a shared pointer)
	
		std::cout << "end of scope, B's destructor will be called, not A's, because it is still referenced in \"shared_a\"." << std::endl;
	}

	std::cout << "now that main finishes, A's destructor will be called because \"shared_a\"'s is called." << std::endl;

	return 0;
}