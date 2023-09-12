#include "lists.h"

/**
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *next = NULL, *prv = NULL;

	if (!head || !*head)
		return (1);

	while (fast && fast->next)
	{
		fast = (fast->next)->next;

		next = slow->next;
		slow->next = prv;
		prv = slow;
		slow = next;
	}

	if (fast)
		slow = slow->next;

	while (slow && prv)
	{
		if (slow->n != prv->n)
			return (0);
		slow = slow->next;
		prv = prv->next;
	}
	return (1);
}
