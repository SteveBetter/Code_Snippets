#include <time.h>

char time_stamp[100];
time_t t;
struct tm *lt;

time(&t);
lt = localtime(&t);

sprintf(time_stamp, "%04d%02d%02d%02d%02d%02d", lt->tm_year + 1900, lt->tm_mon + 1, lt->tm_mday, lt->tm_hour, lt->tm_min, lt->tm_sec);
