// Force-included (g++ -include echo.h) only for the PDF transcripts: copies what the program reads from
// cin onto cout, so piped input shows up on screen the way typed input does in a real console.
#include <iostream>

struct EchoBuf : std::streambuf
{
    std::streambuf *src;
    int cur = EOF;
    bool have = false, newlineShown = false;
    explicit EchoBuf(std::streambuf *s) : src(s) {}
    int fetch()
    {
        if (!have) { cur = src->sbumpc(); have = true; newlineShown = false; }
        return cur;
    }
    int underflow() override            // peek: a peeked newline = the user pressed Enter
    {
        int c = fetch();
        if (c == '\n' && !newlineShown) { std::cout.put('\n'); newlineShown = true; }
        return c;
    }
    int uflow() override                // consume
    {
        int c = fetch();
        have = false;
        if (c != EOF && !(c == '\n' && newlineShown)) std::cout.put((char)c);
        return c;
    }
};

static struct EchoInit
{
    EchoInit() { static EchoBuf b(std::cin.rdbuf()); std::cin.rdbuf(&b); }
} echoInit;
