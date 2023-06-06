#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
/**
 * struct listint_s - single linked list
 * @n: integer
 * @next: points to next nod
 * Description: single linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);

#endif /* LISTS_H */
