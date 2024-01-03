#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - A program that inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: The number to insert in the new node
 *
 * Return: The address of the new node, or NULL
 * This program conforms to the betty documentation style
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_number = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new_number = malloc(sizeof(listint_t));
	if (!new_number)
		return (NULL);
	new_number->n = number;
	new_number->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_number->next = *head;
		return (*head = new_number);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new_number;
		new_number->next = current;
	}


	return (new_number);
}
