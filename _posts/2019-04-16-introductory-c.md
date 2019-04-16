---
author: "Professor Dimitrios Psaltis"
title: "Introductory C programming for astrophysicists"
---

Dr. Psaltis gave a one-hour crash course on C programming based on [material from his class](http://u.arizona.edu/~dpsaltis/Phys305/text.html).

[Slides](/downloads/2018-19/introductory-c/IntroToC.pdf) (PDF)

## Code listings

### `ex1.c`

Compile with `gcc ./ex1.c -o ex1`, run with `./ex1`.

```
#include <stdio.h>

int main(void) {
    float x;
    for (x = 0; x <= 1; x += 0.1) {
        printf("x = %10.8f f(x) %10.8f\n", x, x * x);
    }
    return 0;
}
```

### `ex2.c`

Compile with `gcc ./ex1.c -o ex2`, run with `./ex2`.

(**Note:** Linux needs you to compile with `gcc ./ex1.c -o ex2 -lm`. See [this StackOverflow answer](https://stackoverflow.com/questions/1033898/why-do-you-have-to-link-the-math-library-in-c) for historical context.)

```
#include <stdio.h>
#include <math.h>
#include <time.h>
#define Nrep 1000000
int main(void) {
    double x=1.3, a;
    double time, Mflops;
    int i;
    clock_t ticks1, ticks2;
    ticks1 = clock();
    for (i=1;i<=Nrep;i++) {
        a=x+x;
    }
    ticks2=clock();
    time=(1.0*(ticks2-ticks1))/CLOCKS_PER_SEC/Nrep;
    Mflops=1.e-6/time;
    printf("it took %e seconds\n",time);
    printf("this corresponds to %f MFLOPS\n",Mflops);
    return 0;
}
```

Substitute the loop body (`a = x + x`) with lines from the following block, and see how the number of MFLOPS changes.

```
a=i*x;
a=i/x;
a=i/x/x;
a=i/(x*x);
a=sin(x)*sin(x)+2.*cos(x)*cos(x);
a=1.+cos(x)*cos(x);
a=log(x);
a=pow(x,5.);
a=x*x*x*x*x;
a=i/sqrt(pow(sin(x),2.000001)+2.*pow(cos(x),2.000001));
a=i*pow(1.+cos(x)*cos(x),-0.5);
```