// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45
#define ABCLENGTH 26

typedef struct stats
{
    unsigned int length;
    unsigned int count;
    unsigned int weight;
} stats;

// extern stats wordLengths[LENGTH+1];

// Prototypes
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);


void print_buckets(void);
void initHashSettings(FILE *fp);
void initPrimePowerCache();
void initCharHashMRUHash();
void statFile(FILE *fp, stats *wordLengths);
void swap(stats *left, stats *right);
void do_sort(size_t size, stats n[]);
unsigned int checkMaxHashLength(unsigned int currentLength);

#endif // DICTIONARY_H