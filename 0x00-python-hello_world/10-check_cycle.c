#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *next;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;
	next = list->next;

	while (next && next->next != NULL)
	{
		if (head == next)
		{
			return (1);
		}

		head = head->next;
		next = next->next->next;
	}

	return (0);
}
