#include "lists.h"

/**
 * cycle - checking if a linked list contains a cycle
 * @list: when at list the link list to check
 *
 * Return: 0 if it doesn't has a cylce, 1 if the list has a cycle,
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
