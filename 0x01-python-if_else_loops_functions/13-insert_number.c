#include "lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: the head pointer
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return(NULL);

	new->n = number;
	new->next = NULL;

	if (!(*head) || number < (*head)->n)
	{
		new->next = (*head);
		*head = new;
		return(new);
	}

	temp = *head;
	while (temp->next && (temp->next)->n < number)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;

	return(new);
}
