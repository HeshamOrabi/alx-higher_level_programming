#include "lists.h"

/**
*/
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *end = *head;
	int len = 0, llen, i = 1;

	if (!head || !*head)
		return (1);

	while (end->next)
	{
		end = end->next;
		len++;
	}

	llen = len;
	while (start != end && end != start->next)
	{
		end = *head;

		while (llen)
		{
			end = end->next;
			llen--;
		}

		if (start->n != end->n)
			return (0);

		llen = len - i;
		start = start->next;
		i++;
	}
	return (1);
}
