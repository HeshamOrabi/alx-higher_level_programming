#include "lists.h"

/**
 *
 *
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (!(*head) || !number)
		return(NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return(NULL);

	new->n = number;
	new->next = NULL;


	temp = *head;
	while (temp)
	{
		if ((temp->next)->n < number)
			temp = temp->next;
		else
			break;
	}

	new->next = temp->next;
	temp->next = new;

	return(new);
}
