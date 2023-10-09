#include "lists.h"

/**
 * get_length - get the length of listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: length of the linked list
 */
int get_length(listint_t **head)
{
	int length = 0;
	listint_t *current;

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		length++;
	}

	return (length);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, len = 0;
	int *values;

	if (head == NULL || *head == NULL)
		return (1);

	current = *head;
	len = get_length(head);
	values = (int *)malloc(sizeof(int) * len);
	if (values == NULL)
		return (0);

	for (i = 0; i < len; i++)
	{
		values[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (values[i] != values[len - i - 1])
			return (0);
	}

	free(values);

	return (1);
}
