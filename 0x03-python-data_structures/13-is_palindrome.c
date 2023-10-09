#include "lists.h"

/**
 * reverse_list - reverse structure of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: address of the new element or NULL if it fails
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next;

	if (*head == NULL)
		return (NULL);

	while (*head == NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;
	listint_t *current = *head;
	listint_t *reverse = reverse_list(head);
	int i, len = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (copy != NULL)
	{
		len++;
		copy = copy->next;
	}

	for (i = 0; i < (len / 2); i++)
	{
		if (current != reverse)
			return (0);

		current = current->next;
		reverse = reverse->next;
	}

	return (1);
}

