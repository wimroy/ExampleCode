#include <stdio.h>

#ifdef __cplusplus
    extern "C" {
#endif
int myprint(void);
#ifdef __cplusplus
}
#endif

int myprint()
{
    printf("hello world\n");
    return 100;
}
