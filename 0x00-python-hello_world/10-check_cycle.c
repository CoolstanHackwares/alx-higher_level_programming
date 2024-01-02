#include "lists.h"

/**
 * check_cycle - A program that checks if a linked list contains a cycle
 * @list: The linked list to check
 *
 * Return: 1 if the list contains a cycle, 0 if it doesn't
 *This program conforms to the betty documentation style
 **/

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *z = list;

	if (!list)
	return (0);

	while (a && z && z->next)
{
	a = a->next;
	z = z->next->next;
	if (a == z)
	return (1);
}
	return (0);
}
