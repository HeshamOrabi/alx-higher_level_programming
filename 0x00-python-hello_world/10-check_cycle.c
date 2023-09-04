#include "lists.h"
/**
 *
*/
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;

	while (list)
	{
		if (head == list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
