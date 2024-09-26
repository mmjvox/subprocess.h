#include "subprocess.h"

int main()
{
    const char *command_line[] = {"echo", "\"Hello, world!\"", NULL};
    struct subprocess_s subprocess;
    int result = subprocess_create(command_line, 0, &subprocess);
    if (0 != result) {
        // an error occurred!
    }

    return 0;
}
