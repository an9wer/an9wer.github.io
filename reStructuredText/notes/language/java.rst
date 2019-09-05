Java
====

Fields vs variables:

-   Instance Variables (Non-Static Fields)

-   Class Variables (Static Fields) 

-   Local Variables

-   Parameters


Primitive Data Types:

-   byte

-   short

-   int

-   long

-   float

-   double

-   boolean

-   char

**Note**: *Fields* that are declared but not initialized will be set to a
reasonable default by the compiler. *Local variables* are slightly different;
the compiler never assigns a default value to an uninitialized local variable.

Array:

::

    // declares an array of integers
    int[] anArray;

    // allocates memory for 10 integers
    anArray = new int[10];
       
    // initialize first element
    anArray[0] = 100;

Declaring Class:

::

    class MyClass extends MySuperClass implements YourInterface {
        // field, constructor, and
        // method declarations
    }

Inheritance:

::

    class MountainBike extends Bicycle {

        // new fields and methods defining 
        // a mountain bike would go here

    }

Interface:

::

    class ACMEBicycle implements Bicycle {

        // new fields and methods defining 
        // a ACME bike would go here

    }

**Note**: A class can only extend (subclass) one parent, but can implememt more
than one interface.

Access modifiers:

-   public: the field is accessible from all classes.

-   private: the field is accessible only within its own class.


Method signature:

Two of the components of a method declaration comprise the method signature --
the method's name and the parameter types:

::

    calculateAnswer(double, int, double, double)

Overloading methods:

The Java programming language supports overloading methods, and Java can
distinguish between methods with different method signatures. This means that
methods within a class can have the same name if they have different parameter
lists:

::

    public class DataArtist {
        ...
        public void draw(String s) {
            ...
        }
        public void draw(int i) {
            ...
        }
        public void draw(double f) {
            ...
        }
        public void draw(int i, double f) {
            ...
        }
    }

Constructors:

Constructor declarations look like method declarations—except that they use the
name of the class and have no return type.

::

    class Bicyle {

        public Bicycle(int startCadence, int startSpeed, int startGear) {
            gear = startGear;
            cadence = startCadence;
            speed = startSpeed;
        }

        public Bicycle() {
            gear = 1;
            cadence = 10;
            speed = 0;
        }

    }

**Note**: The compiler automatically provides a no-argument, default
constructor for any class without constructors. This default constructor will
call the no-argument constructor of the superclass. In this situation, the
compiler will complain if the superclass doesn't have a no-argument constructor
so you must verify that it does. If your class has no explicit superclass, then
it has an implicit superclass of Object, which does have a no-argument
constructor.

Parameters vs arguments:

Parameters refers to the list of variables in a method declaration. Arguments
are the actual values that are passed in when the method is invoked. When you
invoke a method, the arguments used must match the declaration's parameters in
type and order. 

Varargs:

To use varargs, you follow the type of the last parameter by an ellipsis (three
dots, ...), then a space, and the parameter name. The method can then be called
with any number of that parameter, including none.

::

    // Method definition
    public PrintStream printf(String format, Object... args)

    // Method call
    System.out.printf("%s: %d, %s%n", name, idnum, address);

    // Method call
    System.out.printf("%s: %d, %s, %s, %s%n", name, idnum, address, phone, email);

Shadowing field:

A parameter can have the same name as one of the class's fields. If this is the
case, the parameter is said to shadow the field. Shadowing fields can make your
code difficult to read and is conventionally used only within constructors and
methods that set a particular field. 

::

    public class Circle {

        private int x, y, radius;

        public void setOrigin(int x, int y) {
            // Parameter x, y will shadow the field x, y
            ...
        }

    }

References
----------

`JavaSE tutorial <https://docs.oracle.com/javase/tutorial/index.html>`_
