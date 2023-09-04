#include "lists.h"
/**
 * check_cycle - check if linked list goes in cycles
 * @list: head of linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *head;

	if (!list)
		return (0);

	head = list;

	while (list)
	{
		if (head == list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
