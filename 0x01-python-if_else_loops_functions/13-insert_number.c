#include "lists.h"

/**
 * get_index - get the index of the new node
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: index of the new node
 */
int get_index(listint_t **head, int number)
{
	int index = 0;
	listint_t *tmp;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (0);

	tmp = *head;
	while (tmp != NULL)
	{
		if (number < tmp->n)
			return (index);
		index++;
		tmp = tmp->next;
	}

	return (index);
}

/**
 * insert_node - insert new node into the linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *last;
	int index, len = 0;

	new = malloc(sizeof(listint_t));
	index = get_index(head, number);

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	last = *head;

	if (index == 0)
	{
		new->next = last;
		*head = new;
		return (new);
	}

	while (len < (index - 1))
	{
		if (last == NULL || last->next == NULL)
			return (NULL);

		last = last->next;
		len++;
	}

	new->next = last->next;
	last->next = new;

	return (new);
}

