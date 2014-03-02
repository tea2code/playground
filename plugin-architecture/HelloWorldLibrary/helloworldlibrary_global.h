#ifndef HELLOWORLDLIBRARY_GLOBAL_H
#define HELLOWORLDLIBRARY_GLOBAL_H

#if defined(__GNUC__)

    #if defined(HELLOWORLDLIBRARY_LIBRARY)
        #define HELLOWORLDLIBRARY_API __attribute__ ((visibility ("default")))
    #endif

#else

    #error Unknown compiler, please implement shared library macros.

#endif

#endif // HELLOWORLDLIBRARY_GLOBAL_H
